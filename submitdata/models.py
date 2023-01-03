from django.db import models

# Create your models here.
class detail(models.Model):
    sno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=250)
    cfname = models.CharField(max_length=250)
    ccourse = models.CharField(max_length=250)
    cphone = models.CharField(max_length=15)
    def __str__(self):
        return str(self.sno)