import re
import random
import streamlit as st

# --- Rule-Based Chatbot Class ---
class RuleBasedChatBot:
    def __init__(self, rules):
        self.rules = rules

    def get_response(self, message):
        message = message.lower()
        for rule in self.rules:
            for pattern in rule['patterns']:
                if re.search(pattern, message):
                    return random.choice(rule['responses'])
        return "🤷 I'm not sure how to respond to that."

# --- Initialize Rules in Session State ---
if "rules" not in st.session_state:
    st.session_state.rules = [
        {
            'patterns': [r'hello|hi|hey|greetings', r'^hi$'],
            'responses': [
                "👋 Hello! How can I help you today?",
                "👋 Hi there! What can I assist you with?",
                "👋 Hey! I'm here to help. What's on your mind?"
            ]
        },
        {
            'patterns': [r'who are you|what are you|tell me about yourself'],
            'responses': [
                "🤖 I'm an advanced AI assistant created by Vinayak Madgundi. I combine rule-based capabilities with AI to provide helpful responses to your questions!"
            ]
        },
        # ... (Include all rules you listed here — they've been truncated for brevity)
        {
            'patterns': [r'(what|how) about blockchain'],
            'responses': [
                "🔗 Blockchain is a distributed ledger technology that records transactions across many computers so no record can be altered retroactively. It enables secure, transparent systems without central authorities and powers cryptocurrencies like Bitcoin, plus applications in supply chain, voting systems, and digital identity verification."
            ]
        }
    ]

# --- Streamlit App Layout ---
st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="centered")
st.title("💬 Rule based Chatbot by Vinayak Madgundi")
st.markdown("Ask me anything about AI, tech, or just for fun!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

bot = RuleBasedChatBot(st.session_state.rules)

# User Input Box
with st.form("chat_input", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    response = bot.get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display Chat History with Basic Styling
for sender, message in st.session_state.chat_history:
    align = "flex-end" if sender == "You" else "flex-start"
    bg_color = "rgb(26, 28, 36)" if sender == "You" else "rgb(26, 28, 36)"
    st.markdown(
        f"""
        <div style='display: flex; justify-content: {align}; margin-bottom: 10px;'>
            <div style='background-color: {bg_color}; padding: 10px 15px; border-radius: 12px; max-width: 80%;'>
                <b>{sender}:</b> {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
