import streamlit as st
import docx2txt
import streamlit.components.v1 as components
import pickle
from owlready2 import *
import simple_icd_10 as icd
from medcat.vocab import Vocab
from medcat.cdb import CDB
from medcat.cat import CAT
from medcat.meta_cat import MetaCAT
DATA_DIR = "./data/"
MODEL_DIR = "./models/"
model_pack_path = MODEL_DIR + "medmen_wstatus_2021_oct.zip"
import wget



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
	#!python -m wget https://medcat.rosalind.kcl.ac.uk/media/medmen_wstatus_2021_oct.zip -P ./models/
	#import urllib.request

	#url = 'https://medcat.rosalind.kcl.ac.uk/media/medmen_wstatus_2021_oct.zip'
	#filename = url.split('/')[-1]

	#urllib.request.urlretrieve(url, filename)
	site_url = 'https://medcat.rosalind.kcl.ac.uk/media/medmen_wstatus_2021_oct.zip'
	file_name = wget.download(site_url)
	print(file_name)
	st.title(file_name)
	from medcat.cat import CAT

	# Download the model_pack from the models section in the github repo.
	cat = CAT.load_model_pack(file_name)

	# Test it
	text = "My simple document with kidney failure"
	entities = cat.get_entities(text)
	st.text_area(str(entities))
	#alltextEntitiesAllStr=loadEntities()
	#raw_text = st.text_area(str(alltextEntitiesAllStr[8]))
	f#or x in alltextEntitiesAllStr[8][3]:
	#	if x!="":
	#		st.title(str(icd.get_description(str(x))))
	#		st.title(str(icd.get_description(icd.get_parent(str(x)))))
	#raw_text = st.text_area("Enter text here please")
	#default_world.set_backend(filename = "pym.sqlite3")(
	#PYM = get_ontology("http://PYM/")
	#PYM.load()
	#ICD10 = PYM["ICD10"]
	#!wget https://medcat.rosalind.kcl.ac.uk/media/medmen_wstatus_2021_oct.zip -P ./data/
	datafile = st.file_uploader("Upload_dat",type=['.dat'])
	if datafile is not None:
	   file_details = {"FileName":datafile.name,"FileType":datafile.type}
	   #df  = pd.read_csv(datafile)
	   #st.dataframe(df)
	   save_uploadedfile(datafile)
		
	vocab_file = st.file_uploader("upload_vocab", type=[".dat"])
	if vocab_file is not None:
            path_in = vocab_file.name
            vocabpath=st.text_area(str(path_in))
	else:
            path_in = None
	
	cdb_file = st.file_uploader("upload_cdb", type=[".dat"])
	if cdb_file is not None:
            path_in_cdb_file = cdb_file.name
            print(path_in_cdb_file)
	else:
            path_in = None
	#raw_text = st.text_area(str(ICD10["E10"]))

if __name__ == '__main__':
	main()
