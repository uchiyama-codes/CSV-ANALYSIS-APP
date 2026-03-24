import streamlit as st
import pandas as pd

st.title("CSV分析アプリ")

# ファイルアップロード
file = st.file_uploader("csvファイルを選択してください", type="csv")

if file:
    df = pd.read_csv(file)

    st.subheader("データ")
    st.write(df)

    st.subheader("統計情報")
    st.write(df.describe())

    # 列選択
    column = st.selectbox("グラフにする列を選択", df.columns)

    st.subheader("グラフ")
    st.line_chart(df[column])