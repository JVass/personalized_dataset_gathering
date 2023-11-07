import streamlit as st

def button_pressed():
    st.session_state.songs_annotated += 1
    if st.session_state.songs_to_test:
        st.session_state.current_song_to_test = st.session_state.songs_to_test.pop()

        # TODO: UPDATE THE DATABASE FOR THE USER
    else:
        st.session_state.change_page = True

def section_B(song_to_test, tags):
    st.markdown("# Section B")

    percentage_of_progression = st.session_state.songs_annotated / st.session_state.number_of_tests

    st.progress(percentage_of_progression, f'Finished with {percentage_of_progression*100:.2f}%')

    audio_file = open(song_to_test, 'rb')
    audio_bytes = audio_file.read()

    st.write('Listen to this excerpt from a song:')
    st.audio(audio_bytes, format = 'wav')

    st.markdown('---')

    checkbox_values = []

    st.write('Which of the following tags best describe this song? (Select all that apply)')
    for i in range(len(tags)):
        value = st.checkbox(tags[i], key = f'{tags[i]}_{len(st.session_state.songs_to_test)}')
        checkbox_values.append(value)

    st.session_state.user.add_annotation(song_to_test, checkbox_values)
    
    st.button(label = "Next page", key = "button_nextpage_section_A", on_click = button_pressed)