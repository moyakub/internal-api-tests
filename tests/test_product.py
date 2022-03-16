import json
from packages import product
from datetime import datetime
from dateutil import parser
#import custom_packages.product

#test get all products endpoint
def test_get_all_products():

  product_dict = product.get_all_products()
  products_returned = False

  if product_dict["total"]:
    products_returned = True

  assert products_returned == True

#test update a product endpoint
def test_update_a_product():
  new_product_name = "Name-Updated-from-mo-mac"
  
  #Extract date and hour from current datetime object
  current_date_time_utc = datetime.utcnow() 
  current_date_utc = current_date_time_utc.date()
  current_hour_utc = current_date_time_utc.hour
  
  payload =   { 
	
    "product" : {
        "name": new_product_name,
        "description": "Description-Updated"
    }
	
  }
  payload = json.dumps(payload) 
  bold_product_id = "2027011"
  product_dict = product.update_a_product(payload,bold_product_id)
  
  updated_at = product_dict["product"]["updated_at"]

  #convert ISO 8601 string to a datetime object
  updated_at_date_time = parser.parse(updated_at)
  updated_at_date = updated_at_date_time.date()
  updated_at_hour = updated_at_date_time.hour 
  
  #just to debug updated at dates and times. This code is not for test
  #print(f'Current Date: {current_date_utc} updated date: {updated_at_date} Current hour{current_hour_utc} updated hour {updated_at_hour}')

  #if update product endpoint worked fine then current date and hour should be same as updated_at date and hour.
  assert current_date_utc == updated_at_date and current_hour_utc == updated_at_hour








  




