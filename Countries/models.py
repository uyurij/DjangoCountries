from django.db import models

   
class country(models.Model):
   country  = models.CharField(max_length=100)
   languages = models.CharField(max_length=100)
   #count = models.PositiveIntegerField()
   #description =  models.CharField(max_length=200, default = 'Описание элемента')
   #colors = models.ManyToManyField(to=Color)

   def __repr__(self):
        return f'country({self.name})'