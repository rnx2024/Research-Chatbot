import streamlit as st
from openai import OpenAI

# Secure API Key from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(page_title="AI Research Assistant", page_icon="🧠")
st.title("🧠 AI Research Assistant")
st.markdown("Powered by OpenAI | BEST AI Team | v2.0 | June 2025")

# === Step 1: Persona Selector ===
persona = st.selectbox(
    "Choose Assistant Persona:",
    options=[
        "🧰 General AI Discovery Assistant",
        "📊 ABA-Centered Strategic AI Researcher"
    ],
    index=0
)

# === Step 2: System Prompt Generator ===
def get_system_prompt(persona_choice):
    if "General" in persona_choice:
        return (
            "You are an advanced AI Research Assistant specializing in discovering and recommending:\n"
            "- ✅ Useful AI and automation tools with pricing info (Free, Paid, Trial)\n"
            "- 🎥 High-quality tutorials from YouTube/Vimeo/etc.\n"
            "- 📰 Trending articles on AI/automation\n"
            "- 🎓 AI/ML courses from Coursera, edX, Udemy, etc.\n"
            "- 🧪 Experimental or beta-stage tools\n\n"
            "Always include:\n"
            "- Brief description\n"
            "- Link (if available)\n"
            "- Price tag (Free, Paid, Trial)\n\n"
            "Be current (2024–2025), concise, and helpful."
        )
    else:
        return (
            "You are a strategic AI research expert embedded in an ABA services company. You:\n"
            "- Ask the user what problem they are trying to solve\n"
            "- Recommend specific AI tools, platforms, and automation\n"
            "- Provide structured guidance, including:\n"
            "   • Business use case overview\n"
            "   • Tool/platform recommendation\n"
            "   • How to implement it (step-by-step)\n"
            "   • Integration strategy within a company\n"
            "- Suggest strategies to apply AI across different business units in ABA\n\n"
            "Always respond in a structured and professional tone, tailored for competitive advantage."
        )

# === Step 3: Session State Setup ===
if "messages" not in st.session_state or st.session_state.get("active_persona") != persona:
    st.session_state.messages = [
        {"role": "system", "content": get_system_prompt(persona)}
    ]
    st.session_state.active_persona = persona

# === Step 4: Display Chat History ===
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# === Step 5: Chat Input and GPT-4 Streaming Response ===
if prompt := st.chat_input("Ask your research question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Stream response from OpenAI
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages,
        stream=True
    )

    full_response = ""
    with st.chat_message("assistant"):
        response_container = st.empty()
        for chunk in stream:
            if chunk.choices[0].delta.get("content"):
                token = chunk.choices[0].delta.content
                full_response += token
                response_container.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
