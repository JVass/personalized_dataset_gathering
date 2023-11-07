import streamlit as st

footer_container = st.container()

with footer_container:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header('Mission')
        st.markdown("<h4> Mission here </h4>", unsafe_allow_html = True)

    with col2:
        st.header("Policies")

        st.header("Support")

    with col3:
        st.header("Contact info")
        st.header("Social media")
