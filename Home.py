import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
import json
from streamlit_option_menu import option_menu

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


def load_lotties(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

def load_lottie(link):
    r = requests.get(link)
    if r.status_code !=200:
        return  None
    return None if r.status_code != 200 else r.json()


def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")

#loading assets
lottie_gif = load_lottie("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")
lottie_gif_2 = load_lotties('lottie_files/Animation - 1698854547620.json')
python_lottie = load_lottie("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottie("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
swift_lottie = load_lottie("https://assets3.lottiefiles.com/packages/lf20_inopzfvq.json")
my_sql_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottie("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
Andorid_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_fztluxdp.json")
Docker_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
Linux_lottie = load_lottie("https://assets2.lottiefiles.com/packages/lf20_drcnxdtp.json")
Xcode_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
firebase_lottie = load_lottie("https://assets5.lottiefiles.com/private_files/lf30_52jsgl4a.json")
img_proj1 = Image.open("images/FRIDAY.png")
img_proj2 = Image.open("images/1.png")
gireverb = Image.open("images/gitreverb.png")
github_card = Image.open("images/gitcardmain.png")
        
        
# options = st.selectbox(
#     'Choose a chapter below',
#     ('Achievments', 'Education', 'Contact', 'My Skills', 'Resume', 'Projects'),
#     # placeholder='Home'
#     index=None,
# )

selected= ""
selected = option_menu("Table of Contents", ["Home", "Education", "Projects", "My Skills", "Achievements", "Hobbies and Interests", "Connect with me", "Resume"], icons=["gear", "gear","gear", "gear", "gear", "gear", "gear", "gear"], menu_icon="cast", default_index=0, orientation='horizontal')
                          



with st.container():
    left_column,right_column = st.columns([2,1])
    with left_column:
        # st.markdown("<h3 style='text-align: center; color: black;'></h3>", unsafe_allow_html=True)
        st.subheader("Hi, Myself Yuvraj Singh :wave:")
        st.subheader("An AI/ML enthusiast with a deep interest in NLP")
        st.write("I am passionate about learning different techniques/algorithms and finding ways to tackle chalnneging problems solve it using the domain of AI/ML using python")
        st.write(
            """
            
            Currently I am in my 1st year of B.Tech in Computer Science and Engineering

            - Started My Journey in the field of AI/ML last year and Explored the domain of ML and DL in Python and its Real-World Applications

            - Learned about Data Analytics tools in Python now on my way to explore it further

            - I have my current skillset in Python,C++,linux, Android Development (in kotlin), Git, Github

            """
        )

        # st.write("[Explore more about my work on github ](https://github.com/YuvrajSingh-mist)")

with right_column:
    st_lottie(lottie_gif, height=400, key="coding")

with st.container():
    column_widths = [2, 1]
    left_column,right_column = st.columns(column_widths)
    with left_column:
        st.write("---")
        st.header("About Me")
        st.write('##')
#         st.write(
#             """
            
#             Currently I am in my 1st year of B.Tech in Computer Science and Engineering

#             - Started My Journey in the field of AI/ML last year and Explored the domain of ML and DL in Python and its Real-World Applications

#             - Learned about Data Analytics tools in Python now on my way to explore it further

#             - I have my current skillset in Python,C++,linux, Android Development (in kotlin), Git, Github

#             """
#         )
        # st.write("[Explore my Github Profile](https://github.com/rpj09)")
        st.write('##')
       
    with right_column:

         st_lottie(lottie_gif_2, width=600, height=600, key="coding2")     
st.divider()


st.title('Add bio')


if selected == 'Connect with me'  :
    switch_page('Connect with me')
    
if selected == 'My Resume'  :
    switch_page('Resume')

if selected == 'Education':
    switch_page('Education')

if selected == 'Achievements':
    switch_page('Achievements')
    
if selected == 'My Skills':
    switch_page('My skills')

if selected == 'Projects':
    switch_page('Projects')
    
if selected == 'Hobbies and Interests':
    switch_page('Hpbbies and Interests')