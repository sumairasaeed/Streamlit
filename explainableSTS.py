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

def main():
	alltextEntitiesAllStr=loadEntities()
	raw_text = st.text_area(str(alltextEntitiesAllStr[8]))
	for x in alltextEntitiesAllStr[8][3]:
		if x!="":
			st.title(str(icd.get_description(str(x))))
			st.title(str(icd.get_description(icd.get_parent(str(x)))))
	#raw_text = st.text_area("Enter text here please")
	#default_world.set_backend(filename = "pym.sqlite3")(
	#PYM = get_ontology("http://PYM/")
	#PYM.load()
	#ICD10 = PYM["ICD10"]
	!wget https://medcat.rosalind.kcl.ac.uk/media/medmen_wstatus_2021_oct.zip -P ./data/
	docx_file = st.file_uploader("Upload Document", type=["txt"])
	#raw_text = st.text_area(str(ICD10["E10"]))

if __name__ == '__main__':
	main()
