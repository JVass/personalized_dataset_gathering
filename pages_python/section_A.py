import streamlit as st

tags = ['fast', 'calm', 'slow', 'groovy',
                    'melodic', 'energetic', 'uplifting', 'dance',
                    'party'
                ]

def button_pressed():
    
    st.session_state.change_page = True
    # TODO: add those values to object

def section_A():
    st.markdown("# Section A")

    st.write('In this section see the tag/descriptor located in the top-right corner of the grey boxes and fill those with you description of the respective tag.')
    st.write("Try to focus on describing the sound, timbre, instrumentation, sentiment or anything else that would help someone understand what you're talking about!")

    st.markdown('---')

    with st.container():
        # st.write("First container")
        column_object = st.columns(2)

        text = column_object[0].text_area(
            tags[0],
            "Fill in with your definition."
            )
        st.session_state.user.add_tag_definition(tags[0], text)
        
        text = column_object[1].text_area(
            tags[1],
            "Fill in with your definition.",
            )
        st.session_state.user.add_tag_definition(tags[1], text)

    with st.container():
        # st.write("Second container")
        column_object = st.columns(2)
        text = column_object[0].text_area(
            tags[2],
            "Fill in with your definition.",
            )
        st.session_state.user.add_tag_definition(tags[2], text)
        
        text = column_object[1].text_area(
            tags[3],
            "Fill in with your definition.",
            )
        st.session_state.user.add_tag_definition(tags[3], text)


    with st.container():
        # st.write("Third container")
        column_object = st.columns(2)

        text = column_object[0].text_area(
            tags[4],
            "Fill in with your definition.",
            )
        st.session_state.user.add_tag_definition(tags[4], text)
        
        text = column_object[1].text_area(
            tags[5],
            "Fill in with your definition.",
            )
        st.session_state.user.add_tag_definition(tags[5], text)
    with st.container():
        # st.write("Fourth container")
        column_object = st.columns(2)

        text = column_object[0].text_area(
            tags[6],
            "Fill in with your definition.",
            )
        st.session_state.user.add_tag_definition(tags[6], text)
        
        text = column_object[1].text_area(
            tags[7],
            "Fill in with your definition.",
            )
        st.session_state.user.add_tag_definition(tags[7], text)
    
    st.button(label = "Next page", key = "button_nextpage_section_A", on_click = button_pressed)