class config(object):
	pushbullet_access_token = "{your token here}"

	#Hong Kong iPhone reserve link, change to your country if you need
	availability_json = "https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability.json"

	#change/add your iPhone reserve link here, format: {"name":"your iPhone", "reserve_url":"the url"},
	iPhoneList = [
		{
			"name" : "iPhone 6s pink 64GB",
			"reserve_url" : "https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability?channel=1&appleCare=N&iPP=N&partNumber=MKQR2ZP/A&returnURL=http%3A%2F%2Fwww.apple.com%2Fhk-zh%2Fshop%2Fbuy-iphone%2Fiphone6s%2F4.7-%E5%90%8B%E8%9E%A2%E5%B9%95-64gb-%E7%8E%AB%E7%91%B0%E9%87%91%E8%89%B2"
		},
		{
			"name" : "iPhone 6s Plus pink 64GB",
			"reserve_url" : "https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability?channel=1&appleCare=N&iPP=N&partNumber=MKU92ZP/A&returnURL=http%3A%2F%2Fwww.apple.com%2Fhk-zh%2Fshop%2Fbuy-iphone%2Fiphone6s%2F5.5-%E5%90%8B%E8%9E%A2%E5%B9%95-64gb-%E7%8E%AB%E7%91%B0%E9%87%91%E8%89%B2"
		}
	]
