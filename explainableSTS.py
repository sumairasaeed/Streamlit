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

@st.cache(ttl=24*60*60)
def downloadFileGdrive():
        url = "https://drive.google.com/file/d/16MagXKJ40efUsoiL2FygIBvXIBHnM906/view?usp=sharing"
	output = "medcatLarge1.zip"
	file=gdown.download(url=url, output=output, quiet=False, fuzzy=True)
        print(file)
        #file=gdown.download(url, output, quiet=False)
        #st.text_area(str(file))
        return output


@st.cache(ttl=24*60*60)
def load_model():
        modelurl="https://medcat.rosalind.kcl.ac.uk/media/medmen_wstatus_2021_oct.zip"
        file_name_model = wget.download(modelurl)
        return file_name_model

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
        file_name_model = downloadFileGdrive()
        with st.spinner("Please wait"):
                cat=CAT.load_model_pack(file_name_model)
        text = "My simple document with kidney failure and fever and cough and flue"
        entities = cat.get_entities(text)
        st.text_area(str(entities))
        #file_name_model = load_model()
	#st.text_area("Explainable Semantic Text Similarity")
	#with st.spinner('Wait for it...'):
	#	modelurl="mc_modelpack_snomed_int_3_feb_2022_a474096eb4566638.zip"
	#	##modelurl="https://github.com/sumairasaeed/modelpack/blob/main/mc_modelpack_snomed_int_3_feb_2022_a474096eb4566638.zip"
	#	cat = CAT.load_model_pack(modelurl)
	#	ext = "My simple document with kidney failure and fever and cough and flue"
	#	entities = cat.get_entities(text)
	#st.success('Done!')	
	
if __name__ == '__main__':
	main()

