import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from listings.models import Listing

# 🔑 сложи твоя API ключ
API_KEY = ""


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
        "sender": {"email": settings.EMAIL_HOST_USER},
        "to": [{"email": to_email}],
        "subject": subject,
        "htmlContent": content
    }

    r = requests.post(url, json=data, headers=headers)
    return r.json()


# -----------------------------
# HOME
# -----------------------------
def home(request):
    listings = Listing.objects.filter(status="approved")[:6]
    return render(request, "pages/home.html", {
        "listings": listings
    })


# -----------------------------
# CONTACT FORM
# -----------------------------
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        honeypot = request.POST.get("website")  # anti-spam

        # 🛑 Anti-spam
        if honeypot:
            return redirect("home")

        # 📧 HTML имейл
        email_content = f"""
        <h2>Ново запитване от сайта</h2>

        <b>Име:</b> {name}<br>
        <b>Телефон:</b> {phone}<br>

        <br>
        <b>Съобщение:</b><br>
        {message}
        """

        try:
            send_email(
                settings.EMAIL_TO_USER,
                f"Ново запитване от {name}",
                email_content
            )
            messages.success(request, "Съобщението беше изпратено успешно!")

        except Exception as e:
            print("EMAIL ERROR:", e)
            messages.error(request, "Грешка при изпращане!")

        return redirect("home")

    return render(request, "pages/contact.html")