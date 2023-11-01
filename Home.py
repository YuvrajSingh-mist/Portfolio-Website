import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(
    page_title = 'Yuvraj-Singh-Portfolio'
)

def load_lotties(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

def load_lottie(link):
    r = requests.get(link)
    if r.status_code !=200:
        return  None
    return None if r.status_code != 200 else r.json()



option = st.selectbox(
    'Choose a chapter below',
    ('Achievments', 'Education', 'Contact', 'My skills', 'Resume')
)



pg_bg_gradient = """

<style>
[class="main css-uf99v8 egzxvld5"]{
background-image: linear-gradient(to right top, #f4bedc, #e7b8df, #d7b2e3, #c3aee6, #acabe8, #979edb, #8192cd, #6c86bf, #596ea2, #465786, #33416b, #212c51);
}
</style>

"""


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
    
    
    
st.markdown("<h1 style='text-align: center; color: black;'>Hi</h1>", unsafe_allow_html=True)
st.divider()

st.markdown(pg_bg_gradient, unsafe_allow_html=True)
st.markdown(card, unsafe_allow_html=True)
st.markdown(tansbuttonbg1, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


lottie_img = load_lotties('lottie_files/Animation - 1698854547620.json')

st_lottie(
    lottie_img,
    speed=1,
    reverse=False,
    loop=True,
    quality='low',
    # renderer='svg',
    height=400,
    width=400,
    key=None
)

def css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

css("style/style.css")


lottie_gif = load_lottie("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")
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



