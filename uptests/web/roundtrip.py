#!/usr/bin/env python

import urllib2
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port', type=int)
args = parser.parse_args()

root = 'http://{host}:{port}/'.format(**vars(args))
data = "dparrot uptest"
req = urllib2.Request(root,
	data=data,
	headers={
		'Content-Type': 'text/plain',
	},
)
resp = urllib2.urlopen(req)
assert resp.headers['Access-Control-Allow-Origin'] == '*'
res = json.loads(resp.read())
new_url = res['url']
assert urllib2.urlopen(new_url).read() == data
