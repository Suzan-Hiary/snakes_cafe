from textwrap import dedent


print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears


**************************************

** What would you like to order? **

**************************************
 """)





menu  = {
  'wings': 0,
  'cookies': 0,
  'spring Rolls': 0,
  'salmon': 0,
  'steak': 0,
  'meat Tornado': 0,
  'a Literal Garden': 0,
  'ice Cream': 0,
  'cake': 0,
  'pie': 0,
  'coffee': 0,
  'tea': 0,
  'unicorn Tears': 0,
}
# print(menu['pie'])

def order() :
     order = input().lower() 
     if order == "quit" :
       print('thanks for your visit')
       exit()
     elif order in menu.keys() :
          menu[order] +=1
          print(f"** {menu[order] } order of {order.capitalize()} have been added to your meal **")
    
          while order !='quit':
            
            order = input()
            if order == "quit" :
                print('thanks for your visit')
                exit()
            else :
              
              
              menu[order] +=1
              print(f"** {menu[order] } order of {order.capitalize()} have been added to your meal **")

     else:
        print('your order is not exisit please order from the menu')
  
order() 