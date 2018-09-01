
class Friend(object):

    def __init__(self, name):
        self.name = name
        self.age = 20
        self.favorite_color = 'black'

    def say_hi(self):
        return 'hi, my name is ' + self.name

    def long_intro(self):
        return self.say_hi() + ' and i am ' + str(self.age)
