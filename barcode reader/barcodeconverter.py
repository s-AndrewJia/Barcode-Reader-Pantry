import requests

def convert_barcode(barcode):	
	# check for improper barcodes
	item = requests.get(f"https://api.upcitemdb.com/prod/trial/lookup?upc={barcode}")

	# if item.json()['code'] == "OK":
	# 	pass
	try:
		if len(item.json()['items']) > 0:
			response = item.json()['items'][0]['title']
			return response
		else:
			return "Invalid UPC. Barcode number detected: " + barcode
	except:
		return "Invalid UPC. Barcode number detected: " + barcode

# convert_barcode("075020087607")
# convert_barcode("064900000348")