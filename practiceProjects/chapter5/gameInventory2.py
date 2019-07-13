stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + "x " + k)
        total_items += v

    print("\nTotal number of items: " + str(total_items))


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)

    return inventory


stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
