import requests
import streamlit as st
import docx2txt
import streamlit.components.v1 as components
import pickle
#from owlready2 import *
import simple_icd_10 as icd
from medcat.vocab import Vocab
from medcat.cdb import CDB
from medcat.cat import CAT
from medcat.meta_cat import MetaCAT
DATA_DIR = "./data/"
MODEL_DIR = "./models/"
#model_pack_path = MODEL_DIR + "medmen_wstatus_2021_oct.zip"
import wget


@st.cache
def load_model():
	modelurl="mc_modelpack_snomed_int_3_feb_2022_a474096eb4566638.zip"
	return CAT.load_model_pack(modelurl)

def loadMedmodel():
	st.text_area("Explainable Semantic Text Similarity")
	modelurl="mc_modelpack_snomed_int_3_feb_2022_a474096eb4566638.zip"
	##modelurl="https://github.com/sumairasaeed/modelpack/blob/main/mc_modelpack_snomed_int_3_feb_2022_a474096eb4566638.zip"
	##file_name_model = wget.download(modelurl)
	##file_name="myfile.zip"
	#req=urllib.request.urlretrieve(modelurl, file_name)
	##req = requests.get(modelurl)
	# Writing the file to the local file system
	##with open(file_name,'wb') as output_file:
	##    output_file.write(req.content)
	
	
	#file_name_model="mymedmodel1.zip"
	#req = requests.get(modelurl)
	#with open(file_name_model,'wb') as output_file:
	#    output_file.write(req.content)
	#print('Downloading Completed')
	#st.title(file_name_model)
	cat = CAT.load_model_pack(modelurl)
	ext = "My simple document with kidney failure and fever and cough and flue"
	entities = cat.get_entities(text)
	##st.text_area(str(entities))
		
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
	cat = load_model()
	ext = "My simple document with kidney failure and fever and cough and flue"
	entities = cat.get_entities(text)
	#st.text_area(str(entities))
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

