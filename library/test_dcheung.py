#!/usr/bin/python
from ansible.module_utils.basic import *
import json

def main():
    module = AnsibleModule(
        argument_spec = dict(
            name      = dict(required=True),
            enabled   = dict(required=True, type='bool'),
        )
    )
    enabled = module.params['enabled']
    module.exit_json(changed=True, msg="haha\nbooya")

if __name__ == '__main__':
    main()
