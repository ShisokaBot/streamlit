import streamlit as st
import pandas as pd
import altair as alt

"""
#### 品別売上
"""
def drink_kind():
    drink_data = pd.read_excel('management_support_app/data/sales_data/2022sales_data.xlsx', sheet_name='drink',
                            engine='openpyxl', index_col=0)
    # 行と列を入れ替える
    transposed_drink_data = drink_data.transpose()
    # 2カラム作成
    col_1, col_2 = st.columns(2)
    with col_1:
        # ラジオボタンの作成
        selected_drink = st.radio('メニューを選んでください',
                                transposed_drink_data.columns.unique(),
                                key='test8')
    with col_2:
        # データフレームを作る
        data = pd.DataFrame({
            '営業月': transposed_drink_data.index.unique(),
            '売上数': transposed_drink_data[selected_drink]
            })
        st.subheader(selected_drink)
        # 棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('営業月', sort=None),
            y='売上数',
        ),
            use_container_width=True)

def meat_kind():
    meat_data = pd.read_excel('management_support_app/data/sales_data/2022sales_data.xlsx',
                            sheet_name='meat',
                            engine='openpyxl', index_col=0)
    # 行と列を入れ替える
    transposed_drink_data = meat_data.transpose()
    # 2カラム作成
    col_1, col_2 = st.columns(2)
    with col_1:
        # ラジオボタンの作成
        selected_drink = st.radio('メニューを選んでください',
                                transposed_drink_data.columns.unique(),
                                key='test8')
    with col_2:
        # データフレームを作る
        data = pd.DataFrame({
            '営業月': transposed_drink_data.index.unique(),
            '売上数': transposed_drink_data[selected_drink]
            })
        st.subheader(selected_drink)
        # 棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('営業月', sort=None),
            y='売上数',
        ),
            use_container_width=True)

def sidemenu_kind():
    meat_data = pd.read_excel('management_support_app/data/sales_data/2022sales_data.xlsx',
                            sheet_name='sidemenu',
                            engine='openpyxl', index_col=0)
    # 行と列を入れ替える
    transposed_drink_data = meat_data.transpose()
    # 2カラム作成
    col_1, col_2 = st.columns(2)
    with col_1:
        # ラジオボタンの作成
        selected_drink = st.radio('メニューを選んでください',
                                transposed_drink_data.columns.unique(),
                                key='test8')
    with col_2:
        # データフレームを作る
        data = pd.DataFrame({
            '営業月': transposed_drink_data.index.unique(),
            '売上数': transposed_drink_data[selected_drink]
            })
        st.subheader(selected_drink)
        # 棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('営業月', sort=None),
            y='売上数',
        ),
            use_container_width=True)

def monthly_drink_sales():
    # タイトル
    st.markdown(' ### ドリンクメニュー売上数比較')
    # エクセルデータの読み込み
    drink_data = pd.read_excel('management_support_app/data/sales_data/2022sales_data.xlsx', sheet_name='drink',
                                engine='openpyxl', index_col=0)
    # 行と列を入れ替える
    transposed_drink_data = drink_data.transpose()
    # マルチセレクトの作成
    multiselected_drink_list = st.multiselect(
        '確認したいドリンクのメニューを選んでください(複数選択可)',
        transposed_drink_data.columns.unique(),
        '生大'
    )
    st.write(transposed_drink_data[multiselected_drink_list])
    if not multiselected_drink_list:
        st.error('表示するメニューが選択されていません。')
    else:
        st.line_chart(transposed_drink_data[multiselected_drink_list])

def monthly_meat_sales():
    # タイトル
    st.markdown(' ### 肉類売上数比較')
    # エクセルデータの読み込み
    meat_data = pd.read_excel('management_support_app/data/sales_data/2022sales_data.xlsx',
                                sheet_name='meat',
                                engine='openpyxl', index_col=0)
    # 行と列を入れ替える
    transposed_meat_data = meat_data.transpose()
    # マルチセレクトの作成
    multiselected_meat_list = st.multiselect(
        '確認したいドリンクのメニューを選んでください(複数選択可)',
        transposed_meat_data.columns.unique(),
        '上カルビ'
    )
    st.write(transposed_meat_data[multiselected_meat_list])
    if not multiselected_meat_list:
        st.error('表示するメニューが選択されていません。')
    else:
        st.line_chart(transposed_meat_data[multiselected_meat_list])

def monthly_sidemenu_sales():
    # タイトル
    st.markdown(' ### サイドメニュー売上数比較')
    # エクセルデータの読み込み
    sidemenu_data = pd.read_excel('management_support_app/data/sales_data/2022sales_data.xlsx',
                                sheet_name='sidemenu',
                                engine='openpyxl', index_col=0)
    # 行と列を入れ替える
    transposed_sidemenu_data = sidemenu_data.transpose()
    # マルチセレクトの作成
    multiselected_sidemenu_list = st.multiselect(
        '確認したいドリンクのメニューを選んでください(複数選択可)',
        transposed_sidemenu_data.columns.unique(),
        'クッパ'
    )
    st.write(transposed_sidemenu_data[multiselected_sidemenu_list])
    if not multiselected_sidemenu_list:
        st.error('表示するメニューが選択されていません。')
    else:
        st.line_chart(transposed_sidemenu_data[multiselected_sidemenu_list])

if st.checkbox('ドリンクの品別売上'):
    drink_kind()
if st.checkbox('ドリンクの品別売上(マルチセレクト)'):
    monthly_drink_sales()

if st.checkbox('肉類の品別売上'):
    meat_kind()
if st.checkbox('肉類の品別売上(マルチセレクト)'):
    monthly_meat_sales()

if st.checkbox('サイドメニューの品別売上'):
    sidemenu_kind()
if st.checkbox('サイドメニューの品別売上(マルチセレクト)'):
    monthly_sidemenu_sales()
