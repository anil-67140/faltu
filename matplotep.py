

import csv
import matplotlib.pyplot as plt
from collections import Counter

# Function to retrieve data from a file
def retrieve_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [line.strip().split(',') for line in file.readlines()]
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found!")
        return []
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}")
        return []

# Function to load menu items from the CSV
def load_menu(file_path):
    menu_data = retrieve_data(file_path)
    menu_dict = {item[0]: item[1] for item in menu_data}  # item_id: item_name
    return menu_dict

# Function to count occurrences of each item in the order list
def count_orders(order_list):
    item_counts = Counter()
    for order in order_list:
        item_name = order[1]  # Assuming item name is the second element in each order entry
        quantity = int(order[3])  # Assuming quantity is the fourth element in each order entry
        item_counts[item_name] += quantity
    return item_counts

# Function to plot a bar graph of popular orders
def plot_bar_graph(item_counts, menu_dict):
    item_names = []
    counts = []
    colors = []

    for item_name in menu_dict.values():
        count = item_counts.get(item_name, 0)
        item_names.append(item_name)
        counts.append(max(count, 0.1))  # Ensure all items have at least a small bar

        if count > 5:
            colors.append('green')
        elif count == 0:
            colors.append('yellow')
        else:
            colors.append('red')

    plt.figure(figsize=(10, 6))
    plt.bar(item_names, counts, color=colors)
    plt.xlabel('Item Name')
    plt.ylabel('Number of Orders')
    plt.title('Popular Orders')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Main function to run the script
def main():
    menu_file = "C:\\Users\\LENOVO\\Desktop\\python froject\\cafe_menu.csv"  # Update with your actual file path
    order_history_file = "C:\\Users\\LENOVO\\Desktop\\python froject\\order_history.csv"  # Update with your actual file path

    menu_dict = load_menu(menu_file)
    orders = retrieve_data(order_history_file)

    if orders:
        order_counts = count_orders(orders)
        plot_bar_graph(order_counts, menu_dict)
    else:
        print("No orders found.")

# Execute the main function
if __name__ == "__main__":
    main()

