import streamlit as st
from openai import OpenAI

# Load API key from secrets
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(page_title="AI Research Assistant", page_icon="🧠")
st.title("🧠 AI Research Assistant")
page_icon="ai.png" 

# Byline under title
st.markdown(
    "<div style='font-size: 12px; color: gray;'>Powered by OpenAI | BEST AI Team | v1.0 | June 2025</div>",
    unsafe_allow_html=True
)

# Persona selector
persona = st.selectbox(
    "Choose Assistant Persona:",
    [
        "🧰 General AI Discovery Assistant",
        "📊 ABA-Centered Strategic AI Researcher"
    ],
    index=0
)

# Define persona-specific system prompts
def get_system_prompt(selected):
    if "General" in selected:
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
            "- Recommend specific AI tools, platforms, and automation\n processes - starting from the most simple no-code solution, to possible agent or customGPT development."
            "- Provide structured guidance, including:\n"
            "   • Business use case overview\n"
            "   • Tool/platform recommendation\n"
            "   • How to implement it (step-by-step)\n"
            "   • Integration strategy within a company\n"
            "- Suggest strategies to apply AI across different business units in ABA\n\n"
            "Always respond in a structured and professional tone, tailored for competitive advantage."
        )

# Reset system prompt if persona changed
if "messages" not in st.session_state or st.session_state.get("active_persona") != persona:
    st.session_state.messages = [
        {"role": "system", "content": get_system_prompt(persona)}
    ]
    st.session_state.active_persona = persona

# Display message history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Prompt input
# Chat input and GPT response
if prompt := st.chat_input("Ask for tools, videos, free courses, or automation help..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages,
        stream=True
    )

    with st.chat_message("assistant"):
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
