import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import base64
import os
import cv2


@st.cache_resource
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_resource
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code
pg_bg_gradient = """

<style>
[class="main css-uf99v8 egzxvld5"]{
background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);
}
</style>

"""

#background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);
#background-image: radial-gradient(circle, rgba(211,170,245,0.966999299719888) 0%, rgba(15,2,37,0.9810049019607843) 95%);
# [class="css-1kyxreq etr89bj2"] img {
#   width: 100%;
#   height: 100%;
#   transition: transform 0.75s ease-in-out;
#   transform-style: preserve-3d;
# }
# [class="css-1kyxreq etr89bj2"]:hover img {
#   transform: rotateY(180deg);
# }

#st-bv st-bw st-b6 st-b5 st-ar st-as st-bx st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-c5 st-c6 st-c7 st-c8 st-c9 st-ca st-cb st-cu st-cd st-ce st-b1 st-cf st-cg st-ch st-ci st-cj st-ck st-cl st-cm st-ae st-cn st-ag st-ah st-ai st-aj st-co st-cp st-cq st-cr st-cs st-ct
#st-bv st-bw st-b6 st-b5 st-ar st-as st-bx st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-c5 st-c6 st-c7 st-c8 st-c9 st-ca st-cb st-cu st-cd st-ce st-b1 st-cf st-cg st-ch st-ci st-cj st-ck st-cl st-cm st-ae st-cn st-ag st-ah st-ai st-aj st-co st-cp st-cq st-cr st-cs st-ct


#after flip card another image
card = """
<style>
[class="css-1kyxreq etr89bj2"]{
    justify-content: center;
}
</style>
"""

tansbuttonbg1 = """
<style>
[class="st-c7"]{
background: transparent;
}
</style>
"""
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#background-image: linear-gradient(180deg, rgba(11,16,19,1) 0%, rgba(4,34,54,1) 50%, rgba(9,16,21,1) 100%);

#background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);


#setting configurations
st.set_page_config(page_title="Yuvraj Singh Portfolio",layout="wide",initial_sidebar_state="expanded")
st.markdown(pg_bg_gradient, unsafe_allow_html=True)
st.markdown(card, unsafe_allow_html=True)
st.markdown(tansbuttonbg1, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")


with st.container():
    st.title("My Projects")
    st.divider()
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = cv2.imread('images/MoviesManiaLogo.png')
        image = cv2.resize(image, (256, 256))
        cv2.imwrite('images/MoviesMania.png',image)
        gif_html = get_img_with_href('images/MoviesMania.png', 'https://www.linkedin.com/in/yuvraj-singh-95b203289/')
        st.markdown(gif_html, unsafe_allow_html=True)

    with text_column:
        st.subheader("**Movie Recommendation System- MoviesMania**")
        # st.write("")
        st.write(
            """
            -**Primary Goal**: To provide an interface to users to find similary movies/web-series recommendations based on an uploaded video clip/YT Short.
            
            -**Solution**: To make use of the various faces of actors in the provided clip and the details provided(title, genre, plot) for the prediction of movie's title (if available in the dataset) or similar movies/web-series. 

            -**Result**: Prediction of movie's title(if available in the dataset) with 78% accuracy and similar movies with 85% acccuracy
            
             -**Tools Used**: Keras, Tensorflow, Word2Vec (Word Embeddings), MTCNN, NLTK, Spacy, VGGFace, OpenCV, Streamlit 
            """
        )
        st.markdown("[Source Code](https://github.com/YuvrajSingh-mist/MoviesMania)")
st.divider()
with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        image = cv2.imread('images/MoviesManiaLogo.png')
        image = cv2.resize(image, (128, 128))
        cv2.imwrite('images/MoviesMania.png',image)
        gif_html = get_img_with_href('images/MoviesMania.png', 'https://www.linkedin.com/in/yuvraj-singh-95b203289/')
        st.markdown(gif_html, unsafe_allow_html=True)
    with text_column:

        st.subheader("**Multi-Class News Classifier Web App**")
        # st.write("Wanna make your life easier , I've got something for you")
        st.write(
            """
           
           -**Primary Goal**: To provide an interface to users to find news under certain categories such as Tech, World, Business and Sports
            
            -**Solution:** Made use of the AGI news kaggle dataset and NLP-based preprocessing techniques along with custom-trained Word2Vec model alongwth Bi-LSTM model.

            -**Result**: Succesfully built the said WebApp with streamlit as front-end. Achieved an accuracy of 91% with precision 91 % and recall 90%
            
            -**Tools Used**: Keras, Tensorflow, Word2Vec (Word Embeddings), Bi-LSTMs, NLTK, Spacy, Streamlit 
            """
        )
        st.markdown("[Source Code](https://github.com/YuvrajSingh-mist/News_Multiclass_Category_Classifier)")

st.divider()
with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        image = cv2.imread('images/MoviesManiaLogo.png')
        image = cv2.resize(image, (128, 128))
        cv2.imwrite('images/MoviesMania.png',image)
        gif_html = get_img_with_href('images/MoviesMania.png', 'https://www.linkedin.com/in/yuvraj-singh-95b203289/')
        st.markdown(gif_html, unsafe_allow_html=True)
    with text_column:

        st.subheader("**Movie's Review System**")
        st.write("""
        
         -**Primary Goal**: To provide an interface to users to freely lookout for movies and its reviews of their choice without having to worry about it getting spoiled alongwith sentiment analysis on reviews to get a basic understanding of the quality of the chosen movie
            
        -**Solution:** Made use of the a Machine Learning model(sentiment analysis) using Voting Classifer(SVC+Logistic Regression) and Deep leearning model(spoiler v/s non-spoiler) using Bi-LSTMs after thorough preprocessings and custom traiend Word2Vec

        -**Result**: Succesfully built the said WebApp with streamlit as front-end. Achieved an accuracy of 91% with precision 91 % and recall 90%
            
        -**Tools Used**: Keras, Tensorflow, Word2Vec (Word Embeddings), Bi-LSTMs, NLTK, Spacy, Streamlit 
     
        
        """)


        st.markdown("[Source Code](https://github.com/YuvrajSingh-mist/Movie_Review_System)")

st.divider()
        
        
with st.container():
    st.header("My Contributions")
    st.divider()
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         image = cv2.imread('images/MoviesManiaLogo.png')
#         image = cv2.resize(image, (256, 256))
#         cv2.imwrite('images/MoviesMania.png',image)
#         gif_html = get_img_with_href('images/MoviesMania.png', 'https://www.linkedin.com/in/yuvraj-singh-95b203289/')
#         st.markdown(gif_html, unsafe_allow_html=True)

#     with text_column:
#         st.subheader("Movie Recommendation System- MoviesMania")
#         st.write("Wanna make your life easier , I've got something for you")
#         st.write(
#             """
#             -Search up for your favourite movies and series just from  your linux/Windows System just at your voice!
#             From sending whatsapp messages to downloading youtube video you are looking at , with just a voice command

#             -and for developers who want to contribute there is always a place
#             """
#         )
#         st.markdown("[Source Code](https://github.com/YuvrajSingh-mist/MoviesMania)")
    st.write('Coming soon...')
st.divider()