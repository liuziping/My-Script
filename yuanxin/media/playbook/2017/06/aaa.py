import ansible.playbook
from ansible import callbacks
from ansible import utils
stats = callbacks.AggregateStats()
playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=2)
pb = ansible.playbook.PlayBook(
    playbook="playbook.yml",
    stats=stats,
    callbacks=playbook_cb,
    runner_callbacks=runner_cb,
    check=True
)

res = pb.run()
print "======================================================="
print res
print "======================================================="
