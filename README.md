The data for this code challenge contains 3 million instacart orders, which you can have access at https://www.instacart.com/datasets/grocery-shopping-2017.

In this code challenge, I managed to combine and summarise two datasets: `order_product.csv` which contains the 3 million instacart orders, and `products.csv` which contains all the products information.

The `order_product.csv` has the below format.
```
order_id,product_id,add_to_cart_order,reordered
2,33120,1,1
2,28985,2,1
2,9327,3,0
2,45918,4,1
3,17668,1,1
3,46667,2,1
3,17461,4,1
3,32665,3,1
4,46842,1,0
```
The `products.csv` has the following format.
```
product_id,product_name,aisle_id,department_id
9327,Garlic Powder,104,13
17461,Air Chilled Organic Boneless Skinless Chicken Breasts,35,12
17668,Unsweetened Chocolate Almond Breeze Almond Milk,91,16
28985,Michigan Organic Kale,83,4
32665,Organic Ezekiel 49 Bread Cinnamon Raisin,112,3
33120,Organic Egg Whites,86,16
45918,Coconut Butter,19,13
46667,Organic Ginger Root,83,4
46842,Plain Pre-Sliced Bagels,93,3
```

The output/summarised data should contain the department_id, number_of_orders from the department, number_of_first_orders from the department, and the ratio of number_of_orders/number_of_first_orders. The following example is shown.
```
department_id,number_of_orders,number_of_first_orders,percentage
3,2,1,0.50
4,2,0,0.00
12,1,0,0.00
13,2,1,0.50
16,2,0,0.00
```
In this code challenge, I didn't use any external libraries in python like pandas, numpy et al. Instead, I only take advantage of the built-in python libraries as instructed. I was successful to test my codes **on the entire 3 million length dataset**.
