from django.db import models
from django.forms import ModelForm
from datetime import datetime


# Create your models here.
class Analysis(models.Model):
    title = models.CharField(max_length=200, default="Default Title")
    file = models.FileField(upload_to="input-files/",
                            default='input-files/DEFAULT_Outline_0_000.txt')
    created_at = models.DateTimeField(auto_now=True)
    unique_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = ['title', 'file']
