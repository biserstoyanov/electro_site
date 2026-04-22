import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from .models import Listing

API_KEY = ''


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


# -----------------------------
# BREVO EMAIL FUNCTION
# -----------------------------
def send_email(to_email, subject, content):
    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": API_KEY,
        "content-type": "application/json"
    }

    data = {
        "sender": {"email": "info@stanelectric.energy"},
        "to": [{"email": to_email}],
        "subject": subject,
        "htmlContent": content
    }

    r = requests.post(url, json=data, headers=headers)
    return r.json()


# -----------------------------
# CREATE LISTING + EMAIL
# -----------------------------
def listing_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        city = request.POST.get("city")
        budget = request.POST.get("budget")
        phone = request.POST.get("phone")
        category = request.POST.get("category")

        Listing.objects.create(
            title=title,
            description=description,
            city=city,
            budget=budget,
            phone=phone,
            category_id=category,
        )

        # 📧 СЪЗДАВАМЕ HTML СЪОБЩЕНИЕ С ДАННИТЕ ОТ ФОРМАТА
        email_content = f"""
        <h2>Нова клиентска заявка</h2>

        <b>Заглавие:</b> {title}<br>
        <b>Описание:</b> {description}<br>
        <b>Град:</b> {city}<br>
        <b>Бюджет:</b> {budget}<br>
        <b>Телефон:</b> {phone}<br>
        <b>Категория ID:</b> {category}<br>
        """

        # 📬 пращаме към твоя имейл
        if settings.EMAIL_HOST_USER:
            send_email(
                settings.EMAIL_HOST_USER,
                f"Нова заявка от {city}",
                email_content
            )

        return redirect("home")

    return render(request, "listings/listing_create.html")