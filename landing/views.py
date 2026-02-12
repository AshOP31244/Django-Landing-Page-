from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import redirect
from .models import Lead
from django.shortcuts import render
from django.contrib import messages



def home(request):
    return render(request, "landing/index.html")


def submit_lead(request):
    if request.method == "POST":
        lead = Lead.objects.create(
            company_name=request.POST.get("company_name"),
            contact_person=request.POST.get("contact_person"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            location=request.POST.get("location"),
            application=request.POST.get("application_type"),
            capacity=request.POST.get("capacity"),
        )

        subject = "New Lead Received – Shubham Tanks"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = ["ashwaz@shubhamtanks.com"]

        html_content = render_to_string("emails/new_lead.html", {"lead": lead})

        msg = EmailMultiAlternatives(
            subject=subject,
            body="New lead received.",
            from_email=from_email,
            to=to_email,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # ✅ THIS IS THE KEY LINE
        messages.success(
            request,
            "Thank you! Our engineering team has received your request and will contact you within 24 hours."
        )

        return redirect("home")

    return redirect("home")

