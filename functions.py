import streamlit as st

def change_current_page(current_value):
    if current_value == "giving_consent":
        st.session_state.currentPage = "introduction"
    elif current_value == "introduction":
        st.session_state.currentPage = "section_A"
    elif current_value == "section_A":
        st.session_state.currentPage = "section_B"
    elif current_value == "section_B":
        st.session_state.currentPage = "ending_credits"


def button_pressed():
    st.session_state.button_pressed = True

class User:
    def __init__(self):
        self.starting_time = -1
        self.end_time = -1
        self.uuid = ""
        self.musical_experience = {
            "instrument_practice_years": -1,
            "theoretical_training_years": -1,
            "hours_of_listening_to_music": -1,
            "specific_uses_of_songs": False
        }
        self.textual_definitions = {}
        self.song_annotations = {}

    def show_musical_experience(self):
        print(self.musical_experience)
    def show_tag_definitions(self):
        print(self.textual_definitions)
    def show_annotations(self):
        print(self.song_annotations)

    def add_tag_definition(self, tag_name, definition_string):
        self.textual_definitions[tag_name] = definition_string

    def add_annotation(self, song_name, tag_list):
        self.song_annotations[song_name] = tag_list

    def check_for_validity(self):
        pass

    def jsonify_data(self):
        json_to_save = {}

        json_to_save["starting_time"] = self.starting_time
        json_to_save["end_time"] = self.end_time
        json_to_save["self.uuid"] = self.uuid
        json_to_save["musical_experience"] = self.musical_experience
        json_to_save["textual_definitions"] = self.textual_definitions
        json_to_save["song_annotations"] = self.song_annotations

        return json_to_save

