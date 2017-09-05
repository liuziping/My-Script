#!/usr/bin/python
import ansible.runner
import sys

results = ansible.runner.Runner(
    pattern='*', forks=10,
    module_name='command', module_args='/bin/df',
).run()
if results is None:
   print "No hosts found"
   sys.exit(1)
for (hostname, result) in results['contacted'].items():
    if not 'failed' in result:
        print "%s ========  %s" % (hostname, result['stdout'])
print "FAILED *******"
for (hostname, result) in results['contacted'].items():
    if 'failed' in result:
        print "%s =========  %s" % (hostname, result['msg'])
print "DOWN *********"
for (hostname, result) in results['dark'].items():
    print "%s ============ %s" % (hostname, result)
