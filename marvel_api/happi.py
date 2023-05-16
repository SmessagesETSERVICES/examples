from marvel import Marvel

from keys import PRIVATE_KEY, PUBLIC_KEY


m = Marvel(PUBLIC_KEY=PUBLIC_KEY, 
           PRIVATE_KEY=PRIVATE_KEY)

characters = m.characters

my_char = characters.all(name="black bird")["data"]["results"]

print(my_char[0]["series"])


