from django import forms
from .models import Appointment,Staff

class AppointmentForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=Staff.objects.all(), empty_label="Select a staff member")
    class Meta:
        model = Appointment
        fields = ['customer_name', 'customer_email', 'staff', 'appointment_time']
