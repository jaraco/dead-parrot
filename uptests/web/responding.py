#!/usr/bin/env python

import argparse

import requests
import portend

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port', type=int)
args = parser.parse_args()
portend.occupied(args.host, args.port, timeout=10)

root = 'http://{host}:{port}/'.format(**vars(args))
resp = requests.get(root)
# parrot returns 404 for /
assert resp.status_code == 404
