import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("<h1 style='text-align: center;'>病院検索便利君</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>☆徳島の病院を検索できるアプリです☆</p>", unsafe_allow_html=True)

image = Image.open('Material/test_1.png')
st.image(image, caption='早めの受診をオススメいたします')

for i in range(3):
    st.write('\n')

df = pd.read_csv('DataBase/徳島県.csv')
Location = list(df['市町村'].drop_duplicates())
selected_location = st.selectbox('市町村を選択してください', Location)
selected_week = st.selectbox('受診する日を選択してください', ['月', '火', '水', '木', '金', '土', '日', '祝日'])
selected_option = st.selectbox('オプションを選択してください', ["選択なし", "オンライン診療", "夜間診療"])

column_name_2 = ["医療機関名", "住所", "電話番号", "医師名", "診療時間_午前", "診療時間_午後", "月", "火", "水", "木", "金", "土", "日", "祝日", "休診日_1", "休診日_2", "休診日_3", "オンライン診療", "夜間診療", "特徴"]

with st.form(key='my_form'):
    if st.form_submit_button("検索"):
        if selected_option == "オンライン診療":
            if selected_location in df["市町村"].values:
                column_name_1 = ["医療機関名", "診療時間_午前", "診療時間_午後"]
                selected_row = df[(df["市町村"] == selected_location) & (df[selected_week] == 1) & (df["オンライン診療"] == 1)]
                st.dataframe(selected_row[column_name_1])
                selected_row_index = st.selectbox("選択", selected_row.index)
                
                # コールバックをst.form_submit_buttonに移動
                st.form_submit_button("詳細", on_click=lambda: st.table(selected_row.loc[selected_row_index, column_name_2]))
        
        elif selected_option == "夜間診療":
            if selected_location in df["市町村"].values:
                column_name_1 = ["医療機関名", "診療時間_午前", "診療時間_午後"]
                selected_row = df[(df["市町村"] == selected_location) & (df[selected_week] == 1) & (df["夜間診療"] == 1)]
                st.dataframe(selected_row[column_name_1])
                selected_row_index = st.selectbox("選択", selected_row.index)
                
                # コールバックをst.form_submit_buttonに移動
                st.form_submit_button("詳細", on_click=lambda: st.table(selected_row.loc[selected_row_index, column_name_2]))
        
        elif selected_option == "選択なし":
            if selected_location in df["市町村"].values:
                column_name_1 = ["医療機関名", "診療時間_午前", "診療時間_午後"]
                selected_row = df[(df["市町村"] == selected_location) & (df[selected_week] == 1)]
                st.dataframe(selected_row[column_name_1])
                selected_row_index = st.selectbox("選択", selected_row.index)
                
                # コールバックをst.form_submit_buttonに移動
                st.form_submit_button("詳細", on_click=lambda: st.table(selected_row.loc[selected_row_index, column_name_2]))

map = df["MAP"]
st.sidebar.write(f"[画像保管場所]({map[0]})")