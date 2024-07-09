# import projectfun 
from projectfun import *
while True :
    
    # Print The Greeting's
    
    greeting()
    print()
    
    # Getting the Type of User
    
    user_type = input("Please Specify The User Type! [Type : a for admin or c for customer] : ",)
    user_type = user_type.lower()
        
    # Admin/Master's Page
    
    if user_type == "a":
        
        # Entering Into The Page For The Varification! 
        
        login = log_in()
        
        # If Login successfully With Correct Login Credentials! 
        
        if login == True:
            
            # Admin System
            
            while True :
                
                # Adding of New Menu Items!
                
                add_menu = input("Do You Want to Add a Item in The Menu! [Type : y for YES or n for NO] : ",)
                add_menu = add_menu.lower()
                                
                if add_menu == "y":
                    while add_menu == "y":
                        add_success = add_menu_item()
                        
                        if add_success == True :
                            print("Added Successfully!!\n")
                            add_menu = input("Do You Want to Add More Item's in The Menu! [Type : y for YES or n for NO] : ",)
                            add_menu = add_menu.lower()
                            
                            if add_menu == "y":
                                continue
                            
                            elif add_menu == "n":
                                break
                            
                            else :    
                                print("Please Write a Valid Input From Next Time!\n")
                        
                        else :
                            pass
                        
                elif add_menu == "n":
                    pass
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                                    
                
                # Display The Sales Details Done Till Now!
                
                see_history = input("Do You Want to See The Order History! [Type : y for YES or n for NO] : ",)
                see_history = see_history.lower()
                
                if see_history == "y":
                    order_history()
                
                elif see_history == "n":
                    pass    
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                
                # Asking Admin Whether He/She Want to Logout From The Admin/Master Page!
                
                ask_exit = input("Do You Want To Logout and Go To The Home Page! [Type : y for YES or n for NO] : ",)
                ask_exit = ask_exit.lower()
                
                if ask_exit == "y":
                    break
                
                elif ask_exit == "n":
                    continue    
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                    continue
            
            # Print After Loging Out From The Admin/Master Page!
            
            print()
            print("Successfully LOGOUT From The Admin/Master Page!\n")
            print("Going To The Main/Home Page!")
            print("Please Wait!\n")
                
    # Customer Page For Order
    
    elif user_type == "c":
        customer_name = input("Please Enter The Customer Name Here! : ",)
        
        # Printing The Menu 
        
        print()
        print("Please Have a Look in The Today's Menu!\n")
        print("       ** Menu **       ")
        menu_display()
        
        # Customer Page
        
        while True :
            
            # Take Order From The Customer! 
            
            ask_order = input("Would You Like to Place Your Order! [Type : y for YES or n for NO] : ",)
            ask_order = ask_order.lower()
            
            if ask_order == "y":
                while ask_order == "y":
                    print()
                    print("*** TAKING ORDER ***\n")
                    order_item_id = input("Please Enter The Item Id Here! : ",)
                    


                    id_check = check_item_details(order_item_id)
                    
                    if id_check == (True , False) :
                        
                        # Printing The Item Information 
                        
                        menu_info = menu_data()
                        item_info = menu_info[order_item_id]
                        print()
                        print("." * 64)
                        print(":  Item Name  :  " , item_info[0] , " "*(15 - len(item_info[0])) , "::  Item Price  :  " 
                                 , str(item_info[1]) , " "*(6 - len(str(item_info[1]))) , ":"  )
                        print("." * 64,"\n")
                        
                        try :
                            item_qty = int(input("Please Enter The Quantity Here! {Hint : Please Enter The Quantity in Integer!} : ",))
                        
                        except :
                            print("Please Enter a Valid Input!\n")
                            continue
                        
                        else : 
                            # Adding the Item To The Cart!
                            
                            add_cart_success = take_order(order_item_id , item_qty)
                            
                            if add_cart_success == True :
                                print("Successfully Added To The Cart!\n")
                                ask_order = input("Would You Like to Order Something Else! [Type : y for YES or n for NO] : ",)
                                ask_order = ask_order.lower()
                                continue
                            
                            else :
                                continue
                    
                    else :
                        print("Please Enter a Valid ITEM ID!\n")
                        continue
            
            elif ask_order == "n":
                print("Please Take Your Time, See The Menu, And Then Order!!\n")
                continue
            
            else :
                print("Please Write a Valid Input!\n")
                continue
            
            # Asking The Customer, If He/She Want's To Remove Some Item From The Cart!
            
            ask_remove = input("Do You Want To Remove a Item From The Cart! [Type : y for YES or n for NO] : ",)
            ask_remove = ask_remove.lower()
            
            if ask_remove == "y":
                while ask_remove == "y":
                    
                    # Printing The Current Item's Present In The Cart! 
                    
                    cart_item = retrieve_data("cart.csv")
                    print("Current Item In The Cart!")
                    for item in cart_item :
                        print(item)
                        
                    remove_item_id = input("Please Enter The Item Id Here! : ",)
                    remove_order_success = item_remove_order(remove_item_id)
                    
                    if remove_order_success == True :
                        print("Successfully Removed From The Cart!\n")
                        ask_remove = input("Do You Want To Remove more Item From The Cart! [Type : y for YES or n for NO] : ",)
                        ask_remove = ask_remove.lower()
                        
                        if ask_remove == "y":
                            continue
                        
                        elif ask_remove == "n": 
                            break
                        
                        else :
                            print("Please Enter A Valid Input!\n")
                            continue
                    else :
                        print("Please Write a Valid Input From Next Time!\n")
                        break
            
            elif ask_remove == "n" :
                pass
            
            else :
                print("Please Write a Valid Input From Next Time!\n")
                pass
            
            # Asking The Customer, To Confirm The Order!
            
            confirm_order = input("Please Confirm Your Order For The Billing [Type : y for YES or n for NO] : ",)
            confirm_order = confirm_order.lower()
            
            if confirm_order == "y":
                final_order_list = retrieve_data("cart.csv")
                for item_list in final_order_list :
                    item_list[2] = float(item_list[2]) 
                    item_list[3] = int(item_list[3]) 
                
                # Transfer The Item Info. From The Cart To The Order History  
                
                store_order_history = cart_to_order(customer_name)
                
                # Generate and Print The Bill!
                
                bill_success = generate_bill(final_order_list)
                
                # Empty The Cart!
                
                cart_empty_success = empty_cart()
                
                if store_order_history == True and bill_success == True and cart_empty_success == True :
                    print()
                    print("Thanks For Choosing Us! Hope You Will Come Back!\n")
                    break
                
                else :
                    print("An ERROR Occured!")
                    print("Sorry, For The Inconvenience!")
                    print("Please wait\n")
                    continue
            
            else :
                cart_empty_success = empty_cart()
                print("Your Order is Cancelled!")
                print("Sorry, For The Inconvenience!\n")
                break
    
    # In Case If The User Type Is Wrong!
    
    else :
        print()
        print("Please Enter A Valid Input!!\n")
        continue                        
                                            