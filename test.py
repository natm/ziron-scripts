#!/usr/bin/env python3

import dateutil
import logging
import os
import sys
import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

LOG = logging.getLogger(__name__)
VERSION = 0.1


def account_request(path="", params=None):
    account_sid = os.environ.get("ZIRON_ACCOUNT_SID")
    auth_token = os.environ.get("ZIRON_AUTH_TOKEN")
    auth = HTTPBasicAuth(account_sid, auth_token)
    resp = requests.get("https://api.ziron.com/v1/Accounts/{account_sid}{path}".format(account_sid=account_sid, path=path), auth=auth, params=params)
    return resp.json()

def get_calls():
    page = 0
    pages = 1
    offset = 0
    calls = []
    while page < pages:
        page = page + 1
        call_request = account_request(path="/Calls", params={"offset": offset})
        pages = call_request["meta"]["last_page"]
        offset = offset + len(call_request["result"])
        calls.extend(call_request["result"])
    return calls

def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)8s [%(asctime)s] %(message)s')
    account = account_request()
    print("Account %s" % account["account_ref"])
    print("Balance %s %s" % (account["balance"], account["currency"]))


    all_calls = get_calls()
    calls_df = pd.DataFrame(all_calls)
    calls_df["charge"] = calls_df["charge"].astype(float)
    calls_df["call_duration"] = calls_df["call_duration"].astype(float)
    calls_df["ts"] = calls_df["ts"].apply(dateutil.parser.parse)
    calls_df["month"] = calls_df["ts"].map(lambda x: x.strftime('%Y-%m'))
    print(calls_df)

    print("\nCalls made to: %s" % list(calls_df.groupby(["rate_destination"]).groups.keys()))
    print("\nMonthly summary")
    print(calls_df.groupby(["month", "type"]).agg({"sid": "count", "charge": "sum", "call_duration": "sum"}).rename(columns={"sid": "calls"}))
    print("\nInbound calls by destination")
    print(calls_df[calls_df["type"]=="call-in"].groupby(["dst"])["sid"].count().reset_index().rename(columns={"sid": "calls"}).sort_values("calls", ascending=False))
    print("\nOutbound sources")
    print(calls_df[(calls_df["type"] == "call-out") & (calls_df["charge"] > 0)].groupby(["src"]).agg(
        {"sid": "count", "charge": "sum"}).rename(columns={"sid": "calls"}).sort_values("charge", ascending=False))
    print("\nOutbound rate destinations")
    print(calls_df[(calls_df["type"] == "call-out") & (calls_df["charge"] > 0)].groupby(["rate_destination"]).agg({"sid": "count", "charge": "sum", "call_duration": "sum"}).rename(columns={"sid": "calls"}))
    sys.exit(0)


if __name__ == "__main__":
    main()