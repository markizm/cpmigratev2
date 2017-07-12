#!/usr/bin/python

import requests
import base64
import json
import os
import argparse
import yaml

class Catchpoint (object):

    def __init__(self, testid):
        self.testid = testid
        self.endpoint = None 

    def api_key(self):
        vault_key=str(os.popen('sudo cat /home/t/etc/vault_key').read())
        curl_key_string="curl -sX GET -u " + vault_key + " https://vault.com/values/catchpoint_api_key/key"
        client_key=os.popen(curl_key_string).read()
        return client_key

    def api_secret(self):
        vault_key=str(os.popen('sudo cat /home/t/etc/vault_key').read())
        curl_secret_string="curl -sX GET -u " + vault_key + " https://vault.com/values/catchpoint_api_secret/secret"
        client_secret=os.popen(curl_secret_string).read()
        return client_secret

    def token_(self):
        token_uri = "https://io.catchpoint.com/ui/api/token" 
        client_auth = requests.auth.HTTPBasicAuth(self.api_key(), self.api_secret())
        post_data = {"grant_type": "client_credentials"}
        response = requests.post(token_uri, auth=client_auth, data=post_data)
        token = response.json()
        enc = base64.b64encode(token['access_token'])
        return enc

    def get_tests(self, testid):
        ### returns test properties, provides name, url, status, etc.
        end_point = "https://io.catchpoint.com/ui/api/v1/tests/" + testid 
        headers = {"Authorization": "bearer %s" % self.token_()}
        try:
            response = requests.get(end_point, headers=headers)
            print response.json()
        except Exception as e:
            return e

    def new_test(self, payload):
        ### generates a new test. test configs pulled from get_tests() 
        end_point = "https://io.catchpoint.com/ui/api/v1/tests/" + "0"
        headers = {"Authorization": "bearer %s" % self.token_()}
        try:
            newpost = requests.post(end_point, headers=headers, data=payload)
            if newpost.status_code == 200:
                print "Test successfully created." 
                print "\n"
                print "Navigate to % Division, Staging folder to find new test" % args.divid
            else:
                print newpost.raise_for_status()
                print "Error: Check test configuration, the API only likes inherited settings"
        except Exception as e:
             print e  
