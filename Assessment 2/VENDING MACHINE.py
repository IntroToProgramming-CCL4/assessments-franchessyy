#display all the avaialble items on your vending machine

def display_items(items):
    print("+========================= Vending Machine Items ===========================+")
    print("|    Code    |           Item           |   Category   |     Price (AED)    |")
    print("+============+==========================+==============+=====================+")
    for code, item_info in items.items():
        print(f"| {code:<10} | {item_info['name']:<25} | {item_info['category']:<12} | {item_info['price']:>17.2f} |")
    print("+============+==========================+==============+=====================+")

#add the item in yoour cart
def add_to_cart(cart, items, code):
    if code in items:
        cart.append(items[code])
        print(f"Item '{items[code]['name']}' added to cart.")
    #check if your code is correct and proceed to the next step
    else:
        print("Invalid item code. Please try again.")

#display your item with a total price showing on the bottom of the receipt given

def display_cart(cart):
    total_price = sum(item['price'] for item in cart)
    print("+============================== Cart ==============================+")
    print("|    Item     |      Category       |      Price (AED)   |")
    print("+============+=================+==================+")
    for item in cart:
        print(f"| {item['name']:<10} | {item['category']:<15} | {item['price']:>15.2f} |")
    print("+===============================================================+")
    print(f"|                         Total:               | {total_price:>15.2f} |")
    print("+===============================================================+")
    return total_price

def purchase(items, cart):
    while True:
        code = input("Enter the code of the item you want (or 'Q' to quit): ")
        if code.lower() == 'q':
            break
            
        if code in items:
            item_info = items[code]
            name = item_info['name']
            price = item_info['price']
            category = item_info['category']
            
            print(f"You selected: {name} ({category}) - AED{price:.2f}")
            add_to_cart(cart, items, code)
        else:
            print("Invalid selection. Please try again.")
#input your cash 
    if cart:
        print("\nItems in your cart:")
        total_cost = display_cart(cart)
        cash = float(input("Insert cash: "))
        if cash >= total_cost:
            change = cash - total_cost
            print(f"Thank you for purchasing! ^^ Your change is AED {change:.2f}")
       
        #make sure you have sufficient funds to proceed purchasing the items
        else:
            print("Insufficient funds, Please Insert more money.")
    else:
        print("Oops! Your cart is empty, try again.")

#display welcome message
        
def welcome_message(): 
     print("Please select item below to purchase!\n")
print("Hello! welcome to my vending machine.")

#shows all the items
items = {

    'A01': {'name': 'Blackforest', 'price': 5.00, 'category': 'Cakes'},
    'A02': {'name': 'Strawberry', 'price': 5.00, 'category': 'Cakes'},
    'A03': {'name': 'Redvelvet', 'price': 5.00, 'category': 'Cakes'},
    'A04': {'name': 'Caramel', 'price': 5.00, 'category': 'Cakes'},
    'A05': {'name': 'Chocolate', 'price': 5.00, 'category': 'Cakes'},
    'B01': {'name': 'Brown Sugar', 'price': 10.00, 'category': 'Milktea'},
    'B02': {'name': 'Okinawa', 'price': 10.00, 'category': 'Milktea'},
    'B03': {'name': 'Oreo', 'price': 10.00, 'category': 'Milktea'},
    'B04': {'name': 'Cheesecake', 'price': 10.00, 'category': 'Milktea'},
    'B05': {'name': 'Matcha', 'price': 10.00, 'category': 'Milktea'},
    'C01': {'name': 'Mini Pau Chocolate', 'price': 4.00, 'category': 'Bread'},
    'C02': {'name': 'Butter Croissant', 'price': 3.00, 'category': 'Bread'},
    'C03': {'name': 'Toasted Bread', 'price': 3.00, 'category': 'Bread'},
    'D01': {'name': 'Water', 'price': 1.00, 'category': 'Drinks'},
    'D02': {'name': 'Sprite', 'price': 2.00, 'category': 'Drinks'},
    'D03': {'name': 'Coca-Cola', 'price': 2.00, 'category': 'Drinks'},
}
# your selected item informataion or details
cart = []
#displaying the welcome_message and display_items
welcome_message()
display_items(items)

purchase(items, cart)
