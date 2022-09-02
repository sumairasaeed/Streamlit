import streamlit as st
import docx2txt
import streamlit.components.v1 as components

# def load_image(image_file):
# 	img = Image.open(image_file)
# 	return img

def main():
	st.title("Explainable Semantic Text Similarity")
	raw_text = st.text_area("Enter text here")
	docx_file = st.file_uploader("Upload Document", type=["txt"])
	

if __name__ == '__main__':
	main()