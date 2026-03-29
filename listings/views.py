from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import Listing


def listing_list(request):
    listings = Listing.objects.filter(status="approved")

    city = request.GET.get("city")
    if city:
        listings = listings.filter(city__icontains=city)

    return render(request, "listings/listing_list.html", {
        "listings": listings
    })


def listing_detail(request, slug):
    listing = get_object_or_404(Listing, slug=slug)
    return render(request, "listings/listing_detail.html", {
        "listing": listing
    })


def listing_create(request):
    if request.method == "POST":
        Listing.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            city=request.POST.get("city"),
            budget=request.POST.get("budget"),
            phone=request.POST.get("phone"),
            category_id=request.POST.get("category"),
        )

        # email известие
        if settings.EMAIL_HOST_USER:
            send_mail(
                "Нова заявка",
                "Имате нова клиентска заявка.",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,
            )

        return redirect("home")

    return render(request, "listings/listing_create.html")
