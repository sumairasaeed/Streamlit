import streamlit as st
import docx2txt
import streamlit.components.v1 as components
import pickle


def loadEntities():
	#File containing mapped codes in textual form for 409 indus records
	file = open("alltextEntitiesKaggleStrDisordersNew.data",'rb')
	##file = open("alltextEntitiesKaggleStrDisorders.data",'rb')
	alltextEntitiesAllStr = pickle.load(file)
	file.close()
	return alltextEntitiesAllStr

def main():
	st.title("Explainable Semantic Text Similarity")
	alltextEntitiesAllStr=loadEntities()
	raw_text = st.text_area(str(alltextEntitiesAllStr[0:10]))
	##raw_text = st.text_area("Enter text here please")
	docx_file = st.file_uploader("Upload Document", type=["txt"])
	

if __name__ == '__main__':
	main()
