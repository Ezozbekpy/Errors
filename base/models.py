from django.db import models
from django.contrib.auth.models import User
class Main(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, )
    img = models.ImageField(upload_to='imgerror')
    description =  models.TextField(null=True, blank=True)
    serious_problem = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return f'{self.title}'


