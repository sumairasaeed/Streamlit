import streamlit as st
import docx2txt
import streamlit.components.v1 as components
import pickle
from owlready2 import *
from owlready2.pymedtermino2 import *
from owlready2.pymedtermino2.umls import *

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
	st.title("Explainable Semantic Text Similarity")
	#PYM = get_ontology("http://PYM/")
	#SNOMEDCT_US = PYM["SNOMEDCT_US"]
	#raw_text = st.text_area(str(SNOMEDCT_US[302509004]))
        #concept = SNOMEDCT_US[302509004]
        #print(concept)
	alltextEntitiesAllStr=loadEntities()
	raw_text = st.text_area(str(alltextEntitiesAllStr[0:10]))
	##raw_text = st.text_area("Enter text here please")
	docx_file = st.file_uploader("Upload Document", type=["txt"])
	

if __name__ == '__main__':
	main()
