import streamlit as st
import docx2txt
import streamlit.components.v1 as components

from owlready2 import *
from owlready2.pymedtermino2 import *
from owlready2.pymedtermino2.umls import *

def main():
	st.title("Explainable Semantic Text Similarity")
	raw_text = st.text_area("Enter text here please")
	docx_file = st.file_uploader("Upload Document", type=["txt"])
	PYM=get_ontology("http://PYM/").load()
	SNOMEDCT_US = PYM["SNOMEDCT_US"]
	concept = SNOMEDCT_US[302509004]
	st.header(concept)

if __name__ == '__main__':
	main()
