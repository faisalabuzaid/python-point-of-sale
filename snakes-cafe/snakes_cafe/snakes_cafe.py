menu = {
  'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
  'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
  'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
  'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
}

print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""", "\n")



for category in menu:
    print(category)
    print("-" * len(category))
    for item in menu[category]:
        print(item)
    print('\n')

print("""***********************************
** What would you like to order? **
***********************************""", "\n")

order = input("> ")

while order != 'quit':

  for key in menu.keys():

    if order in menu[key].keys():

      menu[key][order]+= 1

      if menu[key][order] == 1:
        print(f'** {menu[key][order]} order of {order} has been added to your meal **')
        break

      else:
        print(f'** {menu[key][order]} orders of {order} have been added to your meal **')
        break
  
  else:
    print('** Sorry this item is unavailable, please order item from our menu **')

  order = input("> ")