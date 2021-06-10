from django.db import models

# Create your models here.
class exam_table(models.Model):
    Faculty_name = models.CharField(max_length=50)
    Subject = models.CharField(max_length = 50)
    Upload = models.URLField(max_length=100)
    Exam = models.FileField(upload_to = 'exams')
