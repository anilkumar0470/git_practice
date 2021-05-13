from django.shortcuts import render
from .models import Destination

dest1 = Destination()
dest1.name = "Bangalore"
dest1.desc = "the coolest city in india"
dest1.price = 1900
dest1.img = "destination_1.jpg"
dest1.offer = False

dest2 = Destination()
dest2.name = "Mumbai"
dest2.desc = "Business city of india"
dest2.price = 2000
dest2.img = "destination_2.jpg"
dest2.offer = True

dest3 = Destination()
dest3.name = "Hyderabad"
dest3.desc = "silicon city of india"
dest3.price = 1500
dest3.img = "destination_3.jpg"
dest3.offer = False


dests = [dest1, dest2, dest3]

def index(request):
    # return HttpResponse("hello world")
    return render(request, "index.html", {"dests": dests})