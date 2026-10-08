import streamlit as st
import time

st.set_page_config(page_title="Cognitive Reading Enhancer", page_icon="⚡", layout="wide")

st.title("⚡ FocusRead: Algorithmic Study Enhancer")
st.markdown(
    "Enhance reading speed and focus on dense academic texts using **Bionic Typography formatting** "
    "and real-time reading telemetry."
)

# Core Algorithm: Pure Python String Transformation
def apply_bionic_reading(text: str) -> str:
    """Algorithmically bolds the initial fixation points of words to guide eye movement."""
    words = text.split()
    formatted_words = []
    
    for word in words:
        length = len(word)
        if length == 1:
            formatted_words.append(f"**{word}**")
        elif length <= 3:
            formatted_words.append(f"**{word[:1]}**{word[1:]}")
        else:
            mid = (length // 2) + 1
            formatted_words.append(f"**{word[:mid]}**{word[mid:]}")
            
    return " ".join(formatted_words)

# UI Layout
col1, col2 = st.columns([1, 1], gap="medium")

default_text = """Artificial Intelligence and Computer Science are rapidly reshaping modern problem-solving. 
By understanding algorithms, data structures, and mathematical optimization, students can build software systems 
that analyze patterns, improve human productivity, and automate tedious analytical tasks. Focused study requires 
disciplined reading habits, clear notes, and structured computational thinking."""

with col1:
    st.subheader("📥 Source Material")
    user_input = st.text_area(
        "Paste your study notes, essay, or textbook snippet below:",
        value=default_text,
        height=280
    )
    
    # Telemetry Calculations
    word_count = len(user_input.split())
    char_count = len(user_input)
    est_reading_time = max(1, round(word_count / 200))  # Standard 200 WPM baseline
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Word Count", word_count)
    m2.metric("Characters", char_count)
    m3.metric("Est. Read Time", f"~{est_reading_time} min")

with col2:
    st.subheader("👁️ Enhanced Bionic View")
    if user_input.strip():
        enhanced_text = apply_bionic_reading(user_input)
        
        # Display formatted text inside a styled focus container
        st.markdown(
            f"""
            <div style="background-color: #1e1e2e; padding: 20px; border-radius: 8px; font-size: 1.15rem; line-height: 1.8; color: #cdd6f4;">
                {enhanced_text}
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.info("Paste or type text on the left to see the enhanced focus view.")

# Integrated Reading Speed Test Tool
st.markdown("---")
st.subheader("⏱️ Speed & Focus Diagnostic Tool")
st.caption("Measure your actual Words Per Minute (WPM) on the enhanced text:")

t_col1, t_col2 = st.columns(2)
with t_col1:
    if st.button("Start Reading Timer", type="primary"):
        st.session_state["start_time"] = time.time()
        st.info("Timer active! Read the text on the right and click Finish when done.")

with t_col2:
    if st.button("Finish Reading"):
        if "start_time" in st.session_state and st.session_state["start_time"] is not None:
            elapsed = time.time() - st.session_state["start_time"]
            wpm = round((word_count / elapsed) * 60) if elapsed > 0 else 0
            st.success(f"Elapsed: **{elapsed:.1f}s** | Speed: **{wpm} Words Per Minute (WPM)**")
            st.session_state["start_time"] = None
        else:
            st.warning("Click 'Start Reading Timer' before finishing.")