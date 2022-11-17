import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
import numpy as np

 #レイアウト設定
layout1 = go.Layout(title=dict(text='<b>【温度】'),
                        font=dict(size=15),
                        legend=dict(xanchor='left',
                            yanchor='bottom',
                            x=0.32,
                            y=1.0,
                            orientation='h'    
                            ),width=900,height=700)
layout2 = go.Layout(title=dict(text='<b>【相対湿度】'),
                        font=dict(size=15),
                        legend=dict(xanchor='left',
                            yanchor='bottom',
                            x=0.32,
                            y=1.0,
                            orientation='h'    
                            ),width=900,height=700)
layout3 = go.Layout(title=dict(text='<b>【日射】'),
                        font=dict(size=15),
                        legend=dict(xanchor='left',
                            yanchor='bottom',
                            x=0.32,
                            y=1.0,
                            orientation='h'    
                            ),width=900,height=700)
layout4 = go.Layout(title=dict(text='<b>【CO2濃度】'),
                        font=dict(size=15),
                        legend=dict(xanchor='left',
                            yanchor='bottom',
                            x=0.32,
                            y=1.0,
                            orientation='h'    
                            ),width=900,height=700)

#タイトル
st.title("ベジ・アビオ環境分析")

# データフレーム読み込み
st.sidebar.write("""## ファイルアップロード""")
uploaded_file = st.sidebar.file_uploader("分析したいファイルをアップロードしてください", type='xlsx')
if uploaded_file:
    @st.cache(allow_output_mutation = True)
    def readfile_ex1():
        return pd.read_excel(uploaded_file, sheet_name='01', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex2():
        return pd.read_excel(uploaded_file, sheet_name='02', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex3():
        return pd.read_excel(uploaded_file, sheet_name='03', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex4():
        return pd.read_excel(uploaded_file, sheet_name='04', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex5():
        return pd.read_excel(uploaded_file, sheet_name='05', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex6():
        return pd.read_excel(uploaded_file, sheet_name='06', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex7():
        return pd.read_excel(uploaded_file, sheet_name='07', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex8():
        return pd.read_excel(uploaded_file, sheet_name='08', index_col=[0],parse_dates=[0])
    @st.cache(allow_output_mutation = True)
    def readfile_ex9():
        return pd.read_excel(uploaded_file, sheet_name='09', index_col=[0],parse_dates=[0])

    df_ex1 = readfile_ex1()
    df_ex2 = readfile_ex2()
    df_ex3 = readfile_ex3()
    df_ex4 = readfile_ex4()
    df_ex5 = readfile_ex5()
    df_ex6 = readfile_ex6()
    df_ex7 = readfile_ex7()
    df_ex8 = readfile_ex8()
    df_ex9 = readfile_ex9()
    # #プログレスバーの表示
    # latest_iteration = st.empty()
    # bar = st.progress(0)
    # for i in range(100):
    #    latest_iteration.text(f'Iteration {i+1}')
    #    bar.progress(i+1)
    #    time.sleep(0.1)

    #サイドバーの日付選ぶ
    st.sidebar.write("""
    # オプション設定
    以下のオプションから表示日数・温室を指定できます。
    """)
    st.sidebar.write("""## 表示日付・温室選択""")
    select_dates = st.sidebar.date_input('表示したい日付の選択',value=(df_ex1.index[0],df_ex1.index[-1]),min_value=df_ex1.index[0],max_value=df_ex1.index[-1])

    #ヘッダー
    st.header("温度・相対湿度・日射・CO2濃度のグラフ")

    #温室番号選ぶ
    list = ['1','2','3','4','5','6','7','8','9']
    stocks = st.sidebar.multiselect(label="温室番号の選択",
                options = list,
                default=['1','2','3','4','5','6','7','8','9'])
    if not stocks:
        st.error('少なくとも1つの温室番号を選んでください。')

    #温室ごとグラフデータ定義
    ondofig = go.Figure(layout=layout1)
    situdofig = go.Figure(layout=layout2)
    nisyafig = go.Figure(layout=layout3)
    CO2fig = go.Figure(layout=layout4)

    def cached_1():
        ondofig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['温度'] ,
                                marker_color='blue',
                                line_width=3,
                                name='1',))
        situdofig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['相対湿度'] ,
                                marker_color='blue',
                                line_width=3,
                                name='1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['日射'] ,
                                marker_color='blue',
                                line_width=3,
                                name='1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['CO2濃度'] ,
                                marker_color='blue',
                                line_width=3,
                                name='1'))

    def cached_2():
        ondofig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['温度'] ,
                                marker_color='orange',
                                line_width=3,
                                name='2'))
        situdofig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['相対湿度'] ,
                                marker_color='orange',
                                line_width=3,
                                name='2'))
        nisyafig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['日射'] ,
                                marker_color='orange',
                                line_width=3,
                                name='2'))
        CO2fig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['CO2濃度'] ,
                                marker_color='orange',
                                line_width=3,
                                name='2'))
    def cached_3():
        ondofig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['温度'] ,
                                marker_color='green',
                                line_width=3,
                                name='3'))
        situdofig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['相対湿度'] ,
                                marker_color='green',
                                line_width=3,
                                name='3'))
        nisyafig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['日射'] ,
                                marker_color='green',
                                line_width=3,
                                name='3'))
        CO2fig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['CO2濃度'] ,
                                marker_color='green',
                                line_width=3,
                                name='3'))

    def cached_4():
        ondofig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['温度'] ,
                                marker_color='red',
                                line_width=3,
                                name='4'))
        situdofig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['相対湿度'] ,
                                marker_color='red',
                                line_width=3,
                                name='4'))
        nisyafig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['日射'] ,
                                marker_color='red',
                                line_width=3,
                                name='4'))
        CO2fig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['CO2濃度'] ,
                                marker_color='red',
                                line_width=3,
                                name='4'))

    def cached_5():
        ondofig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['温度'] ,
                                marker_color='purple',
                                line_width=3,
                                name='5'))
        situdofig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['相対湿度'] ,
                                marker_color='purple',
                                line_width=3,
                                name='5'))
        nisyafig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['日射'] ,
                                marker_color='purple',
                                line_width=3,
                                name='5'))
        CO2fig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['CO2濃度'] ,
                                marker_color='purple',
                                line_width=3,
                                name='5'))

    def cached_6():
        ondofig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['温度'] ,
                                marker_color='brown',
                                line_width=3,
                                name='6'))
        situdofig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['相対湿度'] ,
                                marker_color='brown',
                                line_width=3,
                                name='6'))
        nisyafig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['日射'] ,
                                marker_color='brown',
                                line_width=3,
                                name='6'))
        CO2fig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['CO2濃度'] ,
                                marker_color='brown',
                                line_width=3,
                                name='6'))

    def cached_7():
        ondofig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['温度'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7'))
        situdofig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['相対湿度'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7'))
        nisyafig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['日射'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7'))
        CO2fig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['CO2濃度'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7'))

    def cached_8():
        ondofig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['温度'] ,
                                marker_color='gray',
                                line_width=3,
                                name='8'))
        situdofig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['相対湿度'] ,
                                marker_color='gray',
                                line_width=3,
                                name='8'))
        nisyafig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['日射'] ,
                                marker_color='gray',
                                line_width=3,
                                name='8'))
        CO2fig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['CO2濃度'] ,
                                marker_color='gray',
                                line_width=3,
                                name='8'))

    def cached_9():
        ondofig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['温度'] ,
                                marker_color='olive',
                                line_width=3,
                                name='9'))
        situdofig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['相対湿度'] ,
                                marker_color='olive',
                                line_width=3,
                                name='9'))
        nisyafig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['日射'] ,
                                marker_color='olive',
                                line_width=3,
                                name='9'))
        CO2fig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['CO2濃度'] ,
                                marker_color='olive',
                                line_width=3,
                                name='9'))
    
    
    #温室選ばれた時の応答
    if '1' in stocks:
        cached_1()
    if '2' in stocks:
        cached_2()
    if '3' in stocks:
        cached_3()
    if '4' in stocks:
        cached_4()
    if '5' in stocks:
        cached_5()
    if '6' in stocks:
        cached_6()
    if '7' in stocks:
        cached_7()
    if '8' in stocks:
        cached_8()
    if '9' in stocks:
        cached_9()

    #温度グラフ表示
    # st.subheader('【温度】')
    st.plotly_chart(ondofig)
    #相対湿度グラフ表示
    # st.subheader('【相対湿度】')
    st.plotly_chart(situdofig)
    #日射グラフ表示
    # st.subheader('【日射】')
    st.plotly_chart(nisyafig)
    #CO2濃度グラフ表示
    # st.subheader('【CO2濃度】')
    st.plotly_chart(CO2fig)

