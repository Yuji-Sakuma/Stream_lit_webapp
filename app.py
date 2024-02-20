import streamlit as st
import pandas as pd
import numpy as np

# タイトル
st.title('Streamlit デモアプリ')

# ダミーデータの生成
data = pd.DataFrame({
    'first_column': np.random.rand(10),
    'second_column': np.random.rand(10)
})

# データテーブルの表示
st.write('これは私たちのダミーデータテーブルです。')
st.dataframe(data)

# 折れ線グラフの表示
st.line_chart(data)