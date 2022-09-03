import streamlit as st
import docx2txt
import streamlit.components.v1 as components

def main():
	st.title("Explainable Semantic Text Similarity")
	raw_text = st.text_area("Enter text here please")
	docx_file = st.file_uploader("Upload Document", type=["txt"])
	

if __name__ == '__main__':
	main()
