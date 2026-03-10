from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html",{"bands": bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, "listings/band_detail.html",{"band": band})


def about(request):
    return render(request,"listings/about.html")


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, "listings/listing_detail.html", {"listing": listing})

def contact(request):
    return render(request,"listings/contact.html")