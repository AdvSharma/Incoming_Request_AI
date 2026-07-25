import streamlit as st
from classifier import classify_request
from workflow import process_workflow
from generator import generate_response
from database import init_db, save_request

st.set_page_config(
    page_title="Incoming Request Processor",
    page_icon="📨",
    layout="wide"
)

init_db()

st.title("📨 Incoming Request Processing Workflow")

request = st.text_area(
    "Incoming Customer Request",
    height=220
)

if st.button("Process Request"):

    if request.strip() == "":
        st.warning("Enter a request.")

    else:

        with st.spinner("AI is analysing..."):

            result = classify_request(request)
            workflow = process_workflow(result)
            save_request(
                workflow["case_id"],
                request,
                result,
                workflow
            )

            reply = generate_response(request, result)

        st.success("Classification Complete")

        c1, c2, c3 = st.columns(3)

        c1.metric("Request Type", result["type"])
        c2.metric("Urgency", result["urgency"])
        c3.metric("Confidence", f"{result['confidence']:.0%}")

        if result["urgency"] == "High":
            st.error("🔴 High Priority Request")

        elif result["urgency"] == "Medium":
            st.warning("🟡 Medium Priority Request")

        else:
            st.success("🟢 Low Priority Request")

        st.subheader("🧠 AI Reasoning")

        st.write(result["reason"])

        st.divider()

        st.subheader("⚙️ Workflow Execution")

        st.write("**Case ID:**", workflow["case_id"])

        st.write("**Department:**", workflow["department"])

        st.write("**Timestamp:**", workflow["timestamp"])

        st.write("### Automated Actions")

        for action in workflow["actions"]:
            st.success(action)

        st.divider()

        st.subheader("📧 AI Generated Customer Reply")

        with st.expander("Click to view the generated email"):
            st.info(reply)

        st.divider()

        st.caption(
            "Incoming Request Processing Workflow • Agentic AI Engineer POC • Powered by Gemini 3.6 Flash"
        )