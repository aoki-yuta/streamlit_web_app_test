import streamlit as st
import pyqrcode
from PIL import Image

st.title("QRコード作成")

source = st.text_input("テキストを入力")
code = pyqrcode.create(source, error='L', version=3, mode='binary')

code.png('./data/qrcode.png', scale=9, module_color=[0, 0, 0, 128], background=[255, 255, 255])

image = Image.open('./data/qrcode.png')
st.image(image, width=200)

