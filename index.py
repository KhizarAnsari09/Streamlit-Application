import streamlit as st

a = st.number_input("Please enter number 1: ")

b = st.number_input("Please enter number 2: ")

c = st.number_input("Please enter number 3: ")

if(a>b and a>c):
	print(a)
elif(b>c and b>a):
	print(b)
else:
	print(c)