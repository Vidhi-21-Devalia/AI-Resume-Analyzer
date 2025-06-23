from django.db import models

# Create your models here.
class ResumeUpload(models.Model):
    resume_file = models.FileField(upload_to='resumes/')
    job_description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
