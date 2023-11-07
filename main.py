import streamlit as st
import random
import os
from functions import *
import uuid
from PIL import Image

from pages_python.introduction import introduction
from pages_python.section_A import section_A
from pages_python.section_B import section_B
from pages_python.participant_information import participant_information

import pymongo
from datetime import datetime

from streamlit_javascript import st_javascript

def client_ip():

    url = 'https://api.ipify.org?format=json'

    script = (f'await fetch("{url}").then('
                'function(response) {'
                    'return response.json();'
                '})')

    try:
        result = st_javascript(script)

        if isinstance(result, dict) and 'ip' in result:
            return result['ip']

    except:
        pass

# ------------- GLOBAL VARS ----------------
available_tags = ['Metal', 'Hip Hop', 'Reggae', 'Pop',
                    'Jazz', 'Disco', 'Blues', 'Country',
                    'Indian', 'Classical', 'Electronic', 'Rock']
    
MONGO_IP = "localhost"
MONGO_PORT = "27017"
MONGO_PATH = "mongodb://" + MONGO_IP + ":" + MONGO_PORT

# ------------- FUNCTIONS ------------------

def fetch_song_titles(path_to_songs):
    song_titles = os.listdir(path_to_songs)

    return [path_to_songs + "/" + x for x in song_titles]

def update_current_page(current_page_string):
    if current_page_string == "initialization":
        return "giving_consent"
    elif current_page_string == "introduction":
        return "participant_information"
    elif current_page_string == "participant_information":
        return "section_A"
    elif current_page_string == "section_A":
        return "section_B"
    elif current_page_string == "section_B":
        return "ending_credits"

def button_pressed():
    st.session_state.button_pressed = True

def giving_consent():
    st.markdown("## Welcome to 'Dataset for Personalized Tags' !")

    st.write("In order to proceed with the experiment, read carefully the following text.")

    st.markdown('### DATA FAIR USE AND GDPR COMPLIANCE')
    
    st.write("Then, click on the checkbox ('I consent') and press the 'Next page' button!")

    consent_given = st.checkbox('I give consent', key = "checkbox_0")

    if st.session_state['checkbox_0'] == True:
        st.session_state.consent_given = True
        button = st.button(label = "Next page", key = 0, on_click = button_pressed())

    if st.session_state.button_pressed == True:
        st.session_state.current_page = "introduction"

def ending_credits():
    st.write("This is the ending credits page")

    st.write("Compensation link maybe? Let's get some QM money readyyy")

st.set_page_config(layout="centered")


# # ------------------- MAIN -----------------------------
# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "initialization"
if 'button_pressed' not in st.session_state:
    st.session_state.button_pressed = False
if 'consent_given' not in st.session_state:
    st.session_state.consent_given = False
if 'change_page' not in st.session_state:
    st.session_state.change_page = False
if 'songs_to_test' not in st.session_state:
    st.session_state.songs_to_test = []
if "current_song_to_test" not in st.session_state:
    st.session_state.current_song_to_test = ""
    st.session_state.songs_to_test = fetch_song_titles('./songs')
    random.shuffle(st.session_state.songs_to_test)
    st.session_state.number_of_tests = len(st.session_state.songs_to_test)
if 'songs_annotated' not in st.session_state:
    st.session_state.songs_annotated = 0
if 'uuid' not in st.session_state:
    st.session_state.uuid = str(uuid.uuid4())
if 'db_connected' not in st.session_state:
    st.session_state.db_connected = False
if 'session_starting_time' not in st.session_state:
    st.session_state.session_starting_time = datetime.now()
if 'user' not in st.session_state:
    st.session_state.user = User()

main_container = st.container()


with main_container:

    if st.session_state.current_page == "initialization":
        try:
            client = pymongo.MongoClient(MONGO_PATH,
                                            serverSelectionTimeoutMS=2)
            client.server_info() 

        except pymongo.errors.ServerSelectionTimeoutError as err:
            print("DATABASE CONNECTION ERROR")
            st.write('Problem connecting with the database. Please restart...')
        else:
            st.session_state.db_connected = True
            st.session_state.current_page = "giving_consent"
            st.session_state.db = client['personalized_dataset']

        db = client['personalized_dataset']
        collection = db['participants']

        # Check if uuid and starting time exists
        uuid_datatime_combo_exists = False

        while not(uuid_datatime_combo_exists):
            if collection.find_one({'uuid': st.session_state.uuid, 'starting_time': st.session_state.session_starting_time}) is None:
                print(f"Creating user object with uuid: {st.session_state.uuid} and starting time: {st.session_state.session_starting_time}")
                st.session_state.uuid = str(uuid.uuid4())
                st.session_state.session_starting_time = datetime.now()

                st.session_state.user.starting_time = st.session_state.session_starting_time
                st.session_state.user.uuid = st.session_state.uuid

                uuid_datatime_combo_exists = True

    if st.session_state.current_page == "giving_consent" and st.session_state.db_connected == True:
        giving_consent()
        
    elif st.session_state.consent_given == True and st.session_state.db_connected == True:

        if st.session_state.change_page:
            st.session_state.current_page = update_current_page(st.session_state.current_page)
            st.session_state.change_page = False

        if st.session_state.current_page == "introduction":
            introduction(available_tags)

        elif st.session_state.current_page == "participant_information":
            participant_information()

        elif st.session_state.current_page == "section_A":
            section_A()

        elif st.session_state.current_page == "section_B":
            if len(st.session_state.current_song_to_test) == 0:
                st.session_state.current_song_to_test = st.session_state.songs_to_test.pop()

            section_B(st.session_state.current_song_to_test, available_tags)

        elif st.session_state.current_page == "ending_credits":
            st.session_state.user.end_time = datetime.now()


            print(st.session_state.user.jsonify_data())

            st.session_state.db['participants'].insert_one(st.session_state.user.jsonify_data())

            # Get to ending credits

            ending_credits()

st.markdown("---")

footer_container = st.container()

# ------------------- FOOTER -----------------------------

with footer_container:
    images_container = st.container()

    with images_container:
        col1, col2, col3 = st.columns(3)

        with col1:
            image = Image.open("images/UKRI-Logo_Horiz-RGB.png")
            st.image(image)

        with col2:
            image = Image.open("images/Asset_92x_4_45.webp")
            st.image(image)

        with col3:
            image = Image.open("images/queen_mary_logo.jpg")
            st.image(image)

    captions_container = st.container()

    with captions_container:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("This work was supported by ")
            st.write("UK Research and Innovation ")
            st.write("[grant number EP/S022694/1]")

        with col2:
            st.write("Artificial Intelligence and Music")

        with col3:
            st.write("Queen Mary University of London")