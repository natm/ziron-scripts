# Ziron API scripts

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/natm/cctv-gif-buffer/master/LICENSE)

A selection of scripts for working with the [Ziron developer API](https://zironuk.atlassian.net/wiki/spaces/docs/pages/524317/Overview).

[Ziron](https://www.ziron.com/) are a voice and messaging provider, based in the UK offering SIP termination / trunk services. I am not affiliated with them, I'm just a customer.

These we developed due to the functionality being missing in their [dashboard](https://dashboard.ziron.com/), I hope these are handy for other customers.

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

## Usage

Setup your environment.

```
virtualenv venv -p python3
source venv/bin/activate
pip3 install -r requirements.txt
```

## License ##

MIT

## Contributing guidelines ##

* Fork the repo
* Create a branch
* Make your changes
* Open a pull request back from your branch to master in this repo

Found a bug? open an [issue](https://github.com/natm/ziron-scripts/issues).
