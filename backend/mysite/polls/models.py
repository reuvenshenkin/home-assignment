from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
    	return reverse('question_detail', kwargs={'pk': self.pk})

   
        
            