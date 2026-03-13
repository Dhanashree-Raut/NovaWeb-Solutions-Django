from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    # pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name + " | " + self.email + " | "+ self.phone
