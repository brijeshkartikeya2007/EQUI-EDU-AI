import streamlit as st
from orchestrator_agent import OrchestratorAgent

st.set_page_config(page_title="EQUI EDU AI Demo", layout="centered")
st.title("EQUI EDU AI – Capstone Demo")

if 'history' not in st.session_state:
    st.session_state['history'] = []

orchestrator = OrchestratorAgent()

with st.form("ai_input_form"):
    learner = st.text_input("Learner's Name", "")
    topic = st.text_input("What do you want to learn? (e.g., Photosynthesis)")
    style = st.selectbox("How do you want the explanation?", ["simple", "visual", "detailed"])
    accessibility = st.selectbox("Accessibility need?", ["none", "dyslexia", "audio"])
    gender = st.selectbox("Gender", ["female", "male", "other"])
    SES = st.selectbox("Socioeconomic status (SES)", ["high", "mid", "low"])
    intent = st.radio("Request:", ["content", "assessment"])
    submit = st.form_submit_button("Get AI Learning Help!")

if submit:
    context = {
        "learner": learner,
        "topic": topic,
        "style": style,
        "accessibility": accessibility,
        "demographics": {"gender": gender, "SES": SES}
    }
    resp = orchestrator.handle_request(intent, context)
    st.session_state['history'].append((context, resp))
    st.success("AI Response:\n" + resp)

if st.session_state['history']:
    st.markdown("---")
    st.header("Session Memory (History)")
    for idx, (ctx, r) in enumerate(reversed(st.session_state['history'][-5:])):
        st.markdown(f"**#{len(st.session_state['history'])-idx}**  \n*Input:* {ctx}  \n*Output:* {r}")

st.info("This demo shows a multi-agent orchestrator, real agent simulation, accessibility/fairness checks, and session memory. For capstone or YouTube, do a live walkthrough!")
