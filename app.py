import streamlit as st
from audio_input.recorder import record_audio
from audio_input.transcriber import transcribe_audio
from vision_analysis.emotion_detector import capture_frame, detect_emotion
from llm_prompt_engine.prompt_builder import build_prompt
from llm_prompt_engine.llm_interface import get_ai_response
from llm_prompt_engine.empathy_scorer import empathy_score
from diffusion_art.prompt_to_image import emotion_to_art_prompt
from diffusion_art.art_generator import generate_image
from evaluations.logger import log_session


def run_app():
    st.set_page_config(page_title="MirrorMuse", layout="centered")
    st.title("🪞 MirrorMuse: Your Emotional Reflection Companion")

    if st.button("🎙️ Speak"):
        record_audio("output.wav", duration=6)
        transcript = transcribe_audio("output.wav")
        st.subheader("You said:")
        st.write(transcript)

        frame = capture_frame()
        emotion = detect_emotion(frame)
        st.subheader("Detected Emotion:")
        st.write(emotion)

        prompt = build_prompt(transcript, emotion)
        ai_response = get_ai_response(prompt)
        st.subheader("AI's Reflective Response:")
        st.write(ai_response)

        score = empathy_score(transcript, ai_response)
        st.write(f"Empathy Score: {score}/1.0")

        art_prompt = emotion_to_art_prompt(emotion)
        generate_image(art_prompt, output_path="emotion_art.png")
        st.subheader("🎨 AI Art Based on Emotion:")
        st.image("emotion_art.png", use_column_width=True)

        log_session(transcript, emotion, ai_response, score)