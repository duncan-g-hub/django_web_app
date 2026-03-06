from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html",
            {"first_band": bands[0],
                   "second_band": bands[1],
                   "third_band": bands[2],})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""<h1>Listings</h1> 
                        <p>Liste des annonces :</p>
                        <ul>
                            <li>{listings[0].title}</li>
                            <li>{listings[1].title}</li>
                            <li>{listings[2].title}</li>
                        </ul>""")

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>Nous contacte</p>')