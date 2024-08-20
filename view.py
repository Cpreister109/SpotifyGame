import streamlit as st
from logic import prep_albums

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

st.title('SpotGuess')

artist = st.text_input('What artist would you like to choose?')

if artist:
    albums = prep_albums(artist)
    num_columns = 4
    columns = st.columns(num_columns)

    for i, album in enumerate(albums):

        dupe_albums = [
            "folklore: the long pond studio sessions (from the Disney+ special) [deluxe edition]",
            "reputation Stadium Tour Surprise Song Playlist",
            "1989 (Deluxe Edition)",
            "1989",
            "Red (Deluxe Edition)",
            "Red",
            "Speak Now World Tour Live",
            "Speak Now (Deluxe Edition)",
            "Speak Now",
            "Fearless Platinum Edition",
            "Fearless",
            "Live From Clear Channel Stripped 2008"
        ]

        if album['name'] not in dupe_albums:
            url = album['images'][0]['url']
            print(url)
            name =album['name']
            col = columns[i % num_columns]
            with col:
                with st.container():
                    st.image(url, width=150)
                    st.button(name)
