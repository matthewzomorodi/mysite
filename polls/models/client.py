from django.db import models
from .validators import validate_phone_number

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=75)
    email = models.EmailField("Email", max_length=254, blank=True, null=True)
    phone_number = models.CharField("Phone Number",
                                    max_length=15,
                                    blank=True,
                                    validators =[validate_phone_number])