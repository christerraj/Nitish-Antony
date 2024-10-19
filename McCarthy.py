import streamlit as st
import google.generativeai as genai
GOOGLE_API_KEY = "AIzaSyCrUCzO2suUkeiwLR3NYXG85Erw1X4Zh00"
genai.configure(api_key=GOOGLE_API_KEY)
geminiModel = genai.GenerativeModel("gemini-pro")
chat = geminiModel.start_chat(history=[])
st.title("McCarthy")
prompt = ""
if prompt == "":
    pass
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Do you want to ask me somthing?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
def google():
    global prompt,y
    prompt = st.chat_input("ask something", key="question")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    def get_gemini_response(query):
        instantResponse = chat.send_message(query, stream=False)
        return instantResponse
    if prompt:
        output = get_gemini_response(prompt)
        for outputChunk in output:
            y=outputChunk.text
        st.chat_message('ai').write(y)
    exit()
google()
exit()
