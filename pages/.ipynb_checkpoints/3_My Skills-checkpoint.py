import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
# from streamlit_extras.app_logo import app_logo
import base64
import os

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache(allow_output_mutation=True)
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


def load_lottie(link):
    r = requests.get(link)
    if r.status_code !=200:
        return  None
    return None if r.status_code != 200 else r.json()




python_lottie = load_lottie("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
# java_lottie = load_lottie("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
tf_lottie = load_lottie("https://lottie.host/acd39f96-9bc4-4458-9fdb-00672c513334/SFJupCN6Xs.json")
my_sql_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottie("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
Andorid_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_fztluxdp.json")
# Docker_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
Linux_lottie = load_lottie("https://assets2.lottiefiles.com/packages/lf20_drcnxdtp.json")

        
# options = st.selectbox(
#     'Table of Contents',
#     ('Achievments', 'Education', 'Connect with me', 'My Skills', 'Resume', 'Projects', 'Home', 'Hobbies and Interests'),
#     # placeholder='Home'
#     index=None,
# )

def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")


st.markdown("<h1 style='text-align: center; color: black;'>My Skills</h1>", unsafe_allow_html=True)
st.divider()



with st.container():

    # st.header("My Skills :")
    st.title("Languages:")
    st.divider()
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
            #st.image(Image.open('python_logo.png').resize((100,100)), use_column_width=True)
            st.write("Python")
        # with col2:
        #     st_lottie(java_lottie, height=70,width=70, key="kotlin", speed=4)
        #     # st.image(Image.open('java_logo.png').resize((100,100)), use_column_width=True)
        #     st.write("Kotlin")
        with col2:
            # st_lottie(swift_lottie,height=70,width=70, key="swift", speed=2.5)
            st.image(Image.open('images/c.png').resize((64,64)))
            st.write("C")
            pass
        with col1:
            # st_lottie(my_sql_lottie,height=70,width=70, key="c++", speed=2.5)
            # pass
            st.image(Image.open('images/c++.png').resize((64,64)))
            st.write("C++")
        with col2:
            # st_lottie(firebase_lottie, height=70,width=70, key="Firebase", speed=4)Automate
            pass



    st.title("Frameworks/Library:")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
        # st.image("https://www.vectorlogo.zone/logos/apple_xcode/apple_xcode-ar21.svg",width=160)
        # pass
            st.image(Image.open('images/opencv.png').resize((100,64)))
            st.write("Opencv")
        
        with col2:
            st_lottie(tf_lottie,height=100,width=100, key="docker", speed=2.5)
            
            # st.image(Image.open('pycharm_logo.png').resize((64,64))
            st.write("Tensorflow")
        with col3:
            # st.image("https://www.vectorlogo.zone/logos/apple_xcode/apple_xcode-ar21.svg",width=160)
            # pass
            st.image(Image.open('images/Keras.png').resize((100,64)))
            st.write("Keras")

    st.title("Tools:")
    st.divider()
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st_lottie(git_lottie,height=70,width=70, key="Git", speed=2.5)
            #st.image(Image.open('git_logo.png').resize((100,100)), use_column_width=True)
            st.write("Git")
        with col1:
            st_lottie(github_lottie,height=70,width=70, key="Github", speed=2.5)
            #st.image(Image.open('git_logo.png').resize((100,100)), use_column_width=True)
            st.write("GitHub")
        with col2:
            st_lottie(Andorid_lottie,height=70,width=70, key="Android Studio", speed=2.5)
            #st.image(Image.open('jupyter_logo.png').resize((100,100)), use_column_width=True)
            st.write("Android Studio")
        with col3:
            st.image("https://www.vectorlogo.zone/logos/visualstudio_code/visualstudio_code-icon.svg",width=80)
            #st.image(Image.open('vscode_logo.png').resize((100,100)), use_column_width=True)
            st.write("VS Code")
        # with col1:
        #     st_lottie(Linux_lottie,height=70,width=70, key="Linux", speed=2.5)
        #     #st.image(Image.open('pycharm_logo.png').resize((100,100)), use_column_width=True)
        #     st.write("Linux")
       