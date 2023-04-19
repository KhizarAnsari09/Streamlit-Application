import streamlit as st

a = st.number_input("Please enter the first number : ", step=1)

b = st.number_input("Please enter the second number : ")

c = st.number_input("Please enter the third number : ")

if(a>b and a>c):
	s = a
elif(b>c and b>a):
	s = b
else:
	s = c

if st.button("Find the largest number !"):
	st.write(f"The largest number is {s}")
