import streamlit as st
import pandas as pd
import numpy as np

def button_pressed():
    st.session_state.change_page = True

def introduction(tags):
    st.markdown("# General information")
    
    st.markdown('### Greetings')
    st.write("Do you know what a 'happy' song means? Do you think that this is what experts think about that term?")
    st.write("Didn't you have endless fights for the genre a song belongs to?")
    st.write("If yes and with your aid, we aim at solving that once and for all!")

    st.markdown('### Scope')
    st.write('Tags have been very effective for information retrieval. Despite their success, the "meaning" of those words (or phrases) are hypothesized to be objective and constant.')
    st.write('While there is some truth in the objectivity of certain words, this questionnaire will try to test that assumption!')

    st.markdown('---')
    st.markdown("## Description of experiment")
    st.write("The gathering process consists of three sections. Their names and descriptions are provided below.")

    st.markdown('### Section about musical experience')
    st.write('In this section, you will be asked about your musical background, as well as questions about the place music has in your life.')
    
    st.markdown('### Section A')
    st.write('In this section, you will be asked to fill in your definition of specific words/phrases that are used as tags in modern Automatic Music Tagging Systems.')
    st.write('Those words will be given on the top right corner of a grey section, where you can freely insert your description.')

    st.write("**REMEMBER**: Try to focus on describing the sound, timbre, instrumentation, sentiment or anything else that would help someone understand what you're talking about!")

    st.markdown('## PREFILLED EXAMPLE')

    with st.container():
        txt = st.text_area(
            "dance",
            "It's a genre that heavily relies on electronic production techniques, and it's all about crafting beats, melodies, and textures that can make people move on the dance floor. One key feature is the emphasis on rhythmic elements. Melodically, ou can have catchy, uplifting hooks or more atmospheric, mood-setting tones. Synthesizers are like the paintbrushes, allowing musicians to create a wide spectrum of sounds, from lush pads to sharp leads that cut through the mix.",
            )


    st.markdown('---')

    st.markdown('### Section B')
    st.write('In this section, we want you to choose from a dropdown menu all the tags that you find relative to the specific music that you will hear.')
    st.markdown('**REMEMBER**: Try to remember the definition you gave and choose based on that, as well as your general "feeling"!')

    st.markdown('## PREFILLED EXAMPLE')

    with st.container():
        st.write('Listen to this excerpt from a song:')

        # place song here
        path_to_song = 'songs/15.mp3'

        audio_file = open(path_to_song, 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='wav')

        st.write('Which of the following tags best describe this song? (Select all that apply)')
        for i in range(len(tags)):
            st.checkbox(tags[i])

    button = st.button(label = "Next page", key = "button_nextpage_introduction", on_click = button_pressed)


    