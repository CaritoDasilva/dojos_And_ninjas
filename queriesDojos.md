# Run the shell and import your models

from dojo_ninjas_app.models import Dojos, Ninjas

# Query: Create 3 new dojos

Dojos.objects.create(name="Ada Lovelace", city="Santiago", state="RM")  
Dojos.objects.create(name="Lemebel", city="Viña del mar", state="VA")
Dojos.objects.create(name="Margaret Hamilton", city="Puyehue", state="LL")    

# Query: Create 3 ninjas that belong to the first dojo

Ninjas.objects.create(dojo=Dojos.objects.get(id=4),first_name="Carolina",last_name="Da Silva") 

# Query: Retrieve all the ninjas from the first dojo

ninjas_first_dojo = Ninjas.objects.filter(dojos=Dojos.objects.get(id=4)) 

# Query: Retrieve the last ninja's dojo

Ninjas.objects.last()       

# Query: Create a new dojo

Dojos.objects.create(name="Buena Onda City", city="Valparaiso", state="VA", desc=15) 