from pushbullet import Pushbullet
import urlparse
import urllib
import json
import time
import re

import config as c
config = c.config()

pb = Pushbullet(config.pushbullet_access_token)
iPhoneList = config.iPhoneList
iPhone = {}
triedTimes=0

try:

	for i in range(0,len(iPhoneList)):
		parsed = urlparse.urlparse(iPhoneList[i]['reserve_url'])
		partNumber = urlparse.parse_qs(parsed.query)['partNumber'][0]
		iPhone[partNumber]={
			"name":iPhoneList[i]["name"],
			"reserve_url":iPhoneList[i]["reserve_url"],
			"pushed":False,
			"available":False
		}

	print("Started, auto update every 10s, stop using ctrl+c")

	while (True):
		result = ""

		response = urllib.urlopen(config.availability_json)
		availability = json.loads(response.read())

		if availability == {}:
			print("Reserve not available, retry in 20 minutes")
			time.sleep(1200)
			continue

		for partNumber in iPhone:
			iPhone[partNumber]["available"] = False

		for store in availability:
			if re.match("R\d{3}",store):
				productList = availability[store]
				for item in productList:
					if item in iPhone:
						if productList[item] != "NONE":
							iPhone[item]["available"]=True
							result = result + iPhone[item]["name"] + " available!\n" + iPhone[item]["reserve_url"] + "\n"
							if iPhone[item]["pushed"] == False:
								push = pb.push_link(iPhone[item]["name"] + " available!", iPhone[item]["reserve_url"])
								iPhone[item]["pushed"]=True

		for partNumber in iPhone:
			if iPhone[partNumber]["available"]==False and iPhone[partNumber]["pushed"]==True:
				iPhone[partNumber]["pushed"]=False
				result = result + iPhone[partNumber]["name"] + " gone :(\n"

		if result == "":
			result = "Not available"

		triedTimes=triedTimes+1
		print(time.strftime("%Y-%m-%d %H:%M:%S") + " | " + result)
		time.sleep(10)

except KeyboardInterrupt:
	print("\nBye")