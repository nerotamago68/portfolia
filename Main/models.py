from django.db import models

class AboutMe(models.Model):

    name = models.CharField(max_length=100, default='Ryan')
    college = models.CharField( max_length=100, default='Marinduque State College')
    description = models.TextField()
