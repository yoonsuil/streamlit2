
import streamlit as st


def bmi_range(bmi):
    st.write(f'당신의 체질량지수는 {bmi:.2f}입니다.')
    
    if bmi >=18.5 and bmi<=22.9 :
        st.success('정상입니다.',icon="✅")
    elif bmi <=18.5 :
        st.warning('저체중입니다.', icon="⚠️")
    else:
        st.error('비만입니다.',icon="🚨")
        st.image('sunrise.jpeg',caption='산타고 운동하세요.')
    st.balloons()