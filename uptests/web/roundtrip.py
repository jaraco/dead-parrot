#!/usr/bin/env python

import autocommand
import requests
import portend


@autocommand.autocommand(__name__)
def main(host, port: int):
	portend.occupied(host, port, timeout=10)
	data = "dparrot uptest"
	headers = {
		'Content-Type': 'text/plain',
	}
	resp = requests.post(f'http://{host}:{port}/', data=data, headers=headers)

	assert resp.headers['Access-Control-Allow-Origin'] == '*'
	new_url = resp.json()['url']
	assert requests.get(new_url).text == data
