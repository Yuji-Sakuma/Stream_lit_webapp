import streamlit as st
import pandas as pd

# タイトル
st.title('西暦別の人口増加グラフ')

# CSVファイルを読み込む
df = pd.read_csv('c01.csv', encoding='shift_jis')

# 「全国」のデータのみを選択
df_nationwide = df[df['都道府県名'] == '全国']

# 西暦と人口の列を選択
df_selected = df_nationwide[['西暦（年）', '人口（総数）']]

# フィルター用の年を選択するためのスライダー
start_year, end_year = int(df_selected['西暦（年）'].min()), int(df_selected['西暦（年）'].max())
years = st.slider("年を選択してください", start_year, end_year, (start_year, end_year))

# 選択された年でデータをフィルタリング
df_filtered = df_selected[(df_selected['西暦（年）'] >= years[0]) & (df_selected['西暦（年）'] <= years[1])]

# グラフを描画（x軸とy軸を入れ替える）
st.line_chart(df_filtered.set_index('人口（総数）')['西暦（年）'])
