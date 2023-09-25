"""
Write a function called linear_search_product taht takes the list of products and a target product name as input
The function should perform a linear search to  find the target product in  the list and return a list of indices of all occurrences of the product if 
fount or an empty list if the product is not found.
"""


def linearsearchproduct(productList, targerProduct):
  indices = []
  for index, product in enumerate(productList):
    if (product == targerProduct):
      indices.append(index)
  return indices


products = ["shoes", "boots", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = "bata"
result = linearsearchproduct(products, target)
print(result)
