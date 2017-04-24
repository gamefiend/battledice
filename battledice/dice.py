import random
from collections import Counter


# default dice for age of sigmar is 6
SIDES = 6

class DiceStack(object):

    def __init__(self, number, target, **options):
        self.stack = []
        self.history = []
        self.target = target
        self.number = number
        self.options = options
        # Roll all our dice...
        for x in range(number):
            self.stack.append(self.roll())
        # ...then add it to our history of rolls.
        self.history.append(self.stack) 

    def __str__(self):
        i = 1
        for stack in self.history:
           output = "Roll {}\n".format(i)
           output += "Dice rolled: {}\n".format(len(stack))
           output += "Successes: {}\n".format(self.count_successes(self.stack, self.target))
           output += "Rolls:\n{}".format(stack)
           return output

    def roll(self):
        return random.randint(1, SIDES)

    def count_successes(self, stack, target):
        success_total = 0
        self.stackcount = Counter(stack)        
        for i in self.stackcount.keys():
            if int(i) > int(target):
                success_total += self.stackcount[i]
        return success_total

    def history(self, stack):
        pass

if __name__ == "__main__":
    d = DiceStack(10, 4)
    print str(d)
    dd = DiceStack(20, 5)
    print str(dd)
