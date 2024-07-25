# CHATWITHPDFS-USING-GEMINI

 ChatwithPDFs Using Gemini is a tool or service designed to facilitate interaction with PDF documents through natural language queries. Utilizing advanced AI, likely based on the Gemini model, it allows users to upload PDF files and then engage in a conversational interface to extract information, ask questions, and receive summaries or detailed answers based on the content of the PDFs.

# How to run?

### STEPS:

Clone the repository

```bash
Project repo https://github.com/codeakki/ChatWithPdfGemini.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.9 -y
```

```bash
conda activate venv
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
streamlit run app.py
```

Now,

```bash
open up localhost:

```

## Sample

![OpenAI Logo](https://github.com/codeakki/ChatWithPdfGemini/blob/master/image.png)

### Techstack Used:

- Python
- Streamlit
- google-generativeai
- langchain
- PyPDF2
- Langchain_cummunity
- faiss-cpu
- 
