import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

import time

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

        
# options = st.selectbox(
#     'Table of Contents',
#     ('Achievments', 'Education', 'Connect with me', 'My Skills', 'Resume', 'Projects', 'Home', 'Hobbies and Interests'),
#     # placeholder='Home'
#     index=None,
# )

st.markdown("<h1 style='text-align: center; color: black;'>My Resume</h13>", unsafe_allow_html=True)
st.divider()


res1 = Image.open("images/Resume-1.png")
res2 = Image.open("images/Resume-2.png")
# Resume image
# st.title("Resume")
# st.markdown("## Yuvraj Singh")
# res1 = Image.open("images/Resume.png")
# res2 = Image.open("images/res2.jpg")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(res1)
# pdf_url = "https://drive.google.com/file/d/1PEvEfGT1eZ-myO1gQ9W46c0YBq3hrU-Y/view?usp=sharing"
with last_co:
    st.image(res2)
# pdf_url = "https://drive.google.com/file/d/1PEvEfGT1eZ-myO1gQ9W46c0YBq3hrU-Y/view?usp=sharing"

# Download button

# res2 = Image.open("images/res2.jpg")
col1, col2, col3, col4, col5= st.columns(5)
with col1:
    pass
with col2:
    pass
with col3:
#     # st.image(res1)
#     if st.button("Download Resume"):
#         response = requests.get(pdf_url)
#         with open("Resume Yuvraj Singh.pdf", "wb") as f:
#             f.write(response.content)
    with open("pages/Resume-Yuvraj-Singh.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    # st.bar(0)
    with st.spinner('Please wait...'):
       
        if st.download_button(label="Download Resume",
                            data=PDFbyte,
                            file_name="Yuvraj Singh Resume.pdf",
                            mime='application/octet-stream'):
            time.sleep(1)
            st.success('Done!')
    # st.bar(100)
    # st.success("Download complete!")
st.divider()
# st.write('Coming Soon...')
with col4:
    pass
with col5:
    pass


