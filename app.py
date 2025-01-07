import pickle
import streamlit as st
import requests
import base64

# Function to fetch the movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to set a local background image
def set_background(image_path):
    """Set a background image in the Streamlit app."""
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()
    background_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        filter: blur(0px);

    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

# Function to style the title
# Function to style the title
# Function to style the title
# Function to style the title inside a box
# Function to style the title inside a box with animation and gradient
# Function to style the title inside a sleek box with smooth animation
# Function to style the title in one line
def style_title():
    title_css = """
    <style>
    .title-box {
        background-color: #F39C12; /* Dark background color */
        color: #FFFFFF; /* Light text color */
        text-align: center;
        font-family: 'Lobster', cursive; /* Sleek sans-serif font */
        font-size: 50px; /* Larger text size */
        font-weight: 600; /* Semi-bold font */
        padding: 20px 20px; /* Padding for spacious look */
        margin: 30px auto; /* Center the title */
        border-radius: 15px; /* Rounded corners */
        width: 100%; /* Box width */
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.4); /* Smooth shadow */
        letter-spacing: 2px; /* Slight letter spacing */
        text-transform: uppercase; /* Uppercase letters */
        white-space: nowrap; /* Prevent text wrapping */
        animation: fadeIn 2s ease-in-out; /* Smooth fade-in effect */
    }

    /* Keyframes for fade-in animation */
    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
    </style>
    <div class="title-box">Watch With Raghav</div>
    """
    st.markdown(title_css, unsafe_allow_html=True)


# Set the background image (update the path to your local image)
set_background(r"shubham.jpg")

# Display the styled title
style_title()

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Load the movie dataset and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown to select a movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Show recommendations when the button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Display the recommendations in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
