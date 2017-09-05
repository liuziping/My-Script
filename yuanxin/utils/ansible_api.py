# encoding: utf-8
import ansible.runner
import ansible.playbook
import ansible.inventory
from ansible import callbacks
from ansible import utils


class AnsiblePlaybookAPI(object):
    """1.9.x 上通过测试 """
    def __init__(self, playbook, extra_vars={}):   # 初始化参数
        self.stats = callbacks.AggregateStats()
        self.playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
        self.extra_vars = extra_vars
        self.playbook = playbook
        self.setbook = self.book_set()

    def book_set(self):
        #runner_cb = callbacks.PlaybookRunnerCallbacks(self.stats, verbose=utils.VERBOSITY)
        runner_cb = callbacks.PlaybookRunnerCallbacks(self.stats, verbose=2)
        self.pb = ansible.playbook.PlayBook(
            playbook=self.playbook,
            stats =self.stats,
            extra_vars=self.extra_vars,
            callbacks=self.playbook_cb,
            runner_callbacks=runner_cb
        )

    def run(self, log_file='', tmp_log_file=''):
        """
        :param log_file: 总日志文件，会记录每次任务执行的日志
        :param tmp_log_file: 临时日志文件，每次执行完playbook后都会清空
        :return: 
        """
        if log_file:
            callbacks.log_file = log_file
        if tmp_log_file:
            callbacks.tmp_log_file = tmp_log_file
        simple = self.pb.run()
        with open(tmp_log_file, 'r') as f:
            detail = f.read()
        with open(tmp_log_file, 'w') as f:
            pass
        # 添加日志内容到detail
        return {'simple': simple, 'detail': detail}

