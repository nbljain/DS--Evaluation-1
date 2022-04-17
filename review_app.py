import streamlit as st

import pandas as pd

import numpy as np

st.write("""
# Inaccurate Rating Prediction App
This app predicts the **Inaccurate** Ratings!
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        
        ID = st.sidebar.selectbox('ID', list((range(3886,684991))))
        
        Star = st.sidebar.selectbox('Star',list(range(1,5)))
        
        data = {'ID':ID,
                
               'Star':Star
                }             
        features = pd.DataFrame(data, index=[0])
        
        return features
    
    input_df = user_input_features()


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib

def make_hashes(password):
    
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    
	if make_hashes(password) == hashed_text:
        
		return hashed_text
    
	return False

# DB Management
import sqlite3 

conn = sqlite3.connect('data.db')

c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	#st.title("User Authentication Login")

	menu = ["Home","Login","SignUp"]
    
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		#st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
    
   
       #st.write(cleaned_data)
st.write(input_df)
#st.subheader('Prediction')
cleaned_data= pd.read_csv('Cleaned_reviews.csv')
predict = st.selectbox("Predict",["Incorrect Review","None"])
if predict == "Incorrect Review":
           #st.subheader('Prediction')  
   st.write(cleaned_data)