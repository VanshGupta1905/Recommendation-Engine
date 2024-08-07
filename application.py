import streamlit as st
from streamlit_mic_recorder import speech_to_text
st.title("Shopping App")
from streamlit_mic_recorder import mic_recorder
from streamlit_card import card

text = speech_to_text(
    language='en',
    start_prompt="Start recording",
    stop_prompt="Stop recording",
    just_once=False,
    use_container_width=False,
    callback=None,
    args=(),
    kwargs={},
    key=None
)

