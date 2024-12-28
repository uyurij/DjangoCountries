from django.db import models

class country(models.Model):
   country  = models.CharField(max_length=100)
   languages = models.CharField(max_length=100)
  #description =  models.CharField(max_length=200, default = 'Описание элемента')

   def __repr__(self):
        return f'country({self.name})'