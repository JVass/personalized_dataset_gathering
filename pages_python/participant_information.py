import streamlit as st
import numpy as np

def button_pressed():
    
    st.session_state.change_page = True
    # TODO: add those values to object

def participant_information():

    st.markdown("# Musical related information")

    st.write('In this section we want to ask general questions about you and your contact with music.')
    st.write('Check which of those questions apply to you and use the sliders that will pop up!')

    # Musical instrument practice
    agree = st.checkbox('Are you playing a musical instrument?')

    if agree:
        years_available = list(np.arange(1,11))
        years_available[-1] = "10+"
        music_instrument_experience = st.select_slider('How many years did you practice that instrument?', options = years_available)

        st.session_state.user.musical_experience['instrument_practice_years'] = str(music_instrument_experience)

    # Theoretical training
    agree = st.checkbox('Do you have formal theoretical music training?')

    if agree:
        years_available = list(np.arange(1,11))
        years_available[-1] = "10+"
        theoretical_training_experience = st.select_slider('How many years have you been studying music?', options = years_available)

        st.session_state.user.musical_experience['theoretical_training_years'] = str(theoretical_training_experience)
    # Listening to music
    agree = st.checkbox('Do you usually listen to music in your day?')

    if agree:
        years_available = list(np.arange(6))
        years_available[-1] = "5+"
        hours_per_day_listening_to_music = st.select_slider('How many hours do you usually listen to music per day?', options = years_available)

        st.session_state.user.musical_experience['hours_of_listening_to_music'] = str(hours_per_day_listening_to_music)

    # Playlists?
    agree = st.checkbox('Do you have your go-to songs for different uses (e.g. driving or working out)?')

    st.session_state.user.musical_experience['specific_uses_of_songs'] = agree

    # TODO: store that info to the database

    st.button(label = "Next page", key = "button_nextpage_section_A", on_click = button_pressed)