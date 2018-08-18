import urllib.request as request

ITEM_HTML = "ideaname"
SELL_HTML = "High:"
BUY_HTML = "Low:"
TO_END = "</"

DIVIDER = "---------------------------------------------------------------"
HEADERS = ["Item", "Buy", "Sell"]

# The GET request on merchos.net isn't rate limited
# Scrape x number of requests and print them out nicely formatted

class Item:
	def __init__(self, name, buy_value, sell_value):
		self.name = name
		self.buy_value = buy_value
		self.sell_value = sell_value


def get_ideas(num_times):
	items = []

	for j in range(num_times):
		contents = request.urlopen("https://merchos.net/app/api/getideas.php?f2p=true&p2p=true&margin=0.5&min=1").read()
		contents = str(contents)

		# Request only returns 5 entires
		last_index = 0

		for i in range(5):	
			name_index = contents.find(ITEM_HTML, last_index)
			name = contents[name_index  + 10 : contents.find(TO_END, name_index)]

			# Sell value is the "high"
			sell_index = contents.find(SELL_HTML, name_index)
			sell_value = contents[sell_index + 34 : contents.find(TO_END, sell_index)]

			# Buy value is the "low"
			buy_index = contents.find(BUY_HTML, sell_index)
			buy_value = contents[buy_index + 33 : contents.find(TO_END, buy_index)]

			items.append(Item(name, buy_value, sell_value))

			last_index = buy_index

		longest_name = len(max([item.name for item in items], key=len))
		longest_buy = len(max([item.buy_value for item in items], key=len))
		longest_sell = len(max([item.sell_value for item in items], key=len))

	print("{:>{x}}    {:>{y}}    {:>{z}}".format(HEADERS[0], HEADERS[1], HEADERS[2], 
		x=longest_name, y=longest_buy, z=longest_sell))

	print(DIVIDER)


	for item in items:
		print("{:>{x}}    {:>{y}}    {:>{z}}".format(item.name, item.buy_value, item.sell_value, 
			x=longest_name, y=longest_buy, z=longest_sell))	

get_ideas(3)