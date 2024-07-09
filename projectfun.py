# **Funtion to print Greeting!**

# In[7]:

def greeting(): 
    """
    This Function is use to print the greeting at the start of the program.

    Arguments:
        No Argument Taken   

    Returns:
        print greeting message.

    """
    print(r"                                                                                            _")
    print(r" __                __                           _______        _______                     | |")
    print(r" \ \              / /                          |__   __|      | ______|                    | |")
    print(r"  \ \     __     / /                              | |         | |                          | |")
    print(r"   \ \   /__\   / /  __       _  _   _   _   _    | |   _     | |          _     __   __   |_|")
    print(r"    \ \_//  \\_/ /  |_   |   |  | | | \_/ | |_    | |  | |    | |_____    /_\   |_   |_     _ ")
    print(r"     \__/    \__/   |__  |_  |_ |_| |     | |_    |_|  |_|    |_______|  /   \  |    |__   |_|")

    #LOGIN FUNCTION
import csv
from getpass import getpass

# **Function to Log-in into the Admin system **
def log_in(attempts=3):
    """
    This is a login Function for the Admin, It takes the Admin Name and Admin Password and
    Check the input from the Admin_info.csv File(Data Base).
    The password is taken using getpass method.
    

    Argumentss:
        Attempts : Number of attempts provided to login.
                   Default value is 3.
        
    Inputs:
        Take the Admin Name and Password as the input.

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.
        But after first try function returns None value (Thats why to check use login_value). 

    Raises:
        UnknownError: Raises an exception when a error is found.

    """
    
    user_list = user_data()
    
    for attempt in range(attempts, 0, -1):
        print("Please Enter the following details!\n")
        user_name = input("User Name: ")
        # password = getpass("Password: ")
        password=input("userpassword")

        print()
        
        if user_name in user_list and password == user_list[user_name]:
            print("~~~ Log-in successfully!! ~~~\n")
            print("Welcome", user_name, "!")
            return True
        else:
            print(f"This is not a valid Username/Password. You have {attempt-1} attempts left.\n")
            if attempt == 1:
                print("This was your last attempt! Please try later!\n")
                return False
            
# **Get The User Data in the form of dictionary**            

