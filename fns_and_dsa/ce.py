class OutOfStockError(Exception): # We define a custom exception class OutOfStockError that inherits from the base Exception class. This custom exception is designed to handle out-of-stock items.
    def __init(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock"
    

product_inventory = {
    "apple": 10,
    "banana": 5,
    "oranges": 0,
    "grapes": 3
}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase succesful: {quantity} {item}")
            product_inventory[item] -= quantity

    except KeyError:
        print(f"Sorry, {item} is not in our inventory list.")

purchase_item((input("fruit?")), int(input("how many?")))