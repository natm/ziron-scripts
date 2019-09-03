#!/usr/bin/env python3

import dateutil
import logging
import sys
import pandas as pd

from zironcommon import startup_check_envvars, account_request, account_request_pages

LOG = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)8s [%(asctime)s] %(message)s')

    startup_check_envvars()

    country_iso = sys.argv[1]
    area = sys.argv[2]

    # assigned numbers
    areas = pd.DataFrame(account_request(path="/Numbers/Available/{country_iso}".format(country_iso=country_iso)))

    area_df = areas[areas["description"] == area]
    area_sid = area_df["sid"].values[0]

    search_params = {"count": 100}
    if len(sys.argv) == 4:
        search_params["search"] = sys.argv[3]
    numbers = sorted(account_request(path="/Numbers/Available/{area_sid}".format(area_sid=area_sid), params=search_params))
    for number in numbers:
        print(number)

    sys.exit(0)

if __name__ == "__main__":
    main()
