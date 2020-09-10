#!/usr/bin/env python3

import copy
import os
import sys
import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

VERSION = 0.2

def startup_check_envvars():
    for varname in ["ZIRON_ACCOUNT_SID", "ZIRON_AUTH_TOKEN"]:
        if os.environ.get(varname, None) is None:
            print("Envicronment variable %s must be set" % (varname))
            sys.exit(1)

def account_request(path="", params=None, method="GET", data={}):
    account_sid = os.environ.get("ZIRON_ACCOUNT_SID")
    auth_token = os.environ.get("ZIRON_AUTH_TOKEN")
    auth = HTTPBasicAuth(account_sid, auth_token)
    resp = requests.request(method=method, data=data,
                            url="https://api.ziron.com/v1/Accounts/{account_sid}{path}".format(account_sid=account_sid, path=path), auth=auth, params=params)
    return resp.json()

def account_request_pages(path, params={}):
    page = 0
    pages = 1
    offset = 0
    results = []
    while page < pages:
        page = page + 1
        req_params = copy.copy(params)
        req_params["offset"] = offset
        page_results = account_request(path=path, params=req_params)
        pages = page_results["meta"]["last_page"]
        offset = offset + len(page_results["result"])
        results.extend(page_results["result"])
    return pd.DataFrame(results)
