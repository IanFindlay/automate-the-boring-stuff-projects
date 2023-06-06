###Fantasy Game Inventory###


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'map fragments': 3}

# This function displays the inventory
def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items : ' + str(item_total))


def add_to_inventory(inventory, added_items):
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)

inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
