import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

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



# python_lottie = load_lottie("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
# java_lottie = load_lottie("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
# swift_lottie = load_lottie("https://assets3.lottiefiles.com/packages/lf20_inopzfvq.json")
# my_sql_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
# git_lottie = load_lottie("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
# github_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
# Andorid_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_fztluxdp.json")
# Docker_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
# Linux_lottie = load_lottie("https://assets2.lottiefiles.com/packages/lf20_drcnxdtp.json")
# Xcode_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
# firebase_lottie = load_lottie("https://assets5.lottiefiles.com/private_files/lf30_52jsgl4a.json")
img_proj1 = Image.open("movies-mania.png")
img_proj2 = Image.open("")
img_proj3 = Image.open()
# gireverb = Image.open("images/gitreverb.png")
# github_card = Image.open("images/gitcardmain.png")


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
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_proj1)

    with text_column:
        st.subheader("Movie Recommendation System- MoviesMania")
        st.write("Wanna make your life easier , I've got something for you")
        st.write(
            """
            ~Search up for your favourite movies and series just from  your linux/Windows System just at your voice!
            From sending whatsapp messages to downloading youtube video you are looking at , with just a voice command

            ~and for developers who want to contribute there is always a place
            """
        )
        st.markdown("[Checkout the project source code here...](https://github.com/YuvrajSingh-mist/MoviesMania)")

with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_proj2)

    with text_column:

        st.subheader("My personal portfolio website")

        st.markdown("[Checkout the project source code here...](https://github.com/YuvrajSingh-mist/Portfolio-Website)")


with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_proj3, width=200)

    with text_column:

        st.subheader("Fahion Recommendation System- FashionX")
        st.write("""
        A Social Media webapp for developers to share their projects and get feedback from other developers.
        A web app to visualize your github profile and repositories.
        """)


        st.markdown("[Checkout the project source cAutomateode here...](https://github.com/YuvrajSingh-mist/FashionX)")

