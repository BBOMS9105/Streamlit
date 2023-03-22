# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd

def main():
    '''코드 작성'''
    st.title("Hello Universe!")

    st.text('this is {}'.format('good'))

    st.header('This is header')

    st.subheader('This is subHeader')

    st.markdown('## This is Markdown Header')

    # Colored Text
    st.success('성공')

    st.warning('경고')

    st.info('This is information')

    st.error('This is an error')

    d = st.date_input(
        "When\'s your birthday",
        datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)

if __name__ == "__main__":
    main()
