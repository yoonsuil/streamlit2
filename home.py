import streamlit as st 
import pandas as pd  #csv 파일 불러오려면 
import matplotlib.pyplot as plt
import myfunc as my # 내가 만든 파일 호출

st.session_state.id= '윤수일' # 목록 넘겨도 초기화 되지 않는 정보 특별한 데이터를 저장하는 변수를 저장하는 함수 
st.write(st.session_state.id, "님 반갑습니다.")
selected = st.sidebar.selectbox('목차',("체질량 계산기","gapminder","국가별통계"))

if selected == "체질량 계산기":                                      

    st.title('체질량 지수 계산기')
    st.info('체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.')

    height = st.number_input("신장 (cm)",value= 160, step = 3)
    st.write(f"당신의 신장은 : {height} cm입니다.")

    weight = st.number_input("몸무게 (kg)",value= 60, step = 1)
    st.write(f"당신의 몸무게는 : {weight} kg입니다.")


    if st.button("계산하기"):
        bmi=weight/((height/100)**2)
        my.bmi_range(bmi)  # 내가 만든 py 파일 중 .매소드 로 함수 불러오기
        
if selected =="gapminder":
    st.title('gapminder')
    
    st.write("파일 불러오기")
    data =pd.read_csv("gapminder.csv")
    
    year = st.slider("Select a Year",1952,2007,1952,step=5)
    st.write(f"{year}년도")
    
    data = data[data["year"]== year]
    
    #st.write(data)
    
    #fig, ax = plt.subplots()
    #ax.scatter(data['gdpPercap'], data['LifeExp'], s= data['pop']*0.000002)  #s 는 데이터 사이즈 조정   
    #st.pyplot(fig)
    
    df= data[['gdpPercap','lifeExp']]
    st.scatter_chart(df)
    st.write(df)
    
if selected =="국가별통계":
    st.title("국가별통계")

    df =pd.read_csv('gapminder.csv')
    #st.write(df)
    
    country = df['country'].unique()
    #st.write(country)
    
    options = st.multiselect(
        "국가를 선택하세요.",  # 설명
        country,# 선택지 gapminder
        ["Korea, Rep."]) # 선택 리스트 타입으로 저장되는것을 볼수있음.

    st.write("You selected:", options[0]) # options에 리스트 타입으로 들어가있음. 인덱싱
 
    fig, ax = plt.subplots()
    for x in options:
        ax.plot(df[df['country'] ==x ]["year"], df[df['country'] ==x ]["gdpPercap"])# 인덱스 정보 넣으면 
    st.pyplot(fig)    
    
    data = df

    fig1, ax1 = plt.subplots()
    for x in options:
        ax1.plot(range(len(data[data["country"]==x]['lifeExp'])), data[data["country"]==x]['lifeExp'],label=x)
    ax1.legend()
    ax1.set_xticks(range(len(data[data["country"]==x]["pop"])),data[data['country']==x]['year'])
    ax1.set_title('Life Expertancy')
    st.pyplot(fig1)


