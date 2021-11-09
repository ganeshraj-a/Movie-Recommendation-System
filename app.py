import pickle
import streamlit as st
import requests






def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:16]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)


    return recommended_movie_names,recommended_movie_posters




st.title('Movie Recommendation System')

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


movie_list = movies['title'].values
selected_movie = st.sidebar.selectbox(
    "Type a movie from the dropdown",
    movie_list
)

if st.sidebar.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container():
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
    with col2:
        with st.container():
            st.text(recommended_movie_names[5])
            st.image(recommended_movie_posters[5])
            st.text(recommended_movie_names[6])
            st.image(recommended_movie_posters[6])
            st.text(recommended_movie_names[7])
            st.image(recommended_movie_posters[7])
            st.text(recommended_movie_names[8])
            st.image(recommended_movie_posters[8])
            st.text(recommended_movie_names[9])
            st.image(recommended_movie_posters[9])
    with col3:
        with st.container():
            st.text(recommended_movie_names[10])
            st.image(recommended_movie_posters[10])
            st.text(recommended_movie_names[11])
            st.image(recommended_movie_posters[11])
            st.text(recommended_movie_names[12])
            st.image(recommended_movie_posters[12])
            st.text(recommended_movie_names[13])
            st.image(recommended_movie_posters[13])
            st.text(recommended_movie_names[14])
            st.image(recommended_movie_posters[14])



st.sidebar.text('BY GANESHRAJ')
st.sidebar.text('From Artifical Intelligence and Data Science')


