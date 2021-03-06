#sssssh. thest aren't real tests

from character import Character
from character import Hero
from character import Monster

#Characters can be instantiated with name and avatar

arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# after adding 2 items to inventory
#length of inventory should == 2

arya.inventory.append('sword')
arya.inventory.append('mask')

print(len(arya.inventory))

#arya should have a 'greet' method
#and when i call it with arya.greet(jon), it should return
#"Hello,Jon Snow, I am Arya Stark. I am awesome."
print(arya.greet(jon))

#arya should have a 'greet' method
#and when i call it with arya.greet(jon), it should return
#"Hello, I am Arya Stark. I am awesome."
print(arya.greet())

#I should be able to create a Hero Instance
bronn = Hero("Bronn of the Blackwater", "bronn.png")

#hero should be able to greet character
print(bronn.greet(arya))
print(jon.greet(bronn))
print(arya.greet(bronn))

#remember to import the 'Monster' subclass from 'character.py' 
#otherwise, you get an error message!

dragon = Monster()

print(dragon.greet())

print(dragon.greet(jon))

print(bronn.greet(dragon))
print(bronn.greet(jon))
