#!/usr/bin/env python

import autocommand
import requests
import portend


@autocommand.autocommand(__name__)
def main(host, port: int):
	portend.occupied(host, port, timeout=10)
	resp = requests.get(f'http://{host}:{port}/')
	# parrot returns 404 for /
	assert resp.status_code == 404
