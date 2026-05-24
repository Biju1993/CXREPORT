from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os
import streamlit as st
from streamlit.components.v1 import iframe

st.image("https://www.zyeta.com/wp-content/uploads/2024/10/logo-25th-1536x1536-1.png", width=150)
st.title("DB COMMISSIONING REPORT GENERATOR")

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("cx-template (2).html")

form = st.form("template_form")

v1= form.date_input("DATE OF INSPECTION")
v2 = form.text_input("ENTER PROJECT NAME").upper()
v3 = form.text_input("ENTER DISTRIBUTION BOARD NAME").upper()
form.subheader("PHYSICAL CHECKS")
v4= form.radio("PHYSICAL LOCATION OF DISTRIBUTION BOARD IS AS PER DRAWINGS",["YES", "NO","NA"],index=1,horizontal=True)
v5= form.radio("SPECIFICATION OF THE DISTRIBUTION BOARD ARE AS PER DRAWING/TDS",["YES", "NO","NA"],index=1,horizontal=True)
v6= form.radio("DISTRIBUTION BOARD CLEARLY LABELED AS PER DRAWING",["YES", "NO","NA"],index=1,horizontal=True)
form.subheader("DESIGN VERIFICATION")
v7= form.radio("POWER & CIRCUIT WIRING / CABLING AS PER DESIGN ",["YES", "NO","NA"],index=1,horizontal=True)
v8= form.radio("All BREAKERS,SUB BREAKERS,INCOMER BREAKERS RATINGS AS PER APPROVED DRAWINGS",["YES", "NO","NA"],index=1,horizontal=True)
v9= form.radio("SIZE OF THE PHASE,NEUTRAL,EARTHING CABLES IS AS PER DESIGN",["YES", "NO","NA"],index=1,horizontal=True)
v10= form.radio("DB IP RATING IS AS PER DESIGN INTENDED LOCATION",["YES", "NO","NA"],index=1,horizontal=True)
v11= form.radio("ALL THE PANEL INDICATIONS & METERING  IS AS PER THE DESIGN",["YES", "NO","NA"],index=1,horizontal=True)
v12= form.radio("CONTROL CIRCUIT AS PER DESIGN INTENT",["YES", "NO","NA"],index=1,horizontal=True)
form.subheader("INSTALLATION CHECKS")
v13= form.radio("PROPER CONNECTION & TERMINATION OF CABLES DONE",["YES", "NO","NA"],index=1,horizontal=True)
v14= form.radio("MECHANICAL OPERATION OF BREAKERS VERIFIED",["YES", "NO","NA"],index=1,horizontal=True)
v15= form.radio("DISTRIBUTION BOARD DOOR LOCKING ARRANGEMENT VERIFIED",["YES", "NO","NA"],index=1,horizontal=True)
v16= form.radio("CABLE DRESSING & CLAMPING DONE PROPERLY",["YES", "NO","NA"],index=1,horizontal=True)
v17= form.radio("NEUTRAL & EARTHING CONNECTIONS DONE PROPERLY",["YES", "NO","NA"],index=1,horizontal=True)
v18= form.radio("CONNECTION TIGHTNESS VERIFIED WITH A TORQUE WRENCH",["YES", "NO","NA"],index=1,horizontal=True)
v19= form.radio("CABLE FERRULING, CABLE MARKING AND CABLE GLAND EARTHING DONE PROPERLY",["YES", "NO","NA"],index=1,horizontal=True)
form.subheader("FUNCTIONAL CHECKS ")
v20= form.radio("INSULATION RESISTANCE TEST CONDUCTED",["YES", "NO","NA"],index=1,horizontal=True)
v21= form.radio("VOLTAGE CHECKS PHASE TO PHASE/PHASE TO NEUTRAL/NEUTRAL TO EARTH",["YES", "NO","NA"],index=1,horizontal=True)
v22= form.radio("INDICATION LAMPS OPERATION",["YES", "NO","NA"],index=1,horizontal=True)
v23= form.radio("ON / OFF OPERATION OF BREAKER",["YES", "NO","NA"],index=1,horizontal=True)
v24= form.radio("INTERLOCK VERIFIED",["YES", "NO","NA"],index=1,horizontal=True)
v25= form.radio("I/C & O/G CONTINUITY TEST",["YES", "NO","NA"],index=1,horizontal=True)
v26= form.radio("PHASE SEQUENCE VERIFIED",["YES", "NO","NA"],index=1,horizontal=True)
v27= form.radio("METERING ARRANGEMENT VERIFIED FOR ITS OPERATION",["YES", "NO","NA"],index=1,horizontal=True)

submit = form.form_submit_button("GENERATE REPORT")

if submit:
    html = template.render(V1=v1,
V2=v2,
V3=v3,
V4=v4,
V5=v5,
V6=v6,
V7=v7,
V8=v8,
V9=v9,
V10=v10,
V11=v11,
V12=v12,
V13=v13,
V14=v14,
V15=v15,
V16=v16,
V17=v17,
V18=v18,
V19=v19,
V20=v20,
V21=v21,
V22=v22,
V23=v23,
V24=v24,
V25=v25,
V26=v26,
V27=v26
)
    with open("report.html", "w") as f:
        f.write(html)
    f.close()
    st.download_button("⬇️ Download Report",data=html,file_name=v3+".html") 