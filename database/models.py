

from __future__ import unicode_literals
from django.db import models
class report (models.Model):
    No = models.CharField(max_length=40,default="",editable=False,null=True)
    Title = models.CharField(max_length=400,null=True)
    Inventors = models.CharField(max_length=800,null=True)
    Applicants = models.CharField(max_length=400,null=True)
    Publication_number = models.CharField(max_length=400, default="", editable=False,null=True)
    Country = models.CharField(max_length=500, default="", editable=False,null=True)
    Earliest_priority = models.CharField(max_length=800, default="", editable=False,null=True)
    IPC = models.CharField(max_length=480,null=True)
    CPC = models.CharField(max_length=4880,null=True)
    Publication_date = models.CharField(max_length=40,default="", editable=False,null=True)
    Publication_Year = models.CharField(max_length=40,default="", editable=False,null=True)
    Earliest_publication = models.CharField(max_length=400,default="", editable=False,null=True)
    Family_number = models.CharField(max_length=800,default="", editable=False,null=True)