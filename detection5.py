    # -*- coding: utf-8 -*-
    """
    Created on Thu Sep 30 16:23:49 2021
    
    @author: ACER
    """
    
    import pickle
    import streamlit as st
     
    # loading the trained model
    pickle_in = open('fraud4.pkl', 'rb') 
    classifier = pickle.load(pickle_in)
    @st.cache
     
    # defining the function which will make the p   rediction using the data which the user inputs 
    def prediction(AC_1001_Issue, AC_1002_Issue, AC_1003_Issue, TV_2001_Issue,
        TV_2002_Issue, TV_2003_Issue, Claim_Value, Service_Centre,
        Product_Age, Call_details, State_Chennai, State_Hyderabad,
        State_Mumbai,State_Bangalore,State_Kochi,State_Lucknow,
        State_Kolkata,State_Bhubaneswar, State_Vijayawada,
        State_Ahmedabad,City_Maharashtra,
        City_Karnataka,City_Gujarat,City_Kerala,
        City_Delhi, City_Bihar, Region_East,
        Region_North,Region_South,Region_West,
        Area_Rural, Area_Urban, Consumer_profile_Business,
        Consumer_profile_Personal, Product_category_Entertainment,
        Product_category_Household,Product_type_AC,Product_type_TV,
        Purchased_from_Dealer, Purchased_from_Internet,
        Purchased_from_Manufacturer, Purpose_Claim, Purpose_Complaint,
        Purpose_Other):   
        
        City_Maharashtra,City_Karnataka,City_Gujarat,City_Kerala,
        City_Delhi, City_Bihar=0,0,0,0,0,0
        if City==Maharashtra:
           City_Maharashtra=1
        elif City==Karnataka:
            City_Karnataka=1
        elif City==Gujarat:
            City_Gujarat=1
        elif City==Kerala:
             City_Kerala=1
        elif City==Delhi:
             City_Delhi=1
        elif City==Bihar:
             City_Bihar=1
        State_Chennai, State_Hyderabad, State_Mumbai,State_Bangalore,State_Kochi,State_Lucknow,
        State_Kolkata,State_Bhubaneswar, State_Vijayawada,
        State_Ahmedabad =0,0,0,0,0,0,0,0,0,0
        if State==Chennai:
           State_Chennai==1
        elif State==Hyderabad:
             State_Hyderabad=1
        elif State==Mumbai:
             State_Mumbai=1
        elif State==Bangalore:
             State_Bangalore=1
        elif State==Kochi:
             State_Kochi=1
        elif State==Lucknow:
             State_Lucknow=1
        elif State==Kolkata:
             State_Kolkata=1
        elif State==Bhubaneswar:
             State_Bhubaneswar=1
        elif State==Vijayawada:
             State_Vijayawada=1
        elif State==Ahmedabad:
             State_Ahmedabad=1
        
          # Making predictions 
        prediction = classifier.predict([[AC_1001_Issue, AC_1002_Issue, AC_1003_Issue, TV_2001_Issue,
        TV_2002_Issue, TV_2003_Issue, Claim_Value, Service_Centre,
        Product_Age, Call_details, State_Chennai, State_Hyderabad,
        State_Mumbai,State_Bangalore,State_Kochi,State_Lucknow,
        State_Kolkata,State_Bhubaneswar, State_Vijayawada,
        State_Ahmedabad,
        City_Maharashtra,
        City_Karnataka,City_Gujarat,City_Kerala,
        City_Delhi, City_Bihar, Region_East,
        Region_North,
        Region_South,Region_West,
        Area_Rural, Area_Urban, Consumer_profile_Business,
        Consumer_profile_Personal, Product_category_Entertainment,
        Product_category_Household,Product_type_AC,Product_type_TV,
        Purchased_from_Dealer, Purchased_from_Internet,
        Purchased_from_Manufacturer, Purpose_Claim, Purpose_Complaint,
        Purpose_Other]])      
        if prediction == 0:
           pred = 'Fraud'
        else:
           pred = 'notFraud'
        return pred
    # this is the main function in which we define our webpage  
    def main():       
        # front end elements of the web page 
        html_temp = """ 
        <div style ="background-color:yellow;padding:13px"> 
        <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
        </div> 
        """
          
        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html = True)
         # following lines create boxes in which user can enter data required to make prediction 
        City=st.selectbox('City',options=['Maharashtra',
           'Karnataka', 'Gujarat', 'Kerala', 'Uttar Pradesh',
           'Delhi', 'Bihar',])
        State=st.selectbox('state',options=['Chennai', 'Hyderabad',
           'Mumbai', 'Bangalore', 'Kochi', 'Lucknow',
           'Kolkata', 'Bhubaneswar', 'Vijayawada',
           'Ahmedabad'])
        call_details=st.text_input('Calldetails',"Type Here")
        service_center=st.text_input('service center',"Type Here")
        Product_Age=st.text_input('productage',"Type Here")
        Claim_Value=st.text_input('Claimvalue',"Type Here")
        result =""
          
        # when 'Predict' is clicked, make the prediction and store it 
        if st.button("Predict"): 
           result = prediction(AC_1001_Issue, AC_1002_Issue, AC_1003_Issue, TV_2001_Issue,
           TV_2002_Issue, TV_2003_Issue, Claim_Value, Service_Centre,
           Product_Age, Call_details, State_Chennai, State_Hyderabad,
           State_Mumbai,State_Bangalore,State_Kochi,State_Lucknow,
           State_Kolkata,State_Bhubaneswar, State_Vijayawada,
           State_Ahmedabad,City_Maharashtra,
           City_Karnataka,City_Gujarat,City_Kerala,
           City_Delhi, City_Bihar, Region_East,
           Region_North,
           Region_South,Region_West,
           Area_Rural, Area_Urban, Consumer_profile_Business,
           Consumer_profile_Personal, Product_category_Entertainment,
           Product_category_Household,Product_type_AC,Product_type_TV,
           Purchased_from_Dealer, Purchased_from_Internet,
           Purchased_from_Manufacturer, Purpose_Claim, Purpose_Complaint,
           Purpose_Other)
           st.success(result)
           print(result)
    if __name__=='__main__': 
          main()