import streamlit as st

from streamlit_option_menu import option_menu


import AboutAutism, Form, Precautions
st.set_page_config(
        page_title="Autism Spectrum Disorder",
)



class MultiApp:

    def _init_(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Home',
                options=['AboutAutism', 'Form', 'Precautions'],
              #  icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='house',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "AboutAutism":
            AboutAutism.app()
        if app == "Form":
            Form.app()    
        if app == "Precautions":
            Precautions.app()             
    run()