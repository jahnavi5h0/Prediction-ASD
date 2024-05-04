import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
def app():
    #st.header("Form")      
    autism_dataset=pd.read_csv('C:\\Users\\91939\\Downloads\\Project\\spect.csv')  
    x=autism_dataset.drop(columns='Class',axis=1)
    Y=autism_dataset['Class']
    #spliting the data
    x_train,x_test,y_train,y_test=train_test_split(x,Y,test_size=0.20,stratify=Y,random_state=101)
    ada=AdaBoostClassifier(n_estimators=500)
    ada.fit(x_train,y_train)
    predictions_ada=ada.predict(x_test)
    acc_ada=accuracy_score(y_true=y_test,y_pred=predictions_ada)
    def valuecount(str):
        if str=="yes":
            return 1
        else:
            return 0
    def Gender(str):   
        if str=="female":
            return 1
        else:
            return 0
    #form layout
    #a1:Does your child look at you when you call his/her name?
    #a2:How easy is it for you to get eye contact with your child? 
    #a3:Does your child point to indicate that s/he wants something? (e.g. a toy that is out of reach) 
    #a4:A4	Does your child point to share interest with you? (e.g. poin9ng at an interes9ng sight) 
    #a5:A5	Does your child pretend? (e.g. care for dolls, talk on a toy phone) 
    #a6:Does your child follow where you’re looking? 
    #a7:A7	If you or someone else in the family is visibly upset, does your child show signs of wan9ng to comfort them? (e.g. stroking hair, hugging them)
    #a8:A8	Would you describe your child’s first words as: 
    #a9"Does your child use simple gestures? (e.g. wave goodbye) 
    #a10:Does your child stare at nothing with no apparent purpose? 
    #11:slect the age
    #12:select the gender
    #13:Does child has jaundice
    #14:Does your family members have ASD
    #15:who complete the test
    d1=["Select","No","yes"]
    val1=st.selectbox("Does your child look at you when you call his/her name?",d1)    
    val1=valuecount(val1)

    val2=st.selectbox("is it easy for you to get eye contact with your child?",d1)    
    val2=valuecount(val2)

    val3=st.selectbox("Does your child point to indicate that she/he wants something? (e.g. a toy that is out of reach) ",d1)    
    val3=valuecount(val3)

    val4=st.selectbox("Does your child point to share interest with you? (e.g. pointing at an interesting sight) ",d1)    
    val4=valuecount(val4)

    val5=st.selectbox("Does your child pretend? (e.g. care for dolls, talk on a toy phone) ",d1)    
    val5=valuecount(val5)

    val6=st.selectbox("Does your child follow where you’re looking?",d1)    
    val6=valuecount(val6)

    val7=st.selectbox("If you or someone else in the family is visibly upset, does your child show signs of waning to comfort them? (e.g. stroking hair, hugging them)",d1)    
    val7=valuecount(val7)

    val8=st.selectbox("Would you describe your child’s first words?",d1)    
    val8=valuecount(val8)

    val9=st.selectbox("Does your child use simple gestures? (e.g. wave goodbye) ",d1)    
    val9=valuecount(val9)

    val10=st.selectbox("Does your child sometimes look at nothing for no reason? ",d1)    
    val10=valuecount(val10)

    d2=[12,22,24,28,31,36]
    val11=st.selectbox("select age",d2)

    d3=["select","Female","Male"]
    val12 = st.selectbox("Gender  ",d3)
    val12 = Gender(val12)

    val13=st.selectbox("Does child has jaundice",d1)
    val13=valuecount(val13)

    val14=st.selectbox("Does your family members have ASD",d1)    
    val14=valuecount(val14)
    
    def T(str):   
        if str=="family member":
            return 0
        elif str=="Health care professional":
            return 1
        elif str=="Self":
            return 2
        elif str=="Others":
            return 3
    
    d4=["select","family member","Health care professional","Self","Others"]

    val15=st.selectbox("who complete the test",d4)
    val15=T(val15)


    input_data = [val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15]
    input_data_as_numpy_array=np.array(input_data)
    reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction=ada.predict(reshaped)

    with st.expander("Analyse provided data"):
        st.subheader("Results:")

        if (prediction[0] == 0):
            st.info('The person is not with Autism spectrum disorder')
        else:
            st.warning('The person is with Autism spectrum disorder')