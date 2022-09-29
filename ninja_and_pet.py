# from pet import Pet
from ninja import Ninja
from wolf import Wolf

# snoopy= Pet('Snoopy',"beagle","Roll Over")
# charlie= Ninja("Charlie","Cookies","Dog Food", snoopy)

# walk returns a ninja so you can chain a ninja method 
# off of it meaning you can attach feed

# charlie.walk().feed().bathe()

# ghost= Wolf('Ghost')

# ghost.noise()

# i want user to name wolf
# call input as a listener
print ('You will create a wolf!')
wolf_name=input('Name your wolf: ')
wolf=Wolf(wolf_name)

print(f'Your wolf\'s name is {wolf.name} ')
