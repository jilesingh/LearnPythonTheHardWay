# Store information about a Pizza 

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'] 
}

# Summarise trhe order
print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
                      