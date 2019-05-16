#!/usr/bin/python

import json
from urllib2 import urlopen

public_ip = urlopen('http://ip.42.pl/raw').read()

geo_ip = urlopen('http://api.ipstack.com/' + public_ip + '?access_key=4e31988bbbf6d300f7264c3bc82bffa9&output=json&legacy=1').read()

parsed = json.loads(geo_ip)
public_ip = ("Public IP: ") + (parsed["ip"])
country = ("Country: ") + (parsed["country_name"])

print  public_ip + "\n" + country
