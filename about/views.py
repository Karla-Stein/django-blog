from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages


# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    collaborate_form = CollaborateForm()

    if request.method == "POST":
        print('Received a POST request')
        request_form = CollaborateForm(data=request.POST)
        if request_form.is_valid():
            request_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days'  # noqa: E501
            )

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form},
    )

