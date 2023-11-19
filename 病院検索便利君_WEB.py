
import streamlit as st
import pandas as pd
from PIL import Image

#画像サイズを変数に代入
size_logo = (600, 600)
size_logo2 = (400, 400)
size_city = (160, 160)
size_date = (192, 192)
size_option = (160, 160)

#画像ファイルを読み込んで.thumbnailでサイズを指定
image_logo = Image.open('Material/logo.png')
image_logo.thumbnail(size_logo)
image_logo2 = Image.open('Material/logo2.png')
image_logo2.thumbnail(size_logo2)
image_city = Image.open('Material/city.png')
image_city.thumbnail(size_city)
image_date = Image.open('Material/date.png')
image_date.thumbnail(size_date)
image_option = Image.open('Material/option.png')
image_option.thumbnail(size_option)

#()内の変数で表示する画像を指定
st.image(image_logo2)
st.image(image_logo)

#3列改行
for i in range(3):
    st.write('\n')

#pandasでcsvファイルを読み込んでセレクトボックスを配置する
df = pd.read_csv('DataBase/徳島県.csv')
Location = list(df['市町村'].drop_duplicates())
st.image(image_city)
selected_location = st.selectbox("", Location, label_visibility="collapsed")
st.image(image_date)
selected_week = st.selectbox('', ['月', '火', '水', '木', '金', '土', '日', '祝日'], label_visibility="collapsed")
st.image(image_option)
selected_option = st.selectbox('', ["選択なし", "オンライン診療", "夜間診療"], label_visibility="collapsed")

#with内で使用する変数に事前に代入しておく(検索結果の詳細に表示したいカラム名を指定)
column_name_2 = ["医療機関名", "住所", "電話番号", "医師名", "診療時間_午前", "診療時間_午後", "月", "火", "水", "木", "金", "土", "日", "祝日", "休診日_1", "休診日_2", "休診日_3", "オンライン診療", "夜間診療", "特徴"]

#セレクトボックスを選択する度にリロードされるのでwithに内包して回避
#セレクトボックスで選択されたオプション別に検索ボタンが押された時の動作をif構文で記述
with st.form(key='my_form'):
    #検索ボタンが押された時
    if st.form_submit_button("検索"):
        #オプションで選択した項目が"オンライン診療"の時
        if selected_option == "オンライン診療":
            #選択した市町村がdf["市町村"]の中にあった時
            if selected_location in df["市町村"].values:
                column_name_1 = ["医療機関名", "診療時間_午前", "診療時間_午後"]
                #一致した"市町村"の行の中から、曜日に〇があり、かつオプションに〇があるデータを照合する
                selected_row = df[(df["市町村"] == selected_location) & (df[selected_week] == "〇") & (df["オンライン診療"] == "〇")]
                #照合により一致した行データの中から、表示したいカラム名をcolumn_name1で指定して一覧を表示する
                st.dataframe(selected_row[column_name_1])
                #表示された一覧データの行番号をセレクトボックスに反映
                st.markdown("<h5 style='text-align: left; color: salmon;'>行番号を選択して検索ボタンを押してください</h5>", unsafe_allow_html=True)
                selected_row_index = st.selectbox("", selected_row.index, label_visibility="collapsed")            
                #セレクトボックスで行番号を選択し、再度検索ボタンを押すと選択した行番号にあるデータの詳細が表示される
                #elected_row_indexが表示したい行、column_name_2が表示したい列(カラム名)
                st.write(selected_row.loc[selected_row_index, "医療機関名"] + "の詳細情報")
                st.table(selected_row.loc[selected_row_index, column_name_2])
        
                #mapにgoogleマップのアドレスを代入し、map_nameにリンク用の表示文字を代入する(↑詳細の表示とリンクするようにselected_row_indexで行指定する)
                map = selected_row.loc[selected_row_index, ["MAP"]]
                map_name = selected_row.loc[selected_row_index, ["医療機関名"]]

                #アドレスが長いのでmap_name変数をリンクの表示文字に指定してmap変数でアドレスを指定する(文字列内で変数を使用する為にf-stringsを使う)
                st.markdown("<h5 style='text-align: left; color: darkturquoise;'>Googleマップ</h5>", unsafe_allow_html=True)
                st.write(f"[{map_name[0]}]({map[0]})")
                
        elif selected_option == "夜間診療":
            if selected_location in df["市町村"].values:
                column_name_1 = ["医療機関名", "診療時間_午前", "診療時間_午後"]
                selected_row = df[(df["市町村"] == selected_location) & (df[selected_week] == "〇") & (df["夜間診療"] == "〇")]
                st.dataframe(selected_row[column_name_1])
                st.markdown("<h5 style='text-align: left; color: salmon;'>行番号を選択して検索ボタンを押してください</h5>", unsafe_allow_html=True)
                selected_row_index = st.selectbox("", selected_row.index, label_visibility="collapsed") 
                st.write(selected_row.loc[selected_row_index, "医療機関名"] + "の詳細情報")                
                st.table(selected_row.loc[selected_row_index, column_name_2])
                
                map = selected_row.loc[selected_row_index, ["MAP"]]
                map_name = selected_row.loc[selected_row_index, ["医療機関名"]]
                st.markdown("<h5 style='text-align: left; color: darkturquoise;'>Googleマップ</h5>", unsafe_allow_html=True)
                st.write(f"[{map_name[0]}]({map[0]})")

        elif selected_option == "選択なし":
            if selected_location in df["市町村"].values:
                column_name_1 = ["医療機関名", "診療時間_午前", "診療時間_午後"]
                selected_row = df[(df["市町村"] == selected_location) & (df[selected_week] == "〇")]
                st.dataframe(selected_row[column_name_1])
                st.markdown("<h5 style='text-align: left; color: salmon;'>行番号を選択して検索ボタンを押してください</h5>", unsafe_allow_html=True)
                selected_row_index = st.selectbox("", selected_row.index, label_visibility="collapsed") 
                st.write(selected_row.loc[selected_row_index, "医療機関名"] + "の詳細情報")                
                st.table(selected_row.loc[selected_row_index, column_name_2])
                
                map = selected_row.loc[selected_row_index, ["MAP"]]
                map_name = selected_row.loc[selected_row_index, ["医療機関名"]]
                st.markdown("<h5 style='text-align: left; color: darkturquoise;'>Googleマップ</h5>", unsafe_allow_html=True)
                st.write(f"[{map_name[0]}]({map[0]})")