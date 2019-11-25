# DO NOT TOUCH ============================================
from random import randint
pizzas = [
   'Pizza - Pepperoni',
   'Pizza - Cheese',
   'Pizza - Sausage',
   'Pizza - Supreme',
   'Pizza - Veggie'
   ]
selected_pizza = pizzas[randint(0, 5)]
# DO NOT TOUCH ============================================

pizza_type = selected_pizza[8:]  # fill in blank 

print(pizza_type)