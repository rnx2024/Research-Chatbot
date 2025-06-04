import streamlit as st
from openai import OpenAI

# Use OpenAI key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(page_title="AI Research Assistant", page_icon="🧠")
st.title("🧠 AI Research Assistant")
st.write("""
This assistant helps you discover:
- The latest **AI & automation tools**
- **Free, paid, or trial** versions of platforms
- Curated **video tutorials** and **YouTube channels**
- Top **free courses** in AI/Machine Learning
- **Newest articles** and experimental apps worth tracking

Just ask a question and get a research-grade response.
""")

# System role and conversation history setup
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are an advanced AI Research Assistant specializing in discovering and recommending:\n"
                "- ✅ Useful AI and automation tools, with clear labels (Free, Paid, Trial)\n"
                "- 🎥 High-quality recent video tutorials (YouTube, Vimeo, etc.)\n"
                "- 📰 Trending articles on AI/automation\n"
                "- 🎓 Free/paid AI & ML courses (Coursera, edX, Udemy, etc.)\n"
                "- 🧪 Experimental, open-source, or beta-stage tools\n\n"
                "For each resource, include:\n"
                "- A short description\n"
                "- A link if available\n"
                "- Whether it’s Free, Paid, or Free Trial\n\n"
                "Stay up to date with trends from 2024–2025. Be concise, useful, and cite platforms when relevant."
            )
        }
    ]

# Display prior messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

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
