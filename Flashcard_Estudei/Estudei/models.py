from django.db import models
from  django.contrib.auth.models import User

class Topic(models.Model):
    """um assunto sobre o qual o usuario estar aprendeno"""
    text = models.CharField(max_length= 200)
    date_added = models.DateTimeField(auto_now_add= True)
    owner = models.ForeignKey(User,on_delete= models.CASCADE)
# Create your models here.
    def __str__(self):
        """devolve uma representação em string do modelo"""
        return self.text

class Entry(models.Model):
    """ algo especifico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic,on_delete= models.CASCADE)
    text = models.TextField ()
    date_added = models.DateTimeField(auto_now_add= True)
    class Meta:
     verbose_name_plural = 'entries'
     def __str__(self):
         """devolva a represnetação em string do modelo"""
         return  self.text[:50] + '...'
     """reticencia mostra que existe mais coisa"""

