#!/usr/bin/env python
import ansible.runner
import json
runner = ansible.runner.Runner(
	module_name='shelld',
	module_args='uptimed',
	pattern='wx-test',
	forks=10
)
data=runner.run()
print json.dumps(data,indent=4)
