import streamlit as st
import pandas as pd
import plotly.graph_objects as go

#ページ初期設定
st.set_page_config(page_title="環境分析",layout="wide",initial_sidebar_state="auto")

 #レイアウト設定 
layout_Ondo = go.Layout(title=dict(text='<b>【温度】'),
                    yaxis = dict(side = 'left',range = [0, 55]),
                    font=dict(size=15),
                    legend=dict(xanchor='left',
                    yanchor='bottom',
                    x=0.32,
                    y=1.0,
                    orientation='h'    
                    ),width=900,height=700)
layout_Situdo = go.Layout(title=dict(text='<b>【相対湿度】'),
                    yaxis = dict(side = 'left',range = [0, 110]),
                    font=dict(size=15),
                    legend=dict(xanchor='left',
                    yanchor='bottom',
                    x=0.32,
                    y=1.0,
                    orientation='h'    
                    ),width=900,height=700)
layout_Nisya = go.Layout(title=dict(text='<b>【日射】'),
                    yaxis = dict(side = 'left', range = [0,1100]),
                    font=dict(size=15),
                    legend=dict(xanchor='left',
                    yanchor='bottom',
                    x=0.32,
                    y=1.0,
                    orientation='h'    
                    ),width=900,height=700)
layout_Co2 = go.Layout(title=dict(text='<b>【CO2濃度】'),
                    yaxis = dict(side = 'left', range = [0,1000]),
                    font=dict(size=15),
                    legend=dict(xanchor='left',
                    yanchor='bottom',
                    x=0.32,
                    y=1.0,
                    orientation='h'    
                    ),width=900,height=700)
                            
#タイトル
st.title("環境分析")

# データフレーム読み込み
st.sidebar.write("""## ファイルアップロード""")
uploaded_file0 = st.sidebar.file_uploader("ファイル➀をアップロードしてください", type='csv',key=0)
with st.sidebar.expander("複数ファイルをアップロード"):
        # チェックが入っているときはデータフレームを書き出す
        uploaded_file1 = st.file_uploader("ファイル➁をアップロードしてください.", type='csv',key=1)
        uploaded_file2 = st.file_uploader("ファイル➂をアップロードしてください.", type='csv',key=2)

#表示グラフの切り替え
listgrafu = ['データ別4グラフ','相関2軸グラフ','前日比較グラフ','複数ファイルグラフ']
grafustock = st.selectbox(label="表示グラフを選択してください",options=listgrafu,key=3)

#1つ目のファイル読み込み
if uploaded_file0:
    @st.cache
    def readcsv():
        return  pd.read_csv(uploaded_file0, encoding="shift-jis", index_col=[0], parse_dates=[0])
    df_readfile = readcsv()
    #温室ごとに定義
    @st.cache
    def ex1():
        return df_readfile[df_readfile["温室"] == 1]
    @st.cache
    def ex2():
        return df_readfile[df_readfile["温室"] == 2]
    @st.cache
    def ex3():
        return df_readfile[df_readfile["温室"] == 3]
    @st.cache
    def ex4():
        return df_readfile[df_readfile["温室"] == 4]
    @st.cache
    def ex5():
        return df_readfile[df_readfile["温室"] == 5]
    @st.cache
    def ex6():
        return df_readfile[df_readfile["温室"] == 6]
    @st.cache
    def ex7():
        return df_readfile[df_readfile["温室"] == 7]
    @st.cache
    def ex8():
        return df_readfile[df_readfile["温室"] == 8]
    @st.cache
    def ex9():
        return df_readfile[df_readfile["温室"] == 9]

    df_ex1 =  ex1()
    df_ex2 =  ex2()
    df_ex3 =  ex3()
    df_ex4 =  ex4()
    df_ex5 =  ex5()
    df_ex6 =  ex6()
    df_ex7 =  ex7()
    df_ex8 =  ex8()
    df_ex9 =  ex9()
    df_readfile0 = readcsv()

#2つ目のファイル読み込み
if uploaded_file1:
    @st.cache()
    def readcsv1():
        return  pd.read_csv(uploaded_file1, encoding="shift-jis",index_col=[0],parse_dates=[0])
    df_readfile1 = readcsv1()

#3つ目のファイル読み込み
if uploaded_file2:
    @st.cache()
    def readcsv2():
        return  pd.read_csv(uploaded_file2, encoding="shift-jis",index_col=[0],parse_dates=[0])
    df_readfile2 = readcsv2()

