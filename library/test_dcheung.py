#!/usr/bin/python
from ansible.module_utils.basic import *
import json

def main():
    module = AnsibleModule(
        argument_spec = dict(
          path=dict(required=True, type='list'),
        )
    )
    enabled = module.params['path']
    module.exit_json(changed=True, msg=str(enabled))

if __name__ == '__main__':
    main()
