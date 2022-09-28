import requests
#from pymedtermino.all import *
#from pymedtermino import *
#from pymedtermino.snomedct import *
import streamlit as st
import docx2txt
import streamlit.components.v1 as components
import pickle
#from owlready2 import *
import simple_icd_10 as icd
from medcat.cat import CAT
DATA_DIR = "./data/"
MODEL_DIR = "./models/"
#model_pack_path = MODEL_DIR + "medmen_wstatus_2021_oct.zip"
import wget
import gdown
import copy
import os
import tokenizers
#Import the garbage collection module
import gc
from transformers import pipeline

#Enable garbage collection
gc.enable()

#Clean up the memory from unused objects
gc.collect()


@st.cache(ttl=24*60*60)
def downloadFileGdrive():
    url = "https://drive.google.com/file/d/16MagXKJ40efUsoiL2FygIBvXIBHnM906/view?usp=sharing"
    output = "medcatLarge1.zip"
    filename=gdown.download(url=url, output=output, quiet=False, fuzzy=True)
    st.session_state.modelpath=filename
    return filename

def load_model(file):
    return CAT.load_model_pack(file)


#file_name_model="medcatLarge1.zip"

def querySubmit(query, placeholder):
    if "catmodel" not in st.session_state:
        if "modelpath" in st.session_state:
            if os.path.exists(st.session_state.modelpath)==False:
                st.session_state.modelpath= downloadFileGdrive()
                st.session_state.catmodel = load_model(st.session_state.modelpath)
            else:
                st.session_state.catmodel = load_model(st.session_state.modelpath)
        else:
            st.session_state.modelpath= downloadFileGdrive()
            st.session_state.catmodel = load_model(st.session_state.modelpath)
        
        
    entities = st.session_state.catmodel.get_entities(query)
    if entities:
        st.session_state.entities=entities
    else:
        st.session_state.entities="None"
    with placeholder:
        placeholder=st.markdown(str(st.session_state.entities))
    #st.session_state.entities=entities
    #if st.session_state.submit:
        
    #st.write(str(st.session_state.entities))
# =============================================================================
#     
# def querySubmit(query, placeholder):
#     if "modelpath" in st.session_state:
#         if os.path.exists(st.session_state.modelpath)==False:
#          	file_name_model = downloadFileGdrive()
#         else:
#             if "catmodel" not in st.session_state:
#                 st.session_state.catmodel = load_model(st.session_state.modelpath)
#             
#                 
#     else:
#         st.session_state.modelpath=downloadFileGdrive()
#         st.session_state.catmodel = load_model(st.session_state.modelpath)
#         
#     entities = st.session_state.catmodel.get_entities(query)
#     st.session_state.entities=entities
#     st.write(str(st.session_state.entities))
#     placeholder.markdown(str(st.session_state.entities))
#     
# =============================================================================

# =============================================================================
# @st.cache(ttl=24*60*60)
# def downloadFileGdrive():
# 	url = "https://drive.google.com/file/d/16MagXKJ40efUsoiL2FygIBvXIBHnM906/view?usp=sharing"
# 	output = "medcatLarge1.zip"
# 	file=gdown.download(url=url, output=output, quiet=False, fuzzy=True)
# 	return output
# 
# def load_model(file):
# 	cat=CAT.load_model_pack(file)
# 	return cat
# 
# file_name_model="medcatLarge1.zip"
# if os.path.exists(file_name_model)==False:
# 	file_name_model = downloadFileGdrive()
# catmodel = copy.deepcopy(load_model(file_name_model))
# 
# def loadEntities():
# 	#File containing mapped codes in textual form for 409 indus records
# 	file = open("alltextEntitiesKaggleStrDisordersNew.data",'rb')
# 	##file = open("alltextEntitiesKaggleStrDisorders.data",'rb')
# 	alltextEntitiesAllStr = pickle.load(file)
# 	file.close()
# 	return alltextEntitiesAllStr
# 
# def loadProbCalc():
#         #file = open("alltextEntitiesAllStr2.data",'rb')
#         file = open("alltextEntitiesKaggleStr.data",'rb')
#         alltextEntitiesAllStrForProbCalc = pickle.load(file)
#         file.close()
#         return alltextEntitiesAllStrForProbCalc
# 
# def save_uploadedfile(uploadedfile):
# 	with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
#         	f.write(uploadedfile.getbuffer())
# 	return st.success("Saved File:{} to tempDir".format(uploadedfile.name))
# 
# =============================================================================
def main():
    st.title("Explainable Semantic Text Similarity of Medical Notes")
    
    #st.text_input(l6abel, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
    if "querystate" not in st.session_state:
        querytext=st.text_input("Query trxt", value="", max_chars=None, key="query", placeholder="Enter query text here")
    else:
        querytext=st.text_input("Query trxt", value=st.session_state.quarystate, key="query")
    
    buttonsubmit=st.empty()
    placeholder = st.empty()
    
    # Replace the placeholder with some text:
    #placeholder.text("Hello")
        
    buttonsubmit=st.button("Submit", key="submit", on_click=querySubmit, args=(querytext,placeholder))
    if st.session_state.submit:
        if "entities" in st.session_state:
                  with placeholder:
                      placeholder=st.markdown(str(st.session_state.entities))
      

# =============================================================================
#     if "entities" in st.session_state:
#         with placeholder:
#             placeholder=st.markdown(str(st.session_state.entities))
#     else:
#         placeholder = st.empty()
# 
# =============================================================================

    
    
# =============================================================================
#     if(st.button("Submit")):
#                 entities = catmodel.get_entities(query)
#                 st.text("Medical Entities:")
#                 st.text_area(str(entities))       
# =============================================================================
	#text = "A 45-year old male patient was admitted in emergency department. He was feeling Fever and Cough and Flue. Also complained of abdominal pain"
	#entities = catmodel.get_entities(text)
	#st.text_area(str(entities))
if __name__ == '__main__':
	main()
