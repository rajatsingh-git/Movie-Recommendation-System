import pickle
import pandas as pd
import streamlit as st

# Load the data
data = pickle.load(open('movie_dict.pkl', mode='rb'))
data = pd.DataFrame(data)

# Load the Similarity Score
similarity = pickle.load(open('similarity.pkl', mode='rb'))

# Recommendation function
def recommend(movie):
    recommended_movies = []
    try:
        # Get the index of the selected movie
        movie_index = data[data['title'] == movie].index[0]
        distance = similarity[movie_index]
        
        # Sort by similarity scores
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
        
        # Fetch movie titles
        for i in movie_list:
            recommended_movies.append(data.iloc[i[0]]['title'])
        
        return recommended_movies
    except Exception as e:
        return [f"An error occurred: {e}"]

# Streamlit Web-App
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #2F80ED;
        text-align: center;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 20px;
        color: #333333;
        text-align: center;
        margin-top: 0;
        margin-bottom: 30px;
    }
    .recommendation-box {
        background: #333333;
        border: 1px solid #EAEAEA;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title Section
st.markdown("<h1 class='main-title'>🎥 Movie Recommendation System 🍿</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your next favorite movie is just a click away!</p>", unsafe_allow_html=True)

# Layout with Columns
col1, col2 = st.columns(2)

with col1:
    # Dropdown to select a movie
    st.markdown("### 🎬 Choose a Movie:")
    movie_list = data['title'].tolist()
    selected_movie = st.selectbox("", movie_list)




# Recommendation Button
if st.button("🎯 Get Recommendations!"):
    recommendations = recommend(selected_movie)

    # Display Recommendations in a Pretty Box
    if recommendations:
        st.markdown("### 🌟 Recommended Movies:")
        for idx, movie in enumerate(recommendations, start=1):
            st.markdown(
                f"""
                <div class='recommendation-box'>
                <h4>🎥 {idx}. {movie}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.error("No recommendations found. Please try another movie.")

# Footer Section
st.markdown("---")
st.markdown(
    """
    
    """,
    unsafe_allow_html=True
)
