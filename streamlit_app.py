import streamlit as st
from openai import OpenAI

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

# OpenAI Key input
openai_api_key = st.text_input("🔐 Enter your OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    client = OpenAI(api_key=openai_api_key)

    # Initialize system message with clear instructions for the assistant role
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": (
                    "You are an advanced AI Research Assistant specializing in discovering and recommending:"
                    "\n\n✅ Useful AI and automation tools, with clear labels (Free, Paid, Trial)"
                    "\n🎥 Recent high-quality video tutorials (YouTube, Vimeo, etc.)"
                    "\n📰 Recent or trending articles on AI and automation"
                    "\n🎓 Free and paid courses for AI and machine learning (Coursera, edX, Udemy, etc.)"
                    "\n🧪 Experimental, open-source, or beta-stage tools"
                    "\n\nFor each resource, where possible, include:"
                    "\n- A brief description"
                    "\n- A link (if available)"
                    "\n- Whether it’s Free, Paid, or Free Trial"
                    "\n\nStay current with trends from 2024–2025. Be concise, highly useful, and cite known platforms when relevant."
                )
            }
        ]

    # Show prior chat history
    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Prompt input from user
    if prompt := st.chat_input("Ask for tools, videos, free courses, or automation help..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # GPT Response (streamed)
        stream = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages,
            stream=True
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)

        st.session_state.messages.append({"role": "assistant", "content": response})
