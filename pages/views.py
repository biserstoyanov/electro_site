from django.shortcuts import render, redirect

# Create your views here.
from listings.models import Listing
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render


def home(request):
    listings = Listing.objects.filter(status="approved")[:6]
    return render(request, "pages/home.html", {
        "listings": listings
    })


def prices(request):
    return render(request, "pages/prices.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        honeypot = request.POST.get("website")  # anti-spam

        # Anti-spam проверка
        if honeypot:
            return redirect("home")

        full_message = f"""
        Име: {name}
        Телефон: {phone}

        Съобщение:
        {message}
        """

        send_mail(
            subject="Ново запитване от сайта",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=True,
        )

        messages.success(request, "Съобщението беше изпратено успешно!")

    return render(request, "pages/contact.html")
