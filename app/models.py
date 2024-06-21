from django.db import models


class ticket_info(models.Model):
    remark = models.CharField(null=True, max_length=50)
    

# Create your models here.
class myip(models.Model):
    my_ticket = models.ForeignKey(ticket_info,null=True, on_delete=models.CASCADE)
    ip = models.CharField(null=True, max_length=50)
    city = models.CharField(null=True, max_length=50)
    region = models.CharField(null=True, max_length=50)
    country = models.CharField(null=True, max_length=50)
    loc = models.CharField(null=True, max_length=50)
    org = models.CharField(null=True, max_length=50)
    postal = models.CharField(null=True, max_length=50)

