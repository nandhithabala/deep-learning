import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import tensorflow as tf

  

def sample():
    return "working"
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(indgred1,indgred2,indgred3,indgred4,indgred5,indgred6,indgred7,indgred8,indgred9,indgred10,indgred11,indgred12,indgred13,indgred14):  
    ingred=[[indgred1,indgred2,indgred3,indgred4,indgred5,indgred6,indgred7,indgred8,indgred9,indgred10,indgred11,indgred12,indgred13,indgred14]]
    model = tf.keras.models.load_model("C:\\Users\\siva\\Downloads\\Model (1).h5")
    result = model.predict(ingred)
    if result == 0:
        a = 'cancer will not occur'
    else:
        a = 'cancer will occur'
    return a
    
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Cuisine Classification")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Cancer Classification  </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    indgred1= st.number_input("indgedients1")
    indgred2= st.number_input("indgedients2")
    indgred3= st.number_input("indgedients3")
    indgred4= st.number_input("indgedients4")
    indgred5= st.number_input("indgedients5")
    indgred6= st.number_input("indgedients6")
    indgred7= st.number_input("indgedients7")
    indgred8= st.number_input("indgedients8")
    indgred9= st.number_input("indgedients9")
    indgred10= st.number_input("indgedients10")
    indgred11= st.number_input("indgedients11")
    indgred12= st.number_input("indgedients12")
    indgred13= st.number_input("indgedients13")
    indgred14= st.number_input("indgedients14")

    result=""
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
   # sample()
    if st.button("Predict"):
        result = prediction(indgred1,indgred2,indgred3,indgred4,indgred5,indgred6,indgred7,indgred8,indgred9,indgred10,indgred11,indgred12,indgred13,indgred14)
    st.success('The Cuisine is {}'.format(result))
     
if __name__=='__main__':
    main()