from django.shortcuts import render, get_object_or_404, redirect
from .models import Staff, Appointment
from .forms import AppointmentForm

def home(request):
    return render(request, 'salon/home.html')

def contact(request):
    return render(request, 'salon/contact.html')

def book_appointment(request):
    return redirect('https://forms.gle/SxUFpSF5EFVdpbt9A')
