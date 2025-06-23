import spacy
import pdfplumber
import docx
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeUploadForm
from .models import ResumeUpload

nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return ' '.join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        return ' '.join([para.text for para in doc.paragraphs])
    return ""

def extract_skills(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]
    # Simple sample skill list
    known_skills = ['python', 'django', 'sql', 'excel', 'communication', 'flask', 'html', 'css']
    return list(set(token for token in tokens if token in known_skills))

def calculate_score(resume_skills, job_description):
    jd_skills = extract_skills(job_description)
    matched = set(resume_skills) & set(jd_skills)
    score = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0
    return score, matched, jd_skills

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('result', pk=instance.pk)
    else:
        form = ResumeUploadForm()
    return render(request, 'analyzer/upload.html', {'form': form})

def result(request, pk):
    instance = get_object_or_404(ResumeUpload, pk=pk)
    resume_text = extract_text(instance.resume_file)
    resume_skills = extract_skills(resume_text)
    score, matched, jd_skills = calculate_score(resume_skills, instance.job_description)
    
    return render(request, 'analyzer/result.html', {
        'score': score,
        'resume_skills': resume_skills,
        'jd_skills': jd_skills,
        'matched': matched,
        'instance': instance
    })
