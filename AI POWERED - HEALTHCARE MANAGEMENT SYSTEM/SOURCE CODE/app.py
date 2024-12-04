import streamlit as st
from app.login import login_page
from app.super_admin import super_admin_page
from app.dashboard import dashboard_page
from app.data_collection import data_collection_page
from app.report_control import report_control_page
from app.smart_appointment import smart_appointment_page
from app.doctor_dashboard import doctor_dashboard_page
from app.patient_portal import patient_portal_page
from app.dashboard import dashboard_page

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        st.sidebar.title("Navigation")
        selection = st.sidebar.selectbox("Go to", [
            "Dashboard",
            "Data Collection",
            "Report Control",
            "Smart Appointment",
            "Doctor Dashboard",
            "Patient Portal"
        ])
        if selection == "Dashboard":
            dashboard_page()
        elif selection == "Data Collection":
            data_collection_page()
        elif selection == "Report Control":
            report_control_page()
        elif selection == "Smart Appointment":
            smart_appointment_page()
        elif selection == "Doctor Dashboard":
            doctor_dashboard_page()
        elif selection == "Patient Portal":
            patient_portal_page()
    else:
        st.sidebar.title("Navigation")
        selection = st.sidebar.selectbox("Go to", ["Super Admin Page", "Admin Login"])
        if selection == "Super Admin Page":
            super_admin_page()
        elif selection == "Admin Login":
            login_page()

if __name__ == "__main__":
    main()
