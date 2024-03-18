from django.db import models
import random
import string

def generate_short_url():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Url(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, default=generate_short_url)
