from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact


# Create your views here.


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']

    contact = Contact(full_name=full_name, email=email, phone_number=phone_number,
                      company=company, subject=subject, message=message, user_id=user_id)
    contact.save()
    messages.success(request, 'Submitted... Thanks for reaching out')
    return redirect('home')
