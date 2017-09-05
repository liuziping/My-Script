#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import random
import time
import json
import hmac
from datetime import datetime, timedelta

from flask import Flask, request, redirect, make_response
from flask.ext import restful
from flask.ext.restful import fields, marshal_with

app = Flask(__name__)
api = restful.Api(app)

users = {
    "magigo": ["123456"]
}

redirect_uri='http://localhost:5000/client/passport'
client_id = '123456'
users[client_id] = []
auth_code = {}

oauth_redirect_uri = []

TIMEOUT = 3600 * 2


# 新版本的token生成器
def gen_token(data):
    '''
    :param data: dict type
    :return: base64 str
    '''
    data = data.copy()
    if "salt" not in data:
        data["salt"] = unicode(random.random()).decode("ascii")
    if "expires" not in data:
        data["expires"] = time.time() + TIMEOUT
    payload = json.dumps(data).encode("utf8")
    # 生成签名
    sig = _get_signature(payload)
    return encode_token_bytes(payload + sig)

# 授权码生成器
def gen_auth_code(uri, user_id):
    code = random.randint(0,10000)
    auth_code[code] = [uri, user_id]
    return code

# 新版本的token验证
def verify_token(token):
    '''
    :param token: base64 str
    :return: dict type
    '''
    decoded_token = decode_token_bytes(str(token))
    payload = decoded_token[:-16]
    sig = decoded_token[-16:]
    # 生成签名
    expected_sig = _get_signature(payload)
    if sig != expected_sig:
        return {}
    data = json.loads(payload.decode("utf8"))
    if data.get('expires') >= time.time():
        return data
    return 0

# 使用hmac为消息生成签名
def _get_signature(value):
    """Calculate the HMAC signature for the given value."""
    return hmac.new('secret123456', value).digest()

# 下面两个函数将base64编码和解码单独封装
def encode_token_bytes(data):
    return base64.urlsafe_b64encode(data)

def decode_token_bytes(data):
    return base64.urlsafe_b64decode(data)


# 验证服务器端
@app.route('/index', methods=['POST', 'GET'])
def index():
    return 'hello'

@app.route('/login', methods=['POST', 'GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    if users.get(uid)[0] == pw:
        return gen_token(dict(user=uid, pw=pw))
    else:
        return 'error'

@app.route('/oauth', methods=['POST', 'GET'])
def oauth():
    # 处理表单登录， 同时设置Cookie
    if request.method == 'POST' and request.form['user']:
        u = request.form['user']
        p = request.form['pw']
        if users.get(u)[0] == p and oauth_redirect_uri:
            uri = oauth_redirect_uri[0] + '?code=%s' % gen_auth_code(oauth_redirect_uri[0], u)
            expire_date = datetime.now() + timedelta(minutes=1)
            resp = make_response(redirect(uri))
            resp.set_cookie('login', '_'.join([u, p]), expires=expire_date)
            return resp
    # 验证授权码，发放token
    if request.args.get('code'):
        auth_info = auth_code.get(int(request.args.get('code')))
        if auth_info[0] == request.args.get('redirect_uri'):
            # 可以在授权码的auth_code中存储用户名，编进token中
            return gen_token(dict(client_id=request.args.get('client_id'), user_id=auth_info[1]))
    # 如果登录用户有Cookie，则直接验证成功，否则需要填写登录表单
    if request.args.get('redirect_uri'):
        oauth_redirect_uri.append(request.args.get('redirect_uri'))
        if request.cookies.get('login'):
            u, p = request.cookies.get('login').split('_')
            if users.get(u)[0] == p:
                uri = oauth_redirect_uri[0] + '?code=%s' % gen_auth_code(oauth_redirect_uri[0], u)
                return redirect(uri)
        return '''
            <form action="" method="post">
                <p><input type=text name=user>
                <p><input type=text name=pw>
                <p><input type=submit value=Login>
            </form>
        '''


# 客户端
@app.route('/client/login', methods=['POST', 'GET'])
def client_login():
    uri = 'http://localhost:5000/oauth?response_type=code&client_id=%s&redirect_uri=%s' % (client_id, redirect_uri)
    return redirect(uri)

@app.route('/client/passport', methods=['POST', 'GET'])
def client_passport():
    code = request.args.get('code')
    uri = 'http://localhost:5000/oauth?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s' % (code, redirect_uri, client_id)
    return redirect(uri)


# 资源服务器端
# 数据模型
class Test1Data(object):
    def __init__(self, client_id, expires, salt, user_id):
        self.client_id = client_id
        self.expires = expires
        self.salt = salt
        self.user_id = user_id

# marshal-蒙版
resource_fields = {
    'client_id': fields.String(default=''),
    'expires': fields.Float(default=0.0),
    'salt': fields.Float(default=0.0),
    'user_id': fields.String(default=''),
    'date': fields.DateTime(default=str(datetime.now()))

}

# 新的资源服务器
class Test1(restful.Resource):
    @marshal_with(resource_fields)
    def get(self):
        token = request.args.get('token')
        ret = verify_token(token)
        if ret:
            return ret
        else:
            return 'error'

api.add_resource(Test1, '/test1')

if __name__ == '__main__':
    app.run(debug=True)
