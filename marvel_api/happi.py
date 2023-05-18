from marvel import Marvel

from keys import PRIVATE_KEY, PUBLIC_KEY


m = Marvel(PUBLIC_KEY=PUBLIC_KEY, 
           PRIVATE_KEY=PRIVATE_KEY)

event = m.events

my_events = event.all()["data"]['results']
data = my_events[0]['series']
print(data)
