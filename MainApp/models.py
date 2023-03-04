from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User

LANGS = [
    ('PY', 'Python'),
    ('JS', 'JavaScript'),
    ('CPP', 'C++'),
]

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)







# items = Snippet.objects.all()
# count = Snippet.objects.aggregate(id=Max('id'))