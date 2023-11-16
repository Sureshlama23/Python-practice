# An objects variables should not always be directly accessible.
# The methods can ensure the correct values are set.
# if an incorrect value is set, the method can return an error.
import random
uc=int(input('''
    1. Start The Game
    2. Exit

'''))
      if uc==1:
        yourchoice=int(input('''
           1.Rock
           2. Scissor
           3. Paper
           '''))
        computerchoice=random.choice()
        if yourchoice==1:
            

