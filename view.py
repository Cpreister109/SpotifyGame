import streamlit as st
from logic import prep_albums

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

st.title('SpotGuess')

artist = st.text_input('What artist would you like to choose?')

if artist:
    albums, dupe_albums = prep_albums(artist)
    num_columns = 4
    columns = st.columns(num_columns)

    for i, album in enumerate(albums):   
        if album['name'] not in dupe_albums:
            url = album['images'][0]['url']
            print(url)
            name =album['name']
            col = columns[i % num_columns]
            with col:
                with st.container():
                    st.image(url, width=150)
                    st.button(name)
