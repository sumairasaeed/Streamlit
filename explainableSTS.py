import streamlit as st
import docx2txt
import streamlit.components.v1 as components

def load_image(image_file):
	img = Image.open(image_file)
	return img

def main():
	st.title("Explainable Semantic Text Similarity")
	raw_text = st.text_area("Enter text here")

	
	docx_file = st.file_uploader("Upload Document", type=["txt"])
		
	if st.button("Process"):

		if docx_file is not None and raw_text == "":
			
			if docx_file.type == "text/plain":
				# Read as string (decode bytes to string)
				raw_text = str(docx_file.read(),"utf-8")
				st.text(raw_text)
				preprocess(raw_text)

			
			else:
				raw_text = docx2txt.process(docx_file)
				st.write(raw_text)
		elif docx_file is None and raw_text is not None:
			preprocess(raw_text)
				

if __name__ == '__main__':
	main()