# Object-Oriented-Programming - What is it?
# OOP is all about creating our own objects

class BigObject:  # Class
    pass


obj1 = BigObject()  # instanciate
obj2 = BigObject()

print(type(obj1))


class PlayerCharacter:
    isWizard = True  # class object attribute

    @classmethod
    def adding_things(cls, item1, item2):
        items = []
        items.append(item1)
        items.append(item2)
        return cls('Severus Snape', items)

    @staticmethod
    def adding_items(item1, item2):
        items = []
        items.append(item1)
        items.append(item2)
        return items

    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def run(self):
        print(f'{self.name} is running...')


player1 = PlayerCharacter('Harry Potter')
player2 = PlayerCharacter('Hermione Granger')

player1.run()
player2.run()

player2.attack_value = 50
print(player2.attack_value)

# help(player1)

print(player1.isWizard)
print(PlayerCharacter.isWizard)

player3 = PlayerCharacter.adding_things('Magic potion', 'Wizard hat')
print(player3.items)

items = PlayerCharacter.adding_items('item1', 'item2')
print(items)
