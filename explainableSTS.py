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
from medcat.vocab import Vocab
from medcat.cdb import CDB
from medcat.cat import CAT
from medcat.meta_cat import MetaCAT

#from owlready2.pymedtermino2 import *
#from owlready2.pymedtermino2.umls import *


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
        raw_text = st.text_area("Enter text here please")
        docx_file = st.file_uploader("Upload Document", type=["txt"])
        raw_text = st.text_area(str(alltextEntitiesAllStr[8]))
        st.title(str(icd.get_description("XII")))
        # Load the vocab model you downloaded
        #vocab = Vocab.load('vocab.dat')
        # Load the cdb model you downloaded
        #cdb = CDB.load('cdb.dat') 
        # Download the mc_status model from the models section below and unzip it
        #mc_status = MetaCAT.load("D:\Streamlit")
        #cat = CAT(cdb=cdb, config=cdb.config, vocab=vocab, meta_cats=[mc_status])
        # Test it
        #text = "My simple document with kidney failure"
        #entities = cat.get_entities(text)
        #print(entities)
        #raw_text = st.text_area(str(entities))
	#st.title("Explainable Semantic Text Similarity")
	#PYM = get_ontology("http://PYM/")
	#SNOMEDCT_US = PYM["SNOMEDCT_US"]
	#raw_text = st.text_area(str(SNOMEDCT_US[302509004]))
        #concept = SNOMEDCT_US[302509004]
        #print(concept)
	#alltextEntitiesAllStr=loadEntities()
	#raw_text = st.text_area(str(alltextEntitiesAllStr[0:5]))
	
	

if __name__ == '__main__':
	main()
