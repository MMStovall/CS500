#!/usr/bin/env python3

class ItemToPurchase:

    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
        
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
   
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = [] 

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        
    def remove_item(self,name):
        for item in self.cart_items: 
            if item.item_name == name:
                self.cart_items.remove(item)
            else:
                print("\nItem not found in cart. Nothing to remove.")            
        
    
    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
            return  # Successfully modified
        print("Item not found in cart. Nothing modified.")  # Only if no match is found
    
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
            
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")
            
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()





def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Modify an Item\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    command = ""
    while command != "q":
        print(menu)
        command = input("Choose an option:\n").lower()

        if command == "a":
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = float(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(item)
            

        elif command == "r":
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif command == "c":
            modified_item = ItemToPurchase()
            modified_item.item_name = input("Enter the item name:\n")
            user_response= input("what do you want to modify (p = price, q = quantity, d = desciption, z = price and quantity, l= price and description, j=quantity and description, a = all)\n").lower()
            
            if user_response == 'p': # change price only 
                modified_item.item_price = float(input("Enter the new item price:\n"))
                cart.modify_item(modified_item)
            elif user_response == 'q': # change quantity only
                modified_item.item_quantity = int(input("Enter the new quantity:\n"))
                cart.modify_item(modified_item)
            elif user_response == 'd': # change desciption only 
                modified_item.item_description = input("Enter the new item description:\n")
                cart.modify_item(modified_item)
            elif user_response == 'a': # change all
                modified_item.item_price = float(input("Enter the new price:\n"))
                modified_item.item_description = input("Enter the new description:\n")
                modified_item.item_quantity = int(input("Enter the new quantity:\n"))
                cart.modify_item(modified_item)
            elif user_response == 'z': # change price and quantity
               modified_item.item_price = float(input("Enter the new price:\n"))
               modified_item.item_quantity = int(input("Enter the new quantity:\n"))
               cart.modify_item(modified_item)
            elif user_reponse == 'l':  # change price and description 
                modified_item.item_price = float(input("Enter the new price:\n"))
                modified_item.item_description = int(input("Enter the new description:\n"))
                cart.modify_item(modified_item)
            elif user_response == 'j': # change quantity and description
                modified_item.item_quantity = int(input("Enter the new quantity:\n"))
                modified_item.item_description = input("Enter the new description:\n")
                cart.modify_item(modified_item)
            else:
                print("not a correct response returning you to the main menu")
            
           
        elif command == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif command == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif command == "q":
            break

        else:
            print("Invalid option. Please try again.")
 
 
cart = ShoppingCart()
cart.customer_name = input("Enter customer's name:\n")
cart.current_date = input("Enter today's date:\n")
print_menu(cart)



   