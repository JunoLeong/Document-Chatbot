import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai
import gradio as gr

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load and process default documents at system startup
DEFAULT_DOCUMENT_PATHS = ["BDO-Malaysia-Budget-2025-Highlights.pdf"] #Change the document path to the path of the document you want to use.

def get_pdf_text_from_paths(file_paths):
    markdown_text = ""
    for path in file_paths:
        pdf_reader = PdfReader(path)
        for page_num, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            if not text:
                continue

            # Convert page text to markdown (e.g., add headings or bullet points)
            markdown_text += f"\n\n### Page {page_num + 1}\n\n"
            markdown_text += text.strip() + "\n\n"
    return markdown_text

#Splits extracted markdown text into manageable chunks.
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

#Creates and saves a FAISS vector store from text chunks.
def create_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "answer is not available in the context." Do not provide incorrect answers.

    Context:
    {context}?

    Question:
    {question}

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)

def process_user_message(user_input,history):
    if user_input:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = vector_store.similarity_search(user_input)

        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": user_input}, return_only_outputs=True)
        return response["output_text"]

    return "Please enter a question."

# Preload documents and create the vector store
def preload_documents():
    print("Preloading documents...")
    raw_markdown_text = get_pdf_text_from_paths(DEFAULT_DOCUMENT_PATHS)
    text_chunks = get_text_chunks(raw_markdown_text)
    create_vector_store(text_chunks)
    print("Documents preloaded and vector store created.")

# Gradio Chat Interface# Gradio Chat Interface
def main():
    preload_documents()
    title = "Document Chatbot"
    
    # Create custom theme based on Ocean theme
    theme = gr.themes.Ocean().set(
        body_background_fill="*primary_50",  
        background_fill_primary="*primary_100",  
        block_background_fill="*neutral_50",  
        block_label_background_fill="*primary_100"  
    )

    # Set up CSS styles for additional customization
    css = """
    .gradio-container {
        background-color: var(--body-background-fill);
    }
    """

    demo = gr.ChatInterface(
        fn=process_user_message,
        title = title,
        theme=theme,
        css=css,
        examples=[
            "What is the content of the document?",
            "Summarize the tax personal update."
        ]
    )
    demo.launch()

if __name__ == "__main__":
    main()