from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import CollaborateForm
# Create your views here.


def about(request):
    """
    Allow users  to send collaboration requests.

    **Template**
    :template:`contact/contact.html`
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Message received! You can expect a respond within 2 working days.'
            )
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact,
         "collaborate_form": collaborate_form},
    )