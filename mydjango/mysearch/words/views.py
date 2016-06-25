from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch
def index(request):                 
    return HttpResponse('<h1>hello world</h1>')

   
def search(request):
    if request.method == "GET":
        return render(request,'result.html')
    else:
        query = request.POST['query']
        print query
        es = Elasticsearch(hosts=[{'host':'192.168.1.253', 'port': 9200}])
        res = es.search(
            index = 'baike',
            doc_type = "people",
            body = {
                "query":{
                    'multi_match':{
                       "query":query,
                       "fields":["name","info"]
                        }}})
        result = []
        for source in res['hits']['hits']:
            result.append(source['_source']['info'])
        return render(request,'result.html',{'query':query,'took':res['took'],'total':res['hits']['total'],"result":result})
