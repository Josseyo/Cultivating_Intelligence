from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import CollaborateForm

# Create your views here.


def contact_view(request):
    """
    Handle the display and submission of collaboration requests.

    This view allows users to send collaboration requests through a form.
    Upon successful submission, a success message will be displayed.

    **Template**
    :template:`contact/contact.html`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered contact page with the contact information
        and form.
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Message received! You can expect a response "
                "within 2 working days.",
                )

    contact = Contact.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "contact.html",
        {"contact": contact, "collaborate_form": collaborate_form},
    )
