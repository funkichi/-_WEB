import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("<h1 style='text-align: center;'>病院検索便利君_WEB</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>☆徳島県の小児科をを検索できるアプリです☆</p>", unsafe_allow_html=True)

image = Image.open('Material/test_1.png')
st.image(image, caption='早めに受診してください')

for i in range(3):
    st.write('\n')

df = pd.read_csv('DataBase/徳島県.csv')
Location = list(df['市町村'].drop_duplicates())
selected_location = st.sidebar.selectbox('市町村を選択してください', Location)
selected_week = st.sidebar.selectbox('受診する日を選択してください', ['月', '火', '水', '木', '金', '土', '日', '祝日'])
selected_option = st.sidebar.selectbox('オプションを選択してください', ['オンライン診療', '夜間診療'])

if st.sidebar.button("検索"):
    if selected_location in df["市町村"].values:
        column_name_1 = ["医療機関名", "診療時間_午前", "診療時間_午後"]
        selected_row = df[(df["市町村"] == selected_location) & (df[selected_week] == 1)]
        st.write(selected_row[column_name_1])

map = df["MAP"]
st.sidebar.write(f"[地図]({map[1]})")