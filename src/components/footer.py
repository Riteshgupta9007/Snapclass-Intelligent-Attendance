import streamlit as st
import base64

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def footer_home():
    img = get_base64("assets/logo.jpeg")

    st.markdown(f"""
        <div style="
            margin-top:2rem;
            display:flex;
            justify-content:center;
            align-items:center;
            gap:10px;
        ">
            <p style="font-weight:bold; color:white; margin:0;">
                Created with ❤️ by
            </p>
            <img src="data:image/jpeg;base64,{img}" style="height:40px;" />
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    img = get_base64("assets/logo.jpeg")

    st.markdown(f"""
        <div style="
            margin-top:2rem;
            display:flex;
            justify-content:center;
            align-items:center;
            gap:10px;
        ">
            <p style="font-weight:bold; color:black; margin:0;">
                Created with ❤️ by
            </p>
            <img src="data:image/jpeg;base64,{img}" style="height:40px;" />
        </div>
    """, unsafe_allow_html=True)

