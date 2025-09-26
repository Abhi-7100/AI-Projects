

# 📘 AI Tutor – GenAI Powered Learning Assistant

🚀 Overview

The AI Tutor is an intelligent, interactive web application that provides personalized, step-by-step explanations for learning topics such as mathematics. It leverages Generative AI (OpenAI GPT models) to simulate a human-like tutor, answering questions in real time with clarity and context awareness.

This project is built with Python, Flask, and OpenAI’s API, enabling learners to engage in meaningful conversations and get guided solutions to their problems.


---

## 🛠️ Features

✅ AI-Powered Tutoring – Provides detailed explanations for math problems and concepts.

✅ Conversational Interface – Maintains session-based chat history with user and tutor responses.

✅ Customizable Subjects – Easily extendable beyond math to other subjects.

✅ Web Interface – Simple Flask-based front-end to ask and display answers.

✅ Real-time Interaction – Uses OpenAI GPT for quick, context-aware responses.



---

## 🖥️ Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS (Jinja2 templates)

AI Model: OpenAI GPT (ChatCompletion API)

Deployment Ready: Can be deployed on platforms like Render, Heroku, or Vercel with backend



---

## 📂 Project Structure

AI-Tutor/
│
├── app.py                # Main Flask backend
├── templates/
│   └── index.html        # Frontend user interface
├── static/               # (Optional) CSS/JS files
├── requirements.txt      # Dependencies
└── README.md             # Project documentation


---

## ⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/yourusername/ai-tutor.git
cd ai-tutor

2. Create Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Add Your OpenAI API Key

Open app.py

Replace "your_api_key_here" with your actual key:
openai.api_key = "sk-xxxx..."

(or set it as an environment variable OPENAI_API_KEY).

5. Run the Application

python app.py

Open browser → http://127.0.0.1:5000/


## 🎯 Usage

1. Enter your question (e.g., "Solve 2x + 5 = 15 step by step").


2. The AI Tutor generates a step-by-step explanation.


3. Continue asking questions – the chat history is preserved within your sessions 


## 🔮 Future Enhancements

🌐 Multi-subject support (Science, Coding, History, etc.)

🎤 Voice-based Q&A

📊 Graphical/visual solutions for math problems

📱 Responsive UI for mobile learning


# 🤝 Contribution

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to improve.




