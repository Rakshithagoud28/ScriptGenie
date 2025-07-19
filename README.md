# 🎬 ScriptGenie - AI-Powered YouTube Script Generator

**ScriptGenie** is a fun and powerful Streamlit app that helps you generate high-quality YouTube video scripts using Groq's blazing fast LLMs.\n
**Try It Here** : https://rakss-scriptgenie.streamlit.app/

### ✨ Features
- 🧠 AI-generated video scripts (2-minute format)
- 🎨 Choose tone: Motivational, Casual, Funny, Educational
- 🌐 Supports English and Hindi
- 📥 Download or copy script

### 🛠️ Built With
- Streamlit
- Groq LLM API (LLaMA 3)
- Python + Requests + dotenv

### 🚀 Run Locally

```bash
git clone https://github.com/yourusername/scriptgenie.git
cd scriptgenie
pip install -r requirements.txt
touch .env  # Add your GROQ_API_KEY inside
streamlit run app.py
