from datetime import datetime
import uuid


def process_workflow(result):

    request_type = result["type"]

    case_id = "CASE-" + str(uuid.uuid4())[:8].upper()

    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    workflow = {
        "case_id": case_id,
        "timestamp": timestamp,
        "department": "",
        "actions": []
    }

    if request_type == "Complaint":

        workflow["department"] = "Customer Support"

        workflow["actions"] = [
            "Complaint Registered",
            "Priority Escalation",
            "Acknowledgement Email",
            "Follow-up Scheduled"
        ]

    elif request_type == "Service Request":

        workflow["department"] = "Operations"

        workflow["actions"] = [
            "Service Request Logged",
            "Assigned to Operations",
            "SLA Started",
            "Confirmation Email"
        ]

    else:

        workflow["department"] = "Customer Care"

        workflow["actions"] = [
            "Enquiry Logged",
            "Response Generated",
            "Case Closed"
        ]

    return workflow