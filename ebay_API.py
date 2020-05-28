import ebaysdk
from ebaysdk.exception import ConnectionError

#connection is mainly to retrieve the Finding API connection keys stored in a yaml file
#from ebaysdk.finding import connection
from ebaysdk.finding import Connection as Finding
import json


#if __name__ == '__main__':
 #   api = Connection(config_file='ebay.yaml', debug=True, siteid="EBAY-US")

api = Finding(domain='svcs.ebay.com',
              appid="NareshKa-ProductD-PRD-1a6d0a603-d5eebc0b", config_file=None)

# Go through the below link to understand the key words concept
#https://linuxconfig.org/introduction-to-ebay-api-with-python-the-finding-api-part-2
# https://developer.ebay.com/devzone/finding/CallRef/index.html

response = api.execute('findItemsByKeywords', {'keywords': 'handbags'})
#response.status_code or response.raise_for_status()
output = response.dict()
output["searchResult"]["item"]
#data_serialization = json.dump(output, open('data.json',"w"), indent = 4)
# sample data to view
#for item in response.reply.searchResult.item:
# print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")

#declaring arrays to store response data
product_list=[]
shipping_type=[]
payment_method=[]
selling_state=[]
product_price=[]

for i in (output["searchResult"]["item"]):
	title = i["title"]
	shippingtype = i["shippingInfo"]["shippingType"]
	sellingstate = i["sellingStatus"]["sellingState"]
	product_list.append(title)
	shipping_type.append(shippingtype)
	selling_state.append(sellingstate)

import pandas as ps
Product_data  = ps.DataFrame({"PRODUCT_NAME":product_list,
                              "SHIPPNG_TYPE":shipping_type,
                             "SELLING_STATUS":selling_state})

Product_data.drop_duplicates

export_csv = Product_data.to_csv(r'A:\Python\Handbags_API.csv', index = None, header = True)




