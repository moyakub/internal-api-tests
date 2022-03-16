import requests
import json

from . import config_shop_environment as cse


def get_all_products():
  r = requests.get(cse.get_products_url,headers=cse.headers)
  product_dict = r.json()
  return product_dict



def update_a_product(payload,bold_product_id):
  url = cse.update_a_product_url + bold_product_id
  r = requests.put(url,headers=cse.headers, data=payload)
  product_dict = r.json()
  return product_dict  



  