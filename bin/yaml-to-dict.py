#!/usr/bin/env python3

import yaml
import sys
import pprint

with open(sys.argv[1], 'r') as stream:
    try:
        pp = pprint.PrettyPrinter(indent=4, width=1024)
        d = yaml.safe_load(stream)
        pp.pprint(d)
    except yaml.YAMLError as exc:
        print(exc)
