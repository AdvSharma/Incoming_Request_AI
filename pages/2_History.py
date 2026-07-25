import streamlit as st
import pandas as pd

from database import get_requests

st.set_page_config(
    page_title="Request History",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Incoming Request History")

rows = get_requests()

if len(rows) == 0:
    st.info("No requests found.")
    st.stop()

df = pd.DataFrame(rows)

df.columns = [
    "id",
    "case_id",
    "request",
    "type",
    "urgency",
    "confidence",
    "department",
    "timestamp"
]


total = len(df)
complaints = len(df[df["type"] == "Complaint"])
services = len(df[df["type"] == "Service Request"])
enquiries = len(df[df["type"] == "General Enquiry"])

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Requests", total)
c2.metric("Complaints", complaints)
c3.metric("Service Requests", services)
c4.metric("General Enquiries", enquiries)

st.divider()

st.subheader("Request History")

st.dataframe(
    df[
        [
            "case_id",
            "type",
            "urgency",
            "department",
            "timestamp"
        ]
    ],
    use_container_width=True
)

csv = df.to_csv(index=False)

st.download_button(
    "📥 Download CSV",
    csv,
    "request_history.csv",
    "text/csv"
)