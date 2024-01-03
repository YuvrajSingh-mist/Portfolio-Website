import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import cv2
import base64
import os

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data
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

        
# options = st.selectbox(
#     'Table of Contents',
#     ('Achievments', 'Education', 'Connect with me', 'My Skills', 'Resume', 'Projects', 'Home', 'Hobbies and Interests'),
#     # placeholder='Home'
#     index=None,
# )


with st.container():
    st.title("My Achievments")
    st.divider()
    
    st.subheader('D3-Techno-Management Fest@ IIIT-BH')
    st.write(
    """

    - Bagged First Prize at the said event in the domain of AI/ML, leading, managing and co-ordinating a team of three people.
    
    - It was a thrilling experience was for me, leading and co-ordinating with a team consisting of students from different backgrounds and skill sets with many ups-and-downs ranging from model optimization to deployment but it was all worth it in the end. 

    """
    )
    st.divider()
    
        
      
    st.subheader('International Rank 6 @SOF IMO')
    st.write(
    """

    - Bagged international rank 6 at the prestigious Mathematics Olympiad conducted by SOF every year for high school students around the globe.

    """
    )    
    st.divider()
    
        
        
    st.subheader('Medal of Distinction @SOF IMO')
    st.write(
    """

    - Achieved Medal of Distinction with Zonal Rank 6 in the prestigious Mathematics Olympiad conducted by SOF every year for high school students around the globe in the year 2019-2020.

    """
    )    
    st.divider()
    
    st.subheader('Gold Medal in National Mathematical Olympiad Contest')
    st.write(
    """
    - Achieved Gold Medal in a mathematical olympiad organized by the All India Schools Mathematics Teachers Assosciation securing 93% marks overal
     in the year 2018-19.

    """
    
)
    st.divider()
    
    st.subheader('Gold Medal @SOF NCO')
    st.write(
    """
    - Achieved Gold Medal as a Class Topper in the prestigious Computing Olympiad conducted by SOF every year for high school students around the globe in the year 2016-2017.


    """
    
)
    st.divider()
    
    st.subheader('Gold Medal @SOF NSO')
    st.write(
    """
    - Achieved Gold Medal as a Class Topper in the prestigious Science Olympiad conducted by SOF every year for high school students around the globe in the year 2016-2017.


    """
    
)
    st.divider()
    