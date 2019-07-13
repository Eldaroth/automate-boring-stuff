stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + "x " + k)
        total_items += v

    print("\nTotal number of items: " + str(total_items))


displayInventory(stuff)
