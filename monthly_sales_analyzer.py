# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(sales_data, product_a):
    total_sales_product_a= 0
    for product in sales_data:
        total_sales_product_a += product[product_a]
    return total_sales_product_a
total_sales_by_product(sales_data,"product_a")
sales= total_sales_by_product(sales_data,"product_a")
print(f"Las ventas totales de producto A fueron: {sales}")
    
#   """Calculates the total sales of a specific product in 30 days."""

    


def average_daily_sales(sales_data, product_a):
    media_sales = total_sales_by_product(sales_data, product_a) / len(sales_data)
    return media_sales

average_daily_sales (sales_data,"product_a")
media= average_daily_sales (sales_data,"product_a")
print(f"La media total de ventas del producto A fue de: {media}")




#    """Calculates the average daily sales of a specific product."""



def best_selling_day(sales_data):
  max_sales_by_day= 0
  best_day=None
  for day_sales in sales_data:
    daily_sales= day_sales["product_a"] + day_sales["product_b"] + day_sales["product_c"]
    if daily_sales > max_sales_by_day:
      max_sales_by_day = daily_sales
      best_day = day_sales["day"]
  return best_day
    

best_selling_day(sales_data)
best_day=best_selling_day(sales_data)
print(f"El mejor dia de venta fue el dia numero {best_day}")

     


#    """Finds the day with the highest total sales."""
 



def suma_sales(product_a,product_b,product_c,sales_data):
  daily_sales = 0
  for day in sales_data:
    daily_sales += day["product_a"] + day["product_b"] + day["product_c"]
  return daily_sales
suma_sales ("product_a","product_b","product_c",sales_data)
total_sales= suma_sales("product_a","product_b","product_c",sales_data)
print(f"Las suma total de todas las ventas fue de {total_sales}")
 

def media_sales(sales_data):
      media = suma_sales ("product_a","product_b","product_c",sales_data) / len(sales_data)
      return media
media_sales(sales_data)
media_total= media_sales(sales_data)
print(f"La media total de ventas por dia fue de {media_total}")



def days_above_threshold(sales_data):
  days_yes=[]
  for day in sales_data:
    day_sales= day["product_a"] + day["product_b"] + day["product_c"]
    if day_sales >= media_sales(sales_data):
      days_yes.append(day_sales)

  return len(days_yes)

days_above_threshold(sales_data)
days= days_above_threshold(sales_data)
print(f"La cantidad de dias que superaron la media de venta fue: {days}")








#    """Counts how many days the sales of a product exceeded a given threshold."""

def top_product(sales_data):
  
  def sales_tot_product_b (sales_data, product_b):
    total_sales_b = 0
    for product in sales_data:
      total_sales_b += product[product_b]
    return total_sales_b
  sales_tot_product_b(sales_data,"product_b")

  def sales_tot_product_c(sales_data, product_c):
    total_sales_c = 0
    for product in sales_data:
      total_sales_c += product[product_c]
    return total_sales_c
  sales_tot_product_c(sales_data,"product_c")

  product__a = total_sales_by_product(sales_data,"product_a")
  product__b = sales_tot_product_b(sales_data,"product_b")
  product__c = sales_tot_product_c(sales_data,"product_c")

  if product__a > product__b and product__a > product__c:
    return "product_a"

  elif product__b > product__a and product__b > product__c:
    return "product_b"
  else:
    return "product_c"

best_product=top_product(sales_data)

print(f"El producto mas vendido fue: {best_product}")















#    """Determines which product had the highest total sales in 30 days."""
  



# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
