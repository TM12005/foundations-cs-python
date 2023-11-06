# additem
cart = []

# total = 0
items =[["tomato",1],["potato",2],["chocolate",3],["soap",0.5]]

def addItem():
    # items =[["tomato",1],["potato",2],["chocolate",3],["soap",0.5]]
    # ask the user to enter a item name
    item_name = input('Enter an item name: ')

    # loop over the list of fruits
    for i in items:
        # cart = []
        # check if the fruit name matches the user input
        if i[0] == item_name:
            # append the fruit name and price to the found_fruit list
            cart.append(i)
            # break out of the loop
            break
    else:
            print("item not found")
    print(cart)        
    return cart
    

#check cart (check total)
def checkTotal():
    total = 0
    for i in cart:
        total = total + i[1]
    # print the sum
    print("The total of your bill is", total)
    return total

    
# Add Coupon
def addCoupon():
   total = checkTotal()
   value = float(input("Please enter the value of the coupon:"))
   valueAfterCoupon = total - value
   print("Coupon Added")
   return valueAfterCoupon

# Check Out

def checkout():
    coupon = addCoupon()
    counted_names = []
# Loop through the list of items
    for i in range(len(cart)):
        # Get the name of the current item
        name = cart[i][0]
        # Check if the name has already been counted
        if name not in counted_names:
            # Initialize the count as zero
            count = 0
            # Loop through the list of items
            for j in range(len(cart)):
                # If the name matches, increment the count by one
                if cart[j][0] == name:
                    count += 1
            # Print the name and count
            print(f"{name}: {count}")
            # Add the name to the list of counted names
            counted_names.append(name)
    total = checkTotal()
    print("The total is ", total)
    print("Coupon discount ammount is", coupon)
    print("Total ammount after the discount is ", total - coupon)


#AddItem
def newOrder():
  choice=-99 # dummy value1
  while choice !=4:
    print("What do you want to do")
    print("1. to add an item")
    print("2. to check total")
    print("3. to add a coupon")
    print("4. to checkout")

    choice=int(input())

    if choice==1:
      addItem()
    elif choice ==2:
      checkTotal()
    elif choice ==3:
      addCoupon()
    elif choice ==4:
      checkout()
    else:
      print("ivalid input")
      







# Menus
def mainMenu():
    
  choice=-99 # dummy value
  while choice !=2:
    print("Enter")
    print("1. to start a new order")
    print("2. to close the program")
    
    choice=int(input())
    
    if choice==1:
      print("starting a new order...")
      newOrder()
    elif choice ==2:
      print("bye bye")
    else:
      print("invalid input")
    

mainMenu()