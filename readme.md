# NVIDIA NIM Powered Q&A Bot

This project is a Streamlit-based Q&A bot powered by NVIDIA NIM and LangChain. The bot allows users to ask questions from documents uploaded in PDF format. It utilizes NVIDIA's LLM (meta/llama-3.1-8b-instruct) for generating responses and FAISS for document similarity search.

![Screenshot of the Interface](Screenshot%202024-08-29%20141203.png)

## Project Structure

project-directory/ 
│ ├── app.py 
├── Final.py 
├── requirements.txt 
├── .env 
├── README.md 
├── LICENSE 
├── .gitignore 
├── Screenshot_2024-08-29_141203.png 
└── pdf/ # Folder containing the PDF documents 
├── generative ai.pdf └── attention.pdf


## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/nvidia-nim-qa-bot.git
cd nvidia-nim-qa-bot
```

2. Install the required Python packages:
```bash 
pip install -r requirements.txt
```

3. Set up your environment variables in the `.env` file:

```bash 
NVIDIA_API_KEY=your_nvidia_api_key
```

- Replace the placeholder with your actual NVIDIA API key.

1. Running the Application
2. Ensure your `.env` file is properly configured with your NVIDIA API key.

- Run the Streamlit application:
```bash
streamlit run Final.py
```
Open your web browser and go to http://localhost:8501 to interact with the application.

## Example Usage

- Upload PDF documents using the file uploader in the pdf/ directory.
- Enter your question in the text input field and click on "Document Embedding" to prepare the vector store.
- The bot will retrieve relevant sections from the uploaded documents and provide an answer based on the provided context.
- Expand the "Document Similarity search" section to see the retrieved document snippets.

## Integration Details

- NVIDIA NIM: Utilized for the conversational AI component, using the meta/llama-3.1-8b-instruct model.
- LangChain Components: Used for creating the retrieval-augmented generation (RAG) pipeline. It also helps in handling PDF documents and embedding generation.
- FAISS: An efficient similarity search library used to search through the document embeddings.
Files
- app.py: A script containing a basic implementation using the NVIDIA API.
- Final.py: The main Python script that handles the Streamlit interface, LangChain components, PDF loading, and Q&A functionality.
- requirements.txt: Lists all the Python dependencies needed to run the application.
- .env: Contains the NVIDIA API key. This file should not be included in version control.
- README.md: This file, providing an overview of the project.
- LICENSE: The project's license, specifying how others may use the code.
- .gitignore: Specifies files and directories that should be ignored by Git, such as the .env file and any other sensitive information.
- pdf/: Directory containing the PDF documents to be uploaded and queried.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## .gitignore
The following files are ignored in the version control:
```bash
.env
__pycache__/
*.pyc
*.pyo
*.pyd
pdf/
```

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments
- Thanks to NVIDIA for providing powerful APIs and models for advanced NLP tasks.
- Thanks to LangChain for enabling easy integration and handling of complex AI tasks.