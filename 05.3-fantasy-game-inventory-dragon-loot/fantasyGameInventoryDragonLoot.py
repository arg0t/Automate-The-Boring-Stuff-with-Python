def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0

    for k, v in inventory.items():
        itemTotal = itemTotal + v
        print(v, end=" ")
        print(k)

    print("Total number of items: " + str(itemTotal))

def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1

    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
