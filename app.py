import streamlit as st
import requests

st.set_page_config(page_title="Jokes")
def fetch_jokes():
    url = "https://hindi-jokes-api.onrender.com/jokes/2?api_key=4d3318833c71fef405cb7604d89c"
    st.balloons()
    response = requests.get(url)
    data = response.json()
    jokes = [i['jokeContent'] for i in data['data']]
    st.title(jokes[0])

def main():
    st.button("Next Jokes")
    
    try:
        fetch_jokes()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()