import streamlit as st
import pandas as pd
from PIL import Image

# ページ1のコンテンツ
def page1():
    st.write('ページ1のコンテンツd')
    
# ページ2のコンテンツ
def page2():
    st.write('ページ2のコンテンツ')

# メインのコード
st.markdown("<h1 style='text-align: center;'>病院検索便利君</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>☆徳島県の小児科をを検索できるアプリです☆</p>", unsafe_allow_html=True)

image = Image.open('Material/test_1.png')
st.image(image, caption='はやめに受診してください')

for i in range(3):
    st.write('\n')

df = pd.read_csv('DataBase/徳島県.csv')
Location = list(df['市町村'].drop_duplicates())
selected_location = st.sidebar.selectbox('市町村を選択してください', Location)
selected_week = st.sidebar.selectbox('曜日を選択してください', ['月', '火', '水', '木', '金', '土', '日', '祝'])
selected_option = st.selectbox('オプションを選択してください', ['オンライン診療', '夜間診療'])

# 「検索」ボタンが押されたときにページを切り替える
if st.button('検索'):
    if selected_option == 'NAISIS':
        page1()
    elif selected_option == 'MORISIS':
        page2()

st.markdown('[画像保管場所](https://www.google.co.jp/maps/place/%E6%97%A5%E4%BA%9C%E5%8C%96%E5%AD%A6%E5%B7%A5%E6%A5%AD%EF%BC%88%E6%A0%AA%EF%BC%89+N%E5%B7%A5%E5%A0%B4/@34.1343344,134.5222713,17z/data=!3m1!4b1!4m6!3m5!1s0x35537226e570286f:0x97f4d7ff4a4ccdec!8m2!3d34.13433!4d134.5248462!16s%2Fg%2F1v96jlyc?entry=ttu)')
