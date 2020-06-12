from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # dest1 = Destination()
    # dest1.name = "mumbai"
    # dest1.desc = "the city that never sleeps"
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = "hyderabad"
    # dest2.desc = "city of nawabs"
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "bengaluru"
    # dest3.desc = "the city that never sleeps"
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 700
    # dest3.offer = False

    # dests = [dest1,dest2,dest3]
    dests = Destination.objects.all()

    return render(request,'index.html',{'dests':dests})