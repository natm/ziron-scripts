# Ziron API scripts

A selection of scripts for working with the [Ziron developer API](https://zironuk.atlassian.net/wiki/spaces/docs/pages/524317/Overview).

[Ziron](https://www.ziron.com/) are a voice and messaging provider, based in the UK offering SIP termination / trunk services. I am not affiliated with them, I'm just a customer.

## Environment variables

These environement variables need to be set prior to running any of the scripts:

* `ZIRON_ACCOUNT_SID`
* `ZIRON_AUTH_TOKEN`

Example:

```
$ export ZIRON_ACCOUNT_SID=ACxxxxxxxxxxxxxxx
$ export ZIRON_AUTH_TOKEN=xxxxxxxxxxxxxxxxx
```


## Scripts

* Outbound calls to special numbers - `xx.py`
* Summary of monthly charged calls by caller ID - `yy.py`
* Monthly call volume in/out summary caller/callee - `cc.py`
* Table of assigned numbers - `zz.py`
* UK available number search - `aa.py`
* UK available number purchase - `bb.py`