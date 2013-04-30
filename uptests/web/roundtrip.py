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
res = json.loads(urllib2.urlopen(req).read())
new_url = res['url']
assert urllib2.urlopen(new_url).read() == data
