import requests
import base64
import json
import os
import argparse
import yaml
import sys
from cpmigrate import *

## need this in main script for OOP version
## build api endpoint
#uri="https://io.catchpoint.com/ui/api/"
#version="v1"

## just need user to provide testid(s) on cmd line
parser = argparse.ArgumentParser(description='retrieve test_id from user input')
parser.add_argument('-t', '--testid', type=str, help='id for test in catchpoint')
parser.add_argument('-d', '--divid', type=str, help='"client" = client division, "nonprod" = non-prod division, "dev" = dev division')
                    
args = parser.parse_args()

if __name__ == '__main__':
    """
    test_prop = "https://io.catchpoint.com/ui/api/v1/tests/" 
    idt = args.testid
    uri = test_prop + idt
    obj = Catchpoint(uri, idt)
    obj.get_tests(idt)
    """
    f = open('conf.yml')
    conf = yaml.load(f)
    div_ = args.divid
    if div_ == "adplatform":
        obj = Catchpoint(args.testid)
        pr_id = conf['z-stage_product']
        obj['division_id'] = div_
        obj['product_id'] = pr_id
        obj['id'] = 0
        if 'parent_folder_id' in test_prop:
            del_pf()
            json_text = json.dumps(test_prop)
            new_test(json_text)
        else:
            json_text = json.dumps(test_prop)
            new_test(json_text)
    elif div_ == "client":
        obj = Catchpoint(args.testid)
        pr_id = conf['staging_product']
        obj['division_id'] = div_
        obj['product_id'] = pr_id
        obj['id'] = 0
        if 'parent_folder_id' in test_prop:
            del_pf()
            json_text = json.dumps(test_prop)
            new_test(json_text)
        else:
            json_text = json.dumps(test_prop)
            new_test(json_text)
