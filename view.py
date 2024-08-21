import streamlit as st
from logic import prep_albums, display_albums

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

st.title('SpotGuess')

artist = st.text_input('What artist would you like to choose?')

if artist:
    albums, dupe_albums = prep_albums(artist)
    num_columns = 4
    columns = st.columns(num_columns)

    display_albums(albums, dupe_albums, num_columns, columns)
