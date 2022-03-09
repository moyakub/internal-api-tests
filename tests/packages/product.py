import requests
import json

from . import config_shop_environment as cse


def get_all_products():
  r = requests.get(cse.url,headers=cse.headers)
  product_dict = r.json()
  return product_dict


  