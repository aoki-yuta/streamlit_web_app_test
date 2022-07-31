from datetime import datetime
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_player import st_player

# 基本的な文章
st.title("テストアプリ！")
st.caption("これはstreamlitのテスト用のアプリです")

st.subheader("文章の表示")
st.text("ここに文章をかけるよ")

# コードの表示
st.subheader("コードの表示")
code = '''
#上のはこんなコード
import streamlit as st

st.title("テストアプリ！")
st.caption("これはstreamlitのテスト用のアプリです")

st.subheader("これはサブヘッダーです")
st.text("ここに文章をかけるよ")

'''

st.code(code, language="python")

# 画像の表示
st.subheader("画像の表示")
image = Image.open('./data/streamlit_logo.png')
st.image(image, width=200, caption="これはロゴです")

# テキストボックス
st.subheader("テキストボックス")
name = st.text_input ("名前を入れてね")
if name != "":
    st.text(f"{name}さんこんにちは！")

# ボタン
st.subheader("ボタン")
st.text("ボタンはどれか一つがTrueになるっぽい")
btn = st.button("押すなよ")
st.text(f"{btn}")
btn = st.button("押してね")
st.text(f"{btn}")

# フォーム
st.subheader("フォーム")
with st.form(key='profile_form'):
    name = st.text_input("名前")
    address = st.text_input("住所")

    #フォーム用ボタン
    submit_btn = st.form_submit_button('送信')
    
    if submit_btn:
         st.text(f"ようこそ{name}さん！{address}に荷物を送ったよ！")
    
# セレクトボックス
st.subheader("セレクトボックス")
age_category = st.selectbox(
    '年齢層',
    ('子供（18才未満）', '大人(18才以上)')
)
st.text(f"あなたは{age_category}ですね！")

# ラジオボタン
st.subheader("ラジオボタン")
age_category2 = st.radio(
    '年齢層',
    ('子供（18才未満）', '大人(18才以上)')
)
st.text(f"あなたは{age_category2}ですね！")

# 複数選択
st.subheader("複数選択")
hobby = st.multiselect(
    '趣味',
    ('スポーツ', '音楽', '読書', 'アニメ・映画', '料理')
)

if hobby != []:
    st.text(f"趣味は{'と'.join(hobby)}だね！")


# チェックボックス
st.subheader("チェックボックス")
mail_subscribe = st.checkbox("メールマガジンを購読する")

# スライダー
st.subheader("スライダー")
st.text("面積を求めるよ")
height = st.slider('高さ', min_value=0, max_value=100)
width = st.slider('幅', min_value=0, max_value=100)
st.text(f"面積は：{height*width}")

# カラーピッカー
st.subheader("カラーピッカー")
color = st.color_picker('テーマカラー', '#9CC5E6')

# 日付
st.subheader("日付")
start_date = st.date_input(
    '開始日',
    datetime.today()
)


# データフレームの表示
st.subheader("データフレーム")
st.text("千葉の平均気温")
df = pd.read_csv('./data/kionn.csv', index_col="月")
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df['2021'])


# matplotlib
st.subheader("matplotlibで表示")

fig, ax = plt.subplots()
ax.plot(df.index, df['2021'])
ax.set_title("matplotlib graph")
st.pyplot(fig)

# カラム
st.subheader("カラム")

col1, col2 = st.columns(2)

with col1:
    st.text("こちらはcol1")

with col2:
    st.text("こちらはcol2")


# markdown
mkdown = '''
---
ここからmarkdownです
# タイトル
## サブタイトル
---
'''
st.markdown(mkdown)


# プレイヤー
st.subheader("追加モジュール")

url = "[追加モジュール参考サイト](https://streamlit.io/components)"
st.markdown(url)

st.text("試しに動画再生モジュールを追加")
code = '''
pip install streamlit-player
'''
st.code(code)

st_player("https://youtu.be/4nsTce1Oce8")