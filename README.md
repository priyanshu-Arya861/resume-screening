# 🚀 AI Resume Screening System

An intelligent **AI-powered Resume Screening Web App** that matches resumes with job descriptions using **Natural Language Processing (NLP)** and **Machine Learning**.

---

## 📌 Features

* 📄 Upload multiple resumes (PDF)
* 🧠 NLP-based resume analysis
* 📊 Match resumes with job description
* 🏆 Rank candidates based on similarity score
* ⚡ Fast and simple UI
* 🌐 Deployed online for real-time usage

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)
* **Frontend:** HTML, CSS
* **Libraries:** NLTK, NumPy, Pandas
* **Deployment:** Render

---

## 📂 Project Structure

```
resume_screening/
│
├── app.py
├── model.py
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── login.html
│   ├── signup.html
│
├── uploads/
│   ├── sample resumes (PDFs)
```

---

## ⚙️ Installation (Run Locally)

1. Clone the repository:

```
git clone https://github.com/your-username/resume-screening.git
cd resume-screening
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

This project is deployed on Render.

To deploy:

* Push code to GitHub
* Connect repo to Render
* Add build & start commands

---

## 📊 How It Works

1. User uploads resumes
2. System extracts text from PDFs
3. Applies **TF-IDF Vectorization**
4. Computes **Cosine Similarity**
5. Displays ranked results

---

## 🔥 Future Improvements

* Add resume score (%)
* Highlight matched & missing skills
* Improve UI/UX
* Add authentication system
* Use advanced NLP models (BERT/GPT)

---

## 👨‍💻 Author

**Karuna**
GitHub: https://github.com/Karuna-1512

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share!
