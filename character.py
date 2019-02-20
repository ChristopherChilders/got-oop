#name
#avatar (profile picture)
#inventory


class Character():
    #"dunder init" method is the constructor
    def __init__(self, new_name):
        #'self' is the customary way to refer to the instance being built
        #in some other languagers, they use 'this'
        self.name = new_name