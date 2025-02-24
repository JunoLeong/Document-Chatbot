# Document Chatbot 📄
A Conversational AI chatbot that allows users to ask questions based on the content of a PDF document. It leverages FAISS for vector storage, Google Generative AI (Flash Gemini 2.0) for embeddings and responses, and Gradio for an interactive chat interface.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/bee-ching-leong/)
[![YouTube](https://img.shields.io/badge/Youtube-Subcribe-red)](https://www.youtube.com/@BeechingLeong)

## Features ✨ 
- Conversational AI with Flash Gemini 2.0: Uses Google's Gemini 2.0 Flash model to generate accurate and context-aware responses.
- Automatic PDF Processing: Extracts text from PDFs and converts them into searchable chunks.
- Efficient Text Search: Uses FAISS for fast and efficient document retrieval.
- Interactive Chat Interface: Built with Gradio for an easy-to-use web-based chatbot.
- Customizable & Expandable: Modify document sources and enhance AI capabilities as needed.

## Video Demo 📽️
- Click to watch the demo on YouTube! >> [Video Demo's Link](https://youtu.be/LaqiERRpiAg?si=uvZ5TfQ-PQGia8wB)

## How It Works 🏗️
1. Load PDF Document: Extracts text from the provided "BDO-Malaysia-Budget-2025-Highlights.pdf" file.
2. Create Vector Store: The extracted text is split into chunks and embedded using Google Generative AI (```models/embedding-001```), then stored in FAISS.
3. User Query Processing: When a user asks a question, the system searches for relevant document chunks using FAISS.
4. AI-Generated Responses: The chatbot, powered by Gemini 2.0 Flash, provides intelligent responses based on the retrieved document context.

# Installation & Setup 🚀
1. Ensure you have Python installed, then install dependencies:
```bash
pip install -r requirements.txt
```
2. add your Google API Key in ```.env``` file.
``` bash
GOOGLE_API_KEY=your_google_api_key_here
```
3. The system uses "BDO-Malaysia-Budget-2025-Highlights.pdf" as the default document to demonstrate its capabilities. You can replace it with any other document. To use a different document instead of "**BDO-Malaysia-Budget-2025-Highlights.pdf**", modify the ```DEFAULT_DOCUMENT_PATHS``` in ```main.py```:
```bash
DEFAULT_DOCUMENT_PATHS = ["Your_document_name.pdf"]
```
4. Running the Chatbot in your local host.
```bash
python main.py
```
> The chatbot will launch in your web browser via Gradio. ```http://127.0.0.1:7860```

## Project Structure 🛠️
``` bash
📂 Chat with Doc 
├── 📄 main.py                # Main script for running the chatbot
├── 📄 requirements.txt       # Required dependencies
├── 📄 .env                   # Stores API keys (not shared in repo)
├── 📂 faiss_index/           # Directory where FAISS index is stored
└── 📄 README.md              # Project documentation
```
## Chatbot Interface (Gradio) 💬
The chatbot runs on Gradio, providing a simple and interactive web-based interface. It is suitable for rapid prototyping, allowing users to showcase and test the system using a straightforward UI.

### Interface Features 🎨
1. User-Friendly Chatbot:
- Users can input questions and receive AI-generated responses.
- The interface allows easy scrolling and interaction.
- Users can undo and edit their prompt. 
- If the chatbot’s answer does not meet expectations, users can ask the chatbot to regenerate the response with one click for a refined answer.

2. Predefined Example Questions:
- The chatbot includes predefined example questions to help users quickly understand how to interact with the system. These questions **demonstrate** the chatbot's ability to **extract and summarize information** from the document.
- Example questions in this system are "What is the content of the document?", "Summarize the tax personal update."
- These predefined examples serve as guidelines for users, showing how they can ask customized questions to retrieve specific information from the document.

---
Feel free to reach out with suggestions or improvements for the project! If you like or are using this project, please consider giving it a star⭐. Thanks! (●'◡'●)
