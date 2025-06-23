from django import forms
from .models import ResumeUpload

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = ResumeUpload
        fields = ['resume_file', 'job_description']
        widgets = {
            'resume_file': forms.ClearableFileInput(attrs={'accept': '.pdf,.doc,.docx'}),
            'job_description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter job description here...'}),
        }