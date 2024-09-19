import streamlit as st
import pickle
from PIL import Image


logo = Image.open('logo.PNG')

with open('fake_news_detector_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.sidebar.title('Fake News Detector')
st.sidebar.image(logo)

st.title('Fake News Detector with ML')
st.write("Please, provide the details of the news")

# Create main UI
form = st.form(key='fake-news-detector-form')
row = form.columns(4)

word_count = row[0].text_input('Word Count', value="")
number_of_sentence = row[1].text_input('Number of Sentences', value="")
unique_words = row[2].text_input('Unique Words', value="")
average_word_lenght = row[3].text_input('Average Word Lenght', value="")

submit = form.form_submit_button('Check Fake News')

if submit:
    try:
        prediction = model.predict([[float(word_count), float(number_of_sentence), float(unique_words), float(average_word_lenght)]])
        if prediction[0] == 1:
            st.markdown("## :red[Alert! This might be a fake news!]")
        elif prediction[0] == 0:
            st.markdown("## This may be a valid news")
    except ValueError:
        st.markdown("## :orange[Ensure that you entered valid input and try again]")

   

