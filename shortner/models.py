from django.db import models
import string,random

# Create your models here.
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
class Url(models.Model):
    original_url=models.URLField(max_length=200)
    short_code=models.CharField(max_length=6, unique=True, default=generate_short_code)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.original_url} - {self.short_code}"
