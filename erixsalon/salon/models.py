from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    duty_start = models.TimeField()
    duty_end = models.TimeField()
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()

    def __str__(self):
        return f'{self.customer_name} - {self.staff.name} at {self.appointment_time}'

