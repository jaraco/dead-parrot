import urllib2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port', type=int)
args = parser.parse_args()

root = 'http://{host}:{port}/'.format(**vars(args))
try:
	urllib2.urlopen(root)
except urllib2.HTTPError as exc:
	# parrot returns 404 for /
	assert exc.code == 404
