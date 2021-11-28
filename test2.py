# https://es.acervolima.com/2021/02/09/una-guia-para-principiantes-de-streamlit/





import streamlit as st 

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
   .sidebar .sidebar-content {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
    </style>
    """,
    unsafe_allow_html=True
)
  
st.title("Hello GeeksForGeeks !!!") 
st.header("This is a header")  
  
st.subheader("This is a subheader") 
st.text("Hello GeeksForGeeks!!!")
st.markdown("### This is a markdown") 
st.success("Success") 
  
st.info("Information") 
  
st.warning("Warning") 
  
st.error("Error")
st.write("Text with write") 
  
st.write(range(10)) 

from PIL import Image 
#img = Image.open("streamlit.png") 
  
#st.image(img, width=200) 



if st.checkbox("Show/Hide"): 
    
  
  st.text("Showing the widget") 


status = st.radio("Select Gender: ",('Male', 'Female')) 
  
if (status == 'Male'): 
    st.success("Male") 
else: 
    st.success("Female") 


hobby = st.selectbox("Hobbies: ", 
                     ['Dancing', 'Reading', 'Sports']) 
  
st.write("Your hobby is: ", hobby) 



hobbies = st.multiselect("Hobbies: ", 
                         ['Dancing', 'Reading', 'Sports']) 
  
st.write("You selected", len(hobbies), 'hobbies') 


st.button("Click me for no reason") 
  
if(st.button("About")): 
    st.text("Welcome To GeeksForGeeks!!!") 




name = st.text_input("Enter Your name", "Type Here ...") 
  
if(st.button('Submit')): 
    result = name.title() 
    st.success(result) 


level = st.slider("Select the level", 1, 5) 
  
st.text('Selected: {}'.format(level)) 



import streamlit as st 
  
st.title('Welcome to BMI Calculator') 
  
weight = st.number_input("Enter your weight(in kgs)") 
  
status = st.radio('Select your height format: ', 
                  ('cms', 'meters', 'feet')) 
  
if(status == 'cms'): 
    
    height = st.number_input('Centimeters') 
      
    try: 
        bmi = weight / ((height/100)**2) 
    except: 
        st.text("Enter some value of height") 
          
elif(status == 'meters'): 
    
    height = st.number_input('Meters') 
      
    try: 
        bmi = weight / (height ** 2) 
    except: 
        st.text("Enter some value of height") 
          
else: 
    
    height = st.number_input('Feet') 
      
    
    try: 
        bmi = weight / (((height/3.28))**2) 
    except: 
        st.text("Enter some value of height") 
  
if(st.button('Calculate BMI')): 
      
    
    st.text("Your BMI Index is {}.".format(bmi)) 
      
    
    if(bmi < 16): 
        st.error("You are Extremely Underweight") 
    elif(bmi >= 16 and bmi < 18.5): 
        st.warning("You are Underweight") 
    elif(bmi >= 18.5 and bmi < 25): 
        st.success("Healthy")         
    elif(bmi >= 25 and bmi < 30): 
        st.warning("Overweight") 
    elif(bmi >= 30): 
        st.error("Extremely Overweight") 





fill_in_the_blanks = {'questions': ['question1','question2'], 'answers': ['answer1','answer2']}
ans = []
mark = 0
with st.form(key = id_generator()):
	for i,quest in enumerate(fill_in_the_blanks["questions"]):
		st.write(i+1,quest)
		x = st.text_input("Enter your answer here",key=id_generator())
		ans.append(x)
	submitted = st.form_submit_button(label='Submit')
	if submitted:
		# if answers are correct then
			mark = mark+1
	st.success("Test Score - "+str(mark))
