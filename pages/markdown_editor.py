import streamlit as st
from streamlit_ace import st_ace

st.title("markdownエディター！")

st.markdown("---")

prev, editor = st.columns(2)

with editor:
    st.text("エディター")
    content = st_ace(language='markdown', auto_update=True)

with prev:
    st.text("プレビュー")
    st.markdown(content)


st.markdown("---")
st.download_button(
     label=".mdとしてダウンロード",
     data=content,
     file_name='content.md',
 )
st.download_button(
     label=".txtとしてダウンロード",
     data=content,
     file_name='content.txt',
 )