def user_data():
    """
    This Function is use to retrieve the data from the file Admin_info.csv,
    into the function using retrieve_data function.
    Then convert it into a dictonary with Key as admin name and Value as the password.

    Arguments:
        No Argument Taken   

    Returns:
        returns a dictonary with Key as admin name and Value as the password.

    Raises:
        UnknownError: Raises an exception when a error is found.
        Admin_info.csv file not found!
    """
    user_dictionary = {}
    try:
        with open("C:\\Users\\LENOVO\\Desktop\\python froject\\Admin_info.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if there is one
            for row in reader:
                user_name = row[1]
                password = row[2]
                user_dictionary[user_name] = password 
    except FileNotFoundError:
        print("Admin_info.csv file not found!")
    
    return user_dictionary
# ////////////////////


import csv

def add_menu_item():
    """
    This Function is use to Add New Menu Items into the File cafe_menu.txt,
    By Using the data_entry function.
    To verify that the Item_Id provided does not exists in the menu to avoid Duplication of the Item_Id,
    check_item_details function is used (as Item_Id is a unique Key/Primary Key).
    After updating the quantity it stores the order back into the cafe_menu.csv File.

    Arguments:
        No Argument Taken.
    
    Inputs:
        Take the Unique Item Id and Item Name as an input from the user.

    Returns:
       returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    old_menu = retrieve_data("cafe_menu.csv")
    print("       *** The Current Menu Details ***")
    menu_display()
    print("Please Enter the Following Details!\n")
    item_id = input("Unique Item ID: ")
    item_name = input("Item Name: ")
    try:
        item_price = float(input("Item Price: "))
    except ValueError:
        print("\nPlease Enter a valid Item Price!\n")
        return False
    
    validity = check_item_details(item_id, item_name)
    if validity == (False, False) and item_name != "":
        item_detail = [item_id, item_name, f"{item_price:.2f}"]
        old_menu.append(item_detail)
        data_entry("cafe_menu.csv", old_menu)
        return True
    else:
        print("\nPlease Enter valid Inputs!")
        print("ERROR: Duplication of Input was Found!\n")
        return False
    


          
# **Funtion to get data from the file into a list!!**
def retrieve_data(path):
    """
    This Function is use to get the data from the File, 
    which contains the data in comma seprated form and
    convert it into a nested list and return that list.

    Arguments:
        path : The path of the .csv file to read in string format.

    Returns:
        Returns a nested list, in which data in each line is converted into a list.
        In the case of an error, it returns None.

    Raises:
        FileNotFoundError: Raises an exception when the file is not found in the specified path.
    """
    try:
        with open(path, mode='r') as file:
            reader = csv.reader(file)
            return [row for row in reader if row]
    except FileNotFoundError:
        print("Please make sure that the path you have provided is correct!")
        return []
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return []

# **Funtion to Display the menu!!**    

def menu_display():
    """
    This Function is use to retrieve the data from the file cafe_menu.csv,
    into the function using retrieve_data function.
    Then, Print the current Menu Page.

    Arguments:
        No Argument Taken   

    Returns:
        returns the Menu in a Tabular form.

    Raises:
        Cafe_menu.csv not found!.
        UnknownError: Raises an exception when a error is found.
    """
    try:
        print("\n" + "." * 46)
        print(": Item I.D :        Item        :   Price    :")
        menu_list = retrieve_data("C:\\Users\\LENOVO\\Desktop\\python froject\\cafe_menu.csv")
        for item in menu_list:
            print("." * 46)
            print(f": {item[0]:<9} : {item[1]:<15} : {item[2]:>8} :")
        print("." * 46, "\n")
    except Exception as e:
        print("cafe_menu.csv not found!")
        print("ERROR:", e, "\n")
       


# **Get The Menu Data in the form of dictionary**

def menu_data():
    """
    This Function is use to retrieve the data from the file cafe_menu.txt,
    into the function using retrieve_data function.
    Then, convert it into a dictonary with Key as Item_Id and Value as a tuple of name and price.

    Arguments:
        No Argument Taken   

    Returns:
        returns a dictonary with Key as Item_Id and Value as a tuple of name and price.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        menu_dictionary = {}
        menu_list = retrieve_data("C:\\Users\\LENOVO\\Desktop\\python froject\\cafe_menu.csv")
        for item in menu_list:
            item_id = item[0]
            item_name = item[1]
            item_price = float(item[2])
            menu_dictionary[item_id] = (item_name, item_price)
        return menu_dictionary
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return {}

    
# check_item_details(1818)     

def check_item_details(item_id, item_name=None):
    """
    This Function is use to check whether the Item_Id and Item_Name
    provided matches with that in the DataBase(cafe_menu.csv) File.
    And Returns a tuple with 2 boolean values.
    For Example : if item_id is correct and item_name is wrong
    output      : (True,False)

    Arguments:
        item_id   : The Item ID is written in string format.
        item_name : The Item Name is written in string format and it is not necessary to include(optional argument).
                    Default Value is None.

    Returns:
        Returns a tuple with 2 boolean values.
        For Example : if item_id is correct and item_name is wrong
        output      : (True,False)

    Raises:
        UnknownError: Raises an exception when a error is found.
    """ 
    try:
        menu = menu_data()
        for value in menu:
            if value == item_id:
                if menu[value][0] == item_name:
                    return True, True
                else:
                    return True, False
            elif value != item_id:
                if menu[value][0] == item_name:
                    return False, True                        
            else:
                pass
        return False, False
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return False, False


# **Funtion to enter data in the file from a list!!**

def data_entry(path, data):
    """
    This Function is use to enter the data from the Nested List,
    Into the file in a comma seprated form.
    Each line in the file contains the data of a list(element).

    Arguments:
        path  : The path of the .txt file is to write in string format.
        entry : The Nested List(Which means a List inside a List).

    Returns:
        returns True, if executed succesfully.
        In the case of an error it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        with open(path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except Exception as e:
        print("An Error Occurred while writing to file!")
        print("ERROR:", e, "\n")

# ////////////////////////////////////////////////
import csv
# **Function To Store Order in Cart.csv ; Cart.csv : A Temporary txt file to have the order details**
def cart(order_list):
    """
    This Function is use to enter(append) the data from the Nested List,
    into the file cart.csv in a comma seperated form.
    Each line in the file contains the data of a list(element).

    Arguments:
        order_list : The Nested List.(A List Inside A List)   

    Returns:
        returns nothing(None).

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        with open("C:\\Users\\LENOVO\\Desktop\\python froject\\cart.csv", mode="a", newline='', encoding='utf-8') as file_cart:
            writer = csv.writer(file_cart)
            writer.writerow(order_list)
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")

def take_order(item_id, quantity=1):
    """
    This Function is use to Take Order with the Item_Id and quantity as the inputs.
    And uses check_item_details function to check with that in the DataBase(cafe_menu.csv) File.
    And uses cart function to add the item into the cart.csv File.

    Arguments:
        item_id   : The Item ID is written in string format.
        Quentity  : The Item Quantity is written in integer format.( Default value is 1)

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        check = check_item_details(item_id)
        if check == (True, False):
            order_list = [item_id]
            menu_dict = menu_data()
            order_list.append(menu_dict[item_id][0])
            order_list.append(str(menu_dict[item_id][1]))
            order_list.append(str(quantity))
            cart(order_list)
            return True
        else:
            return False
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e)
        print("Please Enter a valid Input!\n")
        return False

# **Function to Generate a Bill**
def generate_bill(order_list):
    """
    This Function is use to generate the bill from the data in the order_list.
    Then generate the bill and also the total amount to be payed.

    Arguments:
        order_list : The Nested List.(A List Inside A List)
    
    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    print("\n\n                                            ***  BILL  ***                                             ")
    print("." * 106)
    print(":    S.No    :    ITEM ID    :       ITEM NAME       :     PRICE     :    QUANTITY   :    TOTAL AMOUNT   :")
    s_no = 1
    total_amount = 0.0
    try:
        for item in order_list:
            total_price = float(item[2]) * float(item[3])
            print("." * 106)
            print(f":    {s_no:<7} :    {item[0]:<9} :    {item[1]:<16} :    {item[2]:<8} :      {item[3]:<8} :     {total_price:<11} :")
            s_no += 1
            total_amount += total_price
        print("." * 106)
        print("\n\n" + "." * 55)
        print(f":    TOTAL AMOUNT TO PAY IN RUPEES    :    {total_amount:<8} :")
        print("." * 55)
        return True
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return False
    
# **Function to Transfer the Order Information into the order_history.txt File**    

def cart_to_order(customer_name):
    """
    This Function is use to enter the data from the cart.csv File into order_history.csv File,
    Data is stored in the order_history.csv file in a comma seprated form with 
    additional customer name added at the last of each line.

    Arguments:
        customer_name : The Name of the Customer is written in the string format.

    Returns:
        returns True, if it is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception, when a error is found.
    """
    try:
        final_order = retrieve_data("C:\\Users\\LENOVO\\Desktop\\python froject\\cart.csv")
        with open("order_history.csv", mode="a", newline='', encoding='utf-8') as file_open:
            writer = csv.writer(file_open)
            for list_data in final_order:
                list_data.append(customer_name)
                writer.writerow(list_data)
        return True
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return False
# **Function to Empty the Current Item in the Cart.csv File**    

def empty_cart():
    """
    This Function is used to empty the data from the cart.csv File.

    Arguments:
        No Argument Taken.

    Returns:
        returns True, if it is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        with open("C:\\Users\\LENOVO\\Desktop\\python froject\\cart.csv", mode="w", encoding='utf-8') as file_open:
            file_open.write("")
        return True
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return False


def item_remove_order(item_id):
    """
    This Function is used to remove an item from the ordered information present in the cart.csv File.
    To verify that the item_id provided exists in the menu, check_item_details funcion is used.
    After checking, the item's information is removed from the cart.csv File.
    Then, the Function update the cart.csv File.

    Arguments:
        item_id : The Item ID is written in the string format.

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        check = check_item_details(item_id)
        if check == (True, False):
            order_list = retrieve_data("C:\\Users\\LENOVO\\Desktop\\python froject\\cart.csv")
            new_order = [value for value in order_list if value[0] != item_id]
            data_entry("cart.csv", new_order)
            return True
        else:
            print("Entered Item ID was wrong. Please Enter A Valid ID!\n")
            return False
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return False
# **Function to Get the Order History and to Display it from order_history.txt File!**    

def order_history():
    """
    This Function is use to retrieve the data from the File order_history.txt,
    into the Function using retrieve_data Function.
    Then, print the Customer Order History with the total sale done till now.

    Arguments:
        No Argument Taken   

    Returns:
        returns the Customer Order History in a Tabular form.
        returns True, if is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    print("\n                                      ***  ORDER HISTORY  ***                                             ")
    print("." * 110)
    print(":    S.No    :     CUSTOMER NAME     :   ITEM ID    :       ITEM NAME        :     PRICE     :    QUANTITY   :")
    s_no = 1
    total_sale = 0.0
    order_list = retrieve_data("order_history.csv")
    try:
        for item in order_list:
            total_price = float(item[2]) * float(item[3])
            print("." * 110)
            print(f":    {s_no:<7} :    {item[-1]:<20} :   {item[0]:<8} :     {item[1]:<18} :     {item[2]:<7} :     {item[3]:<7} :")
            s_no += 1
            total_sale += total_price
        print("." * 110)
        print("\n\n" + "." * 57)
        print(f":    TOTAL SALE TILL NOW IN RUPEES    :    {total_sale:<10} :")
        print("." * 57)
        return True
    except Exception as e:
        print("An Error Occurred!")
        print("ERROR:", e, "\n")
        return False


