#name
#avatar (profile picture)
#inventory


class Character():
    #"dunder init" method is the constructor
    def __init__(self, new_name, new_avatar):
        #'self' is the customary way to refer to the instance being built
        #in some other languagers, they use 'this'
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []

    # 'someone=None' is a default argument
    #'None' is equivalent to 'null' in other languages
    def greet(self, someone=None):
        # When we assume that the 'someone' argument has a '.name. property
        #this is an Object-Oriented Programming principle called
        #polymorphism.
        #In Python, it's called "Duck Typing" 
        # (if it walks like a duck, and talks like a duck... )
        if someone:
            return "Hello, %s, I am %s. I am awesome." %(someone.name, self.name,)
        else:
            return "Hello, I am %s. I am awesome." %(self.name,)
class Monster(Character):
    def __init__(self):
        pass

    def greet(self, someone=None):
        return "Roaaaaar!"

#Hero is a kind of Character
#Hero is a subclass of Character
#Hero inherits from Character
#Character is the super class of Hero
class Hero(Character):
    def greet(self, someone=None):
        if type(someone) == Monster:
            return "Eeeeeeek!"
        else:
            return super().greet(someone)

