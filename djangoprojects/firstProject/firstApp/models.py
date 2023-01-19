from django.db import models

# Create your models here.
# create models here and storing in database acts as mysql
class Contact(models.Model):

    uname=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50,)
    sem=models.CharField(max_length=50,)
    mobno=models.CharField(max_length=50,)


    def __str__(self):
        return self.name
