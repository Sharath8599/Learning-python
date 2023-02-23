# list of inventory items 
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
# how many items are in the warehouse
inventory_len=len(inventory)
# Select the first element 
first=inventory[0]
# Select the last element 
last=inventory[-1]
# Select items from the inventory starting at index 2 and up to, but not including, index 6.
inventory_2_6= inventory[2:6]
# Select the first three elements using slicing
first_3=inventory[0:3]
# How many 'twin bed's are in inventory using count
twin_beds=inventory.count("twin bed")
# Removing the 5th element using pop
removed_item = inventory.pop(4) 
# adding an item using insert
inventory.insert(10,"19th Century Bed Frame")
# sorting the list
inventory.sort()
