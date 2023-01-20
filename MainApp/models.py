from django.db import models
from django.db.models import Max

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)

# items = Snippet.objects.all()
# count = Snippet.objects.aggregate(id=Max('id'))