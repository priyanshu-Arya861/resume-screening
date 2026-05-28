from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import docx

# ---------------- TEXT EXTRACTION ----------------
def extract_text(file_path):
    text = ""

    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text

    else:
        # fallback for txt
        with open(file_path, "r", errors="ignore") as f:
            text = f.read()

    return text.lower()


# ---------------- SKILL LIST ----------------
SKILLS = [
    "python", "java", "c++", "machine learning", "deep learning",
    "sql", "html", "css", "javascript", "react", "node.js",
    "flask", "django", "aws", "docker", "kubernetes",
    "pandas", "numpy", "tensorflow", "pytorch"
]


# ---------------- SKILL EXTRACTION ----------------
def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return list(set(found))


# ---------------- MAIN FUNCTION ----------------
def process_resume(job_desc, resume_path):

    resume_text = extract_text(resume_path)
    job_desc = job_desc.lower()

    # -------- SIMILARITY --------
    documents = [job_desc, resume_text]
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(documents)

    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

    # -------- SKILLS --------
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_desc)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    return {
        "score": round(score * 100, 2),
        "matched": matched,
        "missing": missing
    }