#===============データ別4グラフ=======================
if uploaded_file0 and 'データ別4グラフ' in grafustock:
    #ヘッダー
    st.header("【温度・日射・相対湿度・CO2濃度のグラフ】")

    #サイドバーの日付選ぶ
    st.sidebar.write("""## 表示日付・温室選択""")
    select_dates = st.sidebar.date_input('表示日付の選択',value=(df_ex1.index[0],df_ex1.index[-1]),min_value=df_ex1.index[0],max_value=df_ex1.index[-1])

    #温室番号選ぶ
    list = ['1','2','3','4','5','6','7','8','9']
    stocks = st.sidebar.multiselect(label="温室番号の選択",
                options = list,
                default=['1','2','3','4','5','6','7','8','9'])
    if not stocks:
        st.error('少なくとも1つの温室番号を選んでください。')

    #温室ごとグラフデータ定義
    ondofig = go.Figure(layout=layout_Ondo)
    situdofig = go.Figure(layout=layout_Situdo)
    nisyafig = go.Figure(layout=layout_Nisya)
    CO2fig = go.Figure(layout=layout_Co2)

    def process_1():
        ondofig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['温度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['相対湿度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['日射'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex1[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex1['CO2濃度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',
                                yaxis='y1'))
    def process_2():
        ondofig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['温度'] ,
                                marker_color='darkorange',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['相対湿度'] ,
                                marker_color='darkorange',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['日射'] ,
                                marker_color='darkorange',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex2[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex2['CO2濃度'] ,
                                marker_color='darkorange',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
    def process_3():
        ondofig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['温度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['相対湿度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['日射'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex3[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex3['CO2濃度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3',
                                yaxis='y1'))
    def process_4():
        ondofig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['温度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='4',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['相対湿度'] ,
                                marker_color='red',
                                line_width=3,
                                name='4',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['日射'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='4',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex4[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex4['CO2濃度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='4',
                                yaxis='y1'))
    def process_5():
        ondofig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['温度'] ,
                                marker_color='mediumpurple',
                                line_width=3,
                                name='5',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['相対湿度'] ,
                                marker_color='mediumpurple',
                                line_width=3,
                                name='5',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['日射'] ,
                                marker_color='mediumpurple',
                                line_width=3,
                                name='5',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex5[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex5['CO2濃度'] ,
                                marker_color='mediumpurple',
                                line_width=3,
                                name='5',
                                yaxis='y1'))
    def process_6():
        ondofig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['温度'] ,
                                marker_color='tan',
                                line_width=3,
                                name='6',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['相対湿度'] ,
                                marker_color='tan',
                                line_width=3,
                                name='6',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['日射'] ,
                                marker_color='tan',
                                line_width=3,
                                name='6',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex6[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex6['CO2濃度'] ,
                                marker_color='tan',
                                line_width=3,
                                name='6',
                                yaxis='y1'))
    def process_7():
        ondofig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['温度'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['相対湿度'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['日射'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex7[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex7['CO2濃度'] ,
                                marker_color='pink',
                                line_width=3,
                                name='7',
                                yaxis='y1'))
    def process_8():
        ondofig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['温度'] ,
                                marker_color='slategray',
                                line_width=3,
                                name='8',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['相対湿度'] ,
                                marker_color='slategray',
                                line_width=3,
                                name='8',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['日射'] ,
                                marker_color='slategray',
                                line_width=3,
                                name='8',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex8[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex8['CO2濃度'] ,
                                marker_color='slategray',
                                line_width=3,
                                name='8',
                                yaxis='y1'))
    def process_9():
        ondofig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['温度'] ,
                                marker_color='rosybrown',
                                line_width=3,
                                name='9',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['相対湿度'] ,
                                marker_color='rosybrown',
                                line_width=3,
                                name='9',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['日射'] ,
                                marker_color='rosybrown',
                                line_width=3,
                                name='9',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex9[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=df_ex9['CO2濃度'] ,
                                marker_color='rosybrown',
                                line_width=3,
                                name='9',
                                yaxis='y1'))
                                
    #温室選ばれた時の応答
    if '1' in stocks:
        process_1()
    if '2' in stocks:
        process_2()
    if '3' in stocks:
        process_3()
    if '4' in stocks:
        process_4()
    if '5' in stocks:
        process_5()
    if '6' in stocks:
        process_6()
    if '7' in stocks:
        process_7()
    if '8' in stocks:
        process_8()
    if '9' in stocks:
        process_9()

    #温度グラフ表示
    st.plotly_chart(ondofig)
    #日射グラフ表示
    st.plotly_chart(nisyafig)
    #相対湿度グラフ表示
    st.plotly_chart(situdofig)
    #CO2濃度グラフ表示
    st.plotly_chart(CO2fig)


#===============相関2軸グラフ=======================
if uploaded_file0 and '相関2軸グラフ' in grafustock:
    #ヘッダー
    st.header("相関2軸グラフ")

    st.sidebar.write("""## 表示日付・温室選択""")
    select_dates = st.sidebar.date_input('表示日付の選択',value=(df_ex1.index[0],df_ex1.index[-1]),min_value=df_ex1.index[0],max_value=df_ex1.index[-1])
    
    #温室番号選ぶ
    listnum = ['1','2','3','4','5','6','7','8','9']
    stocks = st.sidebar.selectbox(label="温室番号の選択",options = listnum)

    if '1' in stocks:
        chooseonsitu = df_ex1
    if '2' in stocks:
        chooseonsitu = df_ex2
    if '3' in stocks:
        chooseonsitu = df_ex3
    if '4' in stocks:
        chooseonsitu = df_ex4
    if '5' in stocks:
        chooseonsitu = df_ex5
    if '6' in stocks:
        chooseonsitu = df_ex6
    if '7' in stocks:
        chooseonsitu = df_ex7
    if '8' in stocks:
        chooseonsitu = df_ex8
    if '9' in stocks:
        chooseonsitu = df_ex9

    #温室ごとグラフデータ定義
    a1 = go.Scattergl(x=chooseonsitu[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y= chooseonsitu['温度'] ,
                                marker_color='orangered',
                                line_width=3,
                                yaxis='y1',
                                name='温度')
    a2= go.Scattergl(x=chooseonsitu[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=chooseonsitu['相対湿度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                yaxis='y1',
                                name='相対湿度')
    a3 = go.Scattergl(x=chooseonsitu[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=chooseonsitu['日射'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                yaxis='y2',
                                name='日射')
    a4= go.Scattergl(x=chooseonsitu[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=chooseonsitu['CO2濃度'] ,
                                marker_color='darkorange',
                                line_width=3,
                                yaxis='y2',
                                name='CO2濃度')
    #レイアウト設定
    layout = go.Layout(title=dict(text='<b>【相関グラフ】'),xaxis = dict(title = '日付'), font=dict(size=15),
              yaxis1 = dict(side = 'left',showgrid=False,range = [0, 110]),                            
              yaxis2 = dict(side = 'right', overlaying = 'y1', range = [0,1100],showgrid=False),
              legend=dict(xanchor='left',yanchor='bottom',x=0.32,y=1.0,orientation='h'))
    #グラフ表示
    fig = dict(data = [a1, a2, a3, a4],layout= layout)
    st.plotly_chart(fig,width=900,height=1200)


#===============前日比較グラフ=======================
if uploaded_file0 and '前日比較グラフ' in grafustock:
    #ヘッダー
    st.header("前日比較グラフ")
    #サイドバーの日付選ぶ
    st.sidebar.write("""## 表示日付・温室選択""")
    #指定日の指定
    MMdd_list = sorted(set(df_ex1['月日'].to_list()))
    select_dates = st.sidebar.selectbox('表示日付の選択',MMdd_list)
    #指定日の前日
    if select_dates == MMdd_list[0]:
        secondselect_dates_index = MMdd_list.index(select_dates)
    else:
        secondselect_dates_index = MMdd_list.index(select_dates) - 1
    
    secondselect_dates = MMdd_list[secondselect_dates_index]

    #温室番号選ぶ
    listnum = ['1','2','3','4','5','6','7','8','9']
    stocks = st.sidebar.selectbox(label="温室番号の選択",
                options = listnum)

    if '1' in stocks:
        selectday = df_ex1[df_ex1['月日'] == select_dates]
        yesterday = df_ex1[df_ex1['月日'] == secondselect_dates]
    if '2' in stocks:
        selectday = df_ex2[df_ex2['月日'] == select_dates]
        yesterday = df_ex2[df_ex2['月日'] == secondselect_dates]
    if '3' in stocks:
        selectday = df_ex3[df_ex3['月日'] == select_dates]
        yesterday = df_ex3[df_ex3['月日'] == secondselect_dates]
    if '4' in stocks:
        selectday = df_ex4[df_ex4['月日'] == select_dates]
        yesterday = df_ex4[df_ex4['月日'] == secondselect_dates]
    if '5' in stocks:
        selectday = df_ex5[df_ex5['月日'] == select_dates]
        yesterday = df_ex5[df_ex5['月日'] == secondselect_dates]
    if '6' in stocks:
        selectday = df_ex6[df_ex6['月日'] == select_dates]
        yesterday = df_ex6[df_ex6['月日'] == secondselect_dates]
    if '7' in stocks:
        selectday = df_ex7[df_ex7['月日'] == select_dates]
        yesterday = df_ex7[df_ex7['月日'] == secondselect_dates]
    if '8' in stocks:
        selectday = df_ex8[df_ex8['月日'] == select_dates]
        yesterday = df_ex8[df_ex8['月日'] == secondselect_dates]
    if '9' in stocks:
        selectday = df_ex9[df_ex9['月日'] == select_dates]
        yesterday = df_ex9[df_ex9['月日'] == secondselect_dates]
    
    #レイアウト設定
    layout = go.Layout(title=dict(text='<b>【比較グラフ】'),xaxis = dict(title = '日付'), font=dict(size=15),
              yaxis1 = dict(side = 'left', showgrid=False,range = [0, 110]),                            
              legend=dict(xanchor='left',yanchor='bottom',x=0.32,y=1.0,orientation='h'))

    #温室ごとグラフデータ定義
    ondofig = go.Figure(layout=layout_Ondo)
    situdofig = go.Figure(layout=layout_Situdo)
    nisyafig = go.Figure(layout=layout_Nisya)
    CO2fig = go.Figure(layout=layout_Co2)

    def ondo():
        ondofig.add_traces(go.Scattergl(x=selectday["時間"],
                                y= selectday['温度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                yaxis='y1',
                                name=select_dates))
        ondofig.add_traces(go.Scattergl(x=yesterday["時間"],
                                y=yesterday['温度'] ,
                                marker_color='orangered',
                                line_width=3,
                                yaxis='y1',
                                name=secondselect_dates))
    def nisya():
         nisyafig.add_traces(go.Scattergl(x=selectday["時間"],
                                y= selectday['日射'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                yaxis='y1',
                                name=select_dates))
         nisyafig.add_traces(go.Scattergl(x=yesterday["時間"],
                                y=yesterday['日射'] ,
                                marker_color='orangered',
                                line_width=3,
                                yaxis='y1',
                                name=secondselect_dates))
    def situdo():
         situdofig.add_traces(go.Scattergl(x=selectday["時間"],
                                y= selectday['相対湿度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                yaxis='y1',
                                name=select_dates))
         situdofig.add_traces(go.Scattergl(x=yesterday["時間"],
                                y=yesterday['相対湿度'] ,
                                marker_color='orangered',
                                line_width=3,
                                yaxis='y1',
                                name=secondselect_dates))
    def CO2():
        CO2fig.add_traces(go.Scattergl(x=selectday["時間"],
                                y= selectday['CO2濃度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                yaxis='y1',
                                name=select_dates)) 
        CO2fig.add_traces(go.Scattergl(x=yesterday["時間"],
                                y=yesterday['CO2濃度'] ,
                                marker_color='orangered',
                                line_width=3,
                                yaxis='y1',
                                name=secondselect_dates))   
    ondo()
    nisya()
    situdo()
    CO2()
    #温度グラフ表示
    st.plotly_chart(ondofig)
    #日射グラフ表示
    st.plotly_chart(nisyafig)
    #相対湿度グラフ表示
    st.plotly_chart(situdofig)
    #CO2濃度グラフ表示
    st.plotly_chart(CO2fig)


#===============3ファイル比較グラフ=======================
if uploaded_file0 and uploaded_file1 and uploaded_file2 and '複数ファイルグラフ' in grafustock:
    #ヘッダー
    st.header("3ファイルグラフ")
    #サイドバーの温室番号選ぶ
    listnum = ['1','2','3','4','5','6','7','8','9']
    stocks = st.sidebar.selectbox(label="温室番号の選択",
                options = listnum)
    select_onsitu = int(stocks[0])

    #温室の識別
    def ex0():
        return df_readfile0[df_readfile0["温室"] == select_onsitu]
    def ex1():
        return df_readfile1[df_readfile1["温室"] == select_onsitu]
    def ex2():
        return df_readfile2[df_readfile2["温室"] == select_onsitu]
    df_ex0 = ex0()
    df_ex1 = ex1()
    df_ex2 = ex2()

    #ヘッダー
    st.header("温度・相対湿度・日射・CO2濃度のグラフ")

    #温室ごとグラフデータ定義
    ondofig = go.Figure(layout=layout_Ondo)
    situdofig = go.Figure(layout=layout_Situdo)
    nisyafig = go.Figure(layout=layout_Nisya)
    CO2fig = go.Figure(layout=layout_Co2)

    def hikaku1():
        ondofig.add_traces(go.Scattergl(x=df_ex0["月日時間"],
                                y=df_ex0['温度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',))
        situdofig.add_traces(go.Scattergl(x=df_ex0["月日時間"],
                                y=df_ex0['相対湿度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1'
                                ))
        nisyafig.add_traces(go.Scattergl(x=df_ex0["月日時間"],
                                y=df_ex0['日射'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex0["月日時間"],
                                y=df_ex0['CO2濃度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1'))

        ondofig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y=df_ex1['温度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2',))
        situdofig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y=df_ex1['相対湿度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2'
                                ))
        nisyafig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y=df_ex1['日射'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2'))
        CO2fig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y=df_ex1['CO2濃度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2'))

        ondofig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['温度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3'))
        situdofig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['相対湿度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3'))
        nisyafig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['日射'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3'))
        CO2fig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['CO2濃度'] ,
                                marker_color='mediumseagreen',
                                line_width=3,
                                name='3'))
    hikaku1()

    #温度グラフ表示
    st.plotly_chart(ondofig)
    #日射グラフ表示
    st.plotly_chart(nisyafig)
    #相対湿度グラフ表示
    st.plotly_chart(situdofig)
    #CO2濃度グラフ表示
    st.plotly_chart(CO2fig)

#===============2ファイル比較グラフ=======================
if uploaded_file0 and uploaded_file1 and not uploaded_file2 and '複数ファイルグラフ' in grafustock:
    #ヘッダー
    st.header("2ファイル比較グラフ")

    #サイドバーの温室番号選ぶ
    listnum = ['1','2','3','4','5','6','7','8','9']
    stocks = st.sidebar.selectbox(label="温室番号の選択",
                options = listnum,key=4)
    select_onsitu = int(stocks[0])

    #温室の識別
    def ex1():
        return df_readfile0[df_readfile0["温室"] == select_onsitu]
    def ex2():
        return df_readfile1[df_readfile1["温室"] == select_onsitu]
    df_ex1 = ex1()
    df_ex2 = ex2()

    #温室ごとグラフデータ定義
    ondofig = go.Figure(layout=layout_Ondo)
    situdofig = go.Figure(layout=layout_Situdo)
    nisyafig = go.Figure(layout=layout_Nisya)
    CO2fig = go.Figure(layout=layout_Co2)

    def hikaku2():
        ondofig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y= df_ex1['温度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                yaxis='y1',
                                name='1'))
        situdofig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y=df_ex1['相対湿度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y=df_ex1['日射'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex1["月日時間"],
                                y=df_ex1['CO2濃度'] ,
                                marker_color='dodgerblue',
                                line_width=3,
                                name='1',
                                yaxis='y1'))

        ondofig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['温度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
        situdofig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['相対湿度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
        nisyafig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['日射'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
        CO2fig.add_traces(go.Scattergl(x=df_ex2["月日時間"],
                                y=df_ex2['CO2濃度'] ,
                                marker_color='orangered',
                                line_width=3,
                                name='2',
                                yaxis='y1'))
    hikaku2()

    #温度グラフ表示
    st.plotly_chart(ondofig)
    #日射グラフ表示
    st.plotly_chart(nisyafig)
    #相対湿度グラフ表示
    st.plotly_chart(situdofig)
    #CO2濃度グラフ表示
    st.plotly_chart(CO2fig)

#================エラー回避=====================
if not uploaded_file0 and not uploaded_file1 and not uploaded_file2 and '複数ファイルグラフ' in grafustock:
    st.write("ファイルをアップロードしてください")
if uploaded_file0 and not uploaded_file1 and not uploaded_file2 and '複数ファイルグラフ' in grafustock:
    st.write("ファイルをアップロードしてください")