# 🧠 AI Research Assistant Chatbot (customized from Streamlit Chatbot)

This Streamlit app is an AI-powered research assistant that helps users discover:

- ✅ The latest **AI and automation tools**
- 🎥 High-quality **video tutorials** and **YouTube channels**
- 📰 **Trending articles** on AI and tech
- 🎓 Top **free and paid courses** (e.g., Coursera, Udemy)
- 🧪 **Experimental and open-source tools**

Simply ask a question — the assistant uses GPT-4 to deliver concise, curated insights.

---

## 📸 Preview

![Screenshot](https://github.com/rnx2024/chatbot/raw/main/screenshots/Screenshot%202025-06-05%20040425.png)

---

## 🔧 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant
2. Add your API key via Streamlit Secrets
Create a file at .streamlit/secrets.toml:


[openai]
api_key = "sk-...your-openai-key..."

If you're using Streamlit Cloud, add your secret directly via the Secrets Manager in the dashboard.

3. Install requirements

pip install -r requirements.txt
4. Run the app

🧠 How It Works
Uses OpenAI's GPT-4 via the openai Python SDK.
Maintains chat history using st.session_state.
Custom CSS styling adds a light green border around the input area.
Includes a system prompt to guide GPT's response style and topics.

🖥️ File Structure
.
├── streamlit_app.py           # Main Streamlit chatbot app
├── .streamlit/
│   └── secrets.toml          # Secure API key storage
├── requirements.txt          # Dependencies
├── screenshots
│   └── Screenshot202025.png  # App Screenshot        
└── README.md

✨ Custom Features
✅ Italicized name/credit line under the title
✅ Chat input box with light green border
✅ Real-time streaming of GPT responses
✅ Clean and simple UI for casual users or researchers

🧑‍💻 Credit
Enhanced and Customized by Rhanny_AITeam

📜 License
MIT

---







