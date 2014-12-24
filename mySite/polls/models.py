from django.db import models

# Create your models here.
class Poll (models.Model):
    question = models.CharField(max_length=200);
    pub_date = models.DateTimeField('date published');
#    def __str__(self):              # __unicode__ on Python 2
#        return self.question	

class Choice(models.Model):
    poll = models.ForeignKey(Poll);
    text = models.CharField(max_length=200);
    votes = models.IntegerField(default=0);
#    def __str__(self):              # __unicode__ on Python 2
#        return self.poll
