from packages import product
#import custom_packages.product

#test get all products endpoint
def test_get_all_products():
  product_dict = product.get_all_products()
  assert product_dict["total"] == 18
  




