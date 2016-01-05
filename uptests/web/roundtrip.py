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
data = "dparrot uptest"
headers={
	'Content-Type': 'text/plain',
}
resp = requests.post(root, data=data, headers=headers)
assert resp.headers['Access-Control-Allow-Origin'] == '*'
new_url = resp.json()['url']
assert requests.get(new_url).text == data
