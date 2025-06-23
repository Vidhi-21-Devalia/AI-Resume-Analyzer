# 📄 Resume Analyzer using Django & NLP

A full-stack web application that allows users to upload resumes and analyzes them using **Natural Language Processing (NLP)**. Built with Django and powered by **spaCy**, the app extracts key information such as skills, experience, and education details.

---

## 🚀 Features

- ✅ Upload resume files in `.pdf`, `.docx`, or `.txt` format
- ✅ NLP-based parsing using **spaCy (`en_core_web_sm`)**
- ✅ Extracts:
  - Name
  - Email (basic logic)
  - Skills (e.g., Python, Django, SQL)
  - Education info
  - Experience
- ✅ Displays analyzed data on a result page
- ✅ Stores uploaded resumes in the `media/resumes/` folder
- ✅ Resume data saved in **MySQL database**
- ✅ Basic frontend using HTML/CSS and Django templates

---

## 🛠️ Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Backend     | Python, Django     |
| Frontend    | HTML, CSS (templates) |
| NLP         | spaCy              |
| Database    | MySQL              |
| ORM         | Django ORM         |
