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

    st.header("My Skills :")
    st.subheader("Languages:")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
            #st.image(Image.open('python_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Python")
        with col2:
            st_lottie(java_lottie, height=70,width=70, key="kotlin", speed=4)
            #st.image(Image.open('java_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Java")
        with col3:
            # st_lottie(swift_lottie,height=70,width=70, key="swift", speed=2.5)
            pass
            #st.image(Image.open('javascript_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Swift")
        with col1:
            # st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
            pass
            #st.image(Image.open('sql_logo.png').resize((100,100)), use_column_width=True)
            #st.write("MYSQL")
        with col2:
            # st_lottie(firebase_lottie, height=70,width=70, key="Firebase", speed=4)Automate
            pass



    # st.subheader("Frameworks:")
    # with st.container():
    #     col1, col2, col3 = st.columns([1, 1, 1])
    #     with col1:
    #         st.image("https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg",width=70)
    #         #st.image(Image.open('flask_logo.png').resize((100,100)), use_column_width=True)
    #         #st.write("Flask")
    #     with col2:
    #         st.image("https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg",width=70)
    #         #st.image(Image.open('django_logo.png').resize((100,100)), use_column_width=True)
    #         #st.write("Django")

    st.subheader("Tools:")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st_lottie(git_lottie,height=70,width=70, key="Git", speed=2.5)
            #st.image(Image.open('git_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Git")
        with col1:
            st_lottie(github_lottie,height=70,width=70, key="Github", speed=2.5)
            #st.image(Image.open('git_logo.png').resize((100,100)), use_column_width=True)
            #st.write("GitHub")
        with col2:
            st_lottie(Andorid_lottie,height=70,width=70, key="Android Studio", speed=2.5)
            #st.image(Image.open('jupyter_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Android Studio")
        with col3:
            st.image("https://www.vectorlogo.zone/logos/visualstudio_code/visualstudio_code-icon.svg",width=80)
            #st.image(Image.open('vscode_logo.png').resize((100,100)), use_column_width=True)
            #st.write("VS Code")
        with col1:
            st_lottie(Linux_lottie,height=70,width=70, key="Linux", speed=2.5)
            #st.image(Image.open('pycharm_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Linux")
        with col2:
            # st_lottie(Docker_lottie,height=100,width=100, key="docker", speed=2.5)
            pass
            #st.image(Image.open('pycharm_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Docker")
        with col3:
            st.image("https://www.vectorlogo.zone/logos/apple_xcode/apple_xcode-ar21.svg",width=160)
            #st.image(Image.open('mysql_logo.png').resize((100,100)), use_column_width=True)
            #st.write("Xcode")
