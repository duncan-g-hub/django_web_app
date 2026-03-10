from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.models import Band, Listing
from listings.forms import ContactUsForm
from listings.forms import BandForm


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
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} via Merchex Contact Us Form",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request,"listings/contact.html", {'form': form})


def email_sent(request):
    return render(request,"listings/email_sent.html")

def add_band(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,"listings/add_band.html",{"form": form})

