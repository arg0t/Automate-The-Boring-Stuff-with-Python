stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        itemTotal = itemTotal + v
        print(v, end=" ")
        print(k)

    print("Total number of items: " + str(itemTotal))

displayInventory(stuff)
