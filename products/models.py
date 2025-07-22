from django.db import models


class category(models.Model):
  name = models.CharField(max_length= 100)
  
  @staticmethod
  def get_all_categories():
    return category.objects.all()
  
  def __str__(self):
    return self.name

class Customer (models.Model):
  first_name = models.CharField(max_length = 12)
  last_name = models.CharField(max_length = 20)
  phone_number = models.IntegerField(max_length = 11)
  email = models.EmailField()
  password = models.CharField(max_length = 30)