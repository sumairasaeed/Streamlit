import requests
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

#Enable garbage collection
gc.enable()

#Clean up the memory from unused objects
gc.collect()

@st.cache(ttl=24*60*60)
def downloadFileGdrive():
	url = "https://drive.google.com/file/d/16MagXKJ40efUsoiL2FygIBvXIBHnM906/view?usp=sharing"
	output = "medcatLarge1.zip"
	file=gdown.download(url=url, output=output, quiet=False, fuzzy=True)
	return output

@st.cache(hash_funcs={tokenizers.Tokenizer: lambda _: None, tokenizers.AddedToken: lambda _: None})
def load_model(file):
	cat=CAT.load_model_pack(file)
	return cat

def loadEntities():
	#File containing mapped codes in textual form for 409 indus records
	file = open("alltextEntitiesKaggleStrDisordersNew.data",'rb')
	##file = open("alltextEntitiesKaggleStrDisorders.data",'rb')
	alltextEntitiesAllStr = pickle.load(file)
	file.close()
	return alltextEntitiesAllStr

def loadProbCalc():
        #file = open("alltextEntitiesAllStr2.data",'rb')
        file = open("alltextEntitiesKaggleStr.data",'rb')
        alltextEntitiesAllStrForProbCalc = pickle.load(file)
        file.close()
        return alltextEntitiesAllStrForProbCalc

def save_uploadedfile(uploadedfile):
	with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
        	f.write(uploadedfile.getbuffer())
	return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

def main():
	st.text_area("Explainable Semantic Text Similarity")
	file_name_model="medcatLarge1.zip"
	if os.path.exists(file_name_model)==False:
        	file_name_model = downloadFileGdrive()
	catmodel = copy.deepcopy(load_model(file_name_model))
	text = "A 45-year old male patient was admitted in emergency department. He was feeling Fever and Cough and Flue. Also complained of abdominal pain"
	entities = catmodel.get_entities(text)
	st.text_area(str(entities))	
if __name__ == '__main__':
	main()
