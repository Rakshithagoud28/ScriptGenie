import streamlit as st
import os
from groq import Groq
from deep_translator import GoogleTranslator
from gtts import gTTS  # ✅ Replaced pyttsx3 with gTTS

# Set Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="ScriptGenie 🎬", layout="centered")
st.title("🧞‍♂️ ScriptGenie - YouTube Video Script Generator")

# Sidebar settings
st.sidebar.header("🌐 Language Selection")
language = st.sidebar.selectbox("Choose a language:", ["English", "Hindi", "Telugu"])

st.sidebar.markdown("---")
st.sidebar.header("🎤 Voiceover Generator")
voiceover = st.sidebar.checkbox("Generate Audio for Script")

# Prompt Input
user_topic = st.text_input("Enter your video topic:", placeholder="e.g., How AI is transforming education")

# Script Genie Chat Mode
chat_mode = st.sidebar.checkbox("🧞‍♀️ Enable Script Chat Mode (Refine Your Script)")
refine_instruction = ""
if chat_mode:
    refine_instruction = st.sidebar.selectbox(
        "Choose Refinement:", 
        ["Make it funnier", "Make it more engaging", "Make it shorter", "Add emotional tone"]
    )

# Script Generation Button
if st.button("✨ Generate Script") and user_topic:
    with st.spinner("Generating magic script ✨"):
        # Base Prompt
        prompt = f"Generate a YouTube video script on the topic: '{user_topic}'. Make it informative and engaging."
        if refine_instruction:
            prompt += f" Now, refine it with the following instruction: {refine_instruction}."

        # Translation Logic
        if language != "English":
            prompt = GoogleTranslator(source='auto', target='en').translate(prompt)

        # Generate Response from Groq
        chat_completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        script = chat_completion.choices[0].message.content.strip()

        # Translate back if needed
        if language != "English":
            script = GoogleTranslator(source='en', target=language.lower()).translate(script)

        st.subheader("📜 Your Script")
        st.text_area("YouTube Video Script", script, height=350)

        # Voiceover using gTTS (only for English)
        if voiceover and language == "English":
            try:
                tts = gTTS(text=script, lang='en')
                tts.save("voiceover.mp3")
                audio_file = open("voiceover.mp3", "rb")
                st.audio(audio_file.read(), format="audio/mp3")
            except Exception as e:
                st.error(f"Voiceover generation failed: {str(e)}")
        elif voiceover and language != "English":
            st.warning("⚠️ Voiceover is only available for English language. Please uncheck the option or switch to English.")

        # 🎬 Auto Video Ideas
        st.subheader("🎬 Video Ideas & SEO")
        seo_prompt = f"Suggest a catchy YouTube video title, a creative thumbnail idea, and 10 SEO tags for the topic: {user_topic}"
        seo_completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": seo_prompt}]
        )
        seo_ideas = seo_completion.choices[0].message.content.strip()
        st.text_area("Video Title, Thumbnail, Tags", seo_ideas, height=200)

else:
    st.info("Enter a topic above to begin generating your magical YouTube script ✨")
