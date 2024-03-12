import streamlit as st
import pandas as pd
import numpy as np

# タイトル
st.title('Streamlit デモアプリ')

# CSVファイルを読み込む
df = pd.read_csv('c01.csv', encoding='shift_jis')

# 表を表示する
st.write(df)
