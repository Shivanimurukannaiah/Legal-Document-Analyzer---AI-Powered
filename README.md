# Legal-Document-Analyzer---AI-Powered
Legal Document Analyzer is an AI-powered web application that allows users to upload legal documents (PDF, DOCX, or TXT formats). The app analyzes the content using OpenAI's GPT-3.5/4 to extract
Certainly! Here’s a **detailed README** for your project:

---

This project is a **Legal Document Analyzer** powered by **OpenAI's GPT-3.5/4**. The goal of the application is to help users analyze legal documents by extracting key insights, answering questions, and providing consequences of signing the document. The app allows users to upload legal documents (PDF, DOCX, or TXT formats) and performs natural language processing (NLP) to extract and analyze the content.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
   - [Cloning the Repository](#cloning-the-repository)
   - [Installing Dependencies](#installing-dependencies)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Example](#example)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

---

## Features

- **Document Upload**: Upload legal documents in PDF, DOCX, or TXT formats.
- **AI-Powered Analysis**: Use **OpenAI's GPT-3.5 or GPT-4** to analyze the document for:
  - **Questions and Answers**: Extract questions and provide answers.
  - **Consequences of Signing**: Identify the possible consequences of signing the document.
  - **Subtopics**: Extract the main points and subtopics from the document.
- **Custom Questions**: Users can ask specific questions about the document, and the AI will answer based on the content.
- **Interactive Interface**: The user interface is built using **Streamlit**, making it simple and interactive.

---

## Installation

### Cloning the Repository

To get started with the project, you'll first need to clone the repository to your local machine.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/legal-document-analyzer.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd legal-document-analyzer
   ```

### Installing Dependencies

Make sure you have `pip` installed to manage Python packages. You can install all the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

This will install the required Python libraries:

- **Streamlit**: For building the web app interface.
- **OpenAI**: To interact with OpenAI’s GPT models.
- **python-docx**: For extracting text from DOCX files.
- **PyPDF2**: For extracting text from PDF files.

---

## Usage

1. **Set up your OpenAI API Key**: You will need an **OpenAI API key** to use the application. Obtain it from [OpenAI’s platform](https://platform.openai.com/account/api-keys) and replace the placeholder in the `app.py` file with your API key:

   ```python
   openai.api_key = "YOUR_OPENAI_API_KEY"
   ```

2. **Run the Streamlit app**:

   Once everything is set up, run the following command to start the application:

   ```bash
   streamlit run app.py
   ```

3. **Access the app**: Open your web browser and go to `http://localhost:8501` to interact with the app.

---
Methodologies Used

This project leverages the following AI and engineering methodologies:

Document Parsing & Preprocessing: Extract text from PDF, DOCX, and TXT files using PyPDF2 and python-docx, followed by cleaning and chunking for LLM inputs.

Zero-Shot Prompting: Directly query GPT-3.5/4 without examples using clear, structured prompts for Q&A and extraction tasks.

Few-Shot Prompting: Provide brief examples in prompts for consistent formatting when summarizing clauses or generating question/answer pairs.

Persona Prompting: Use system messages (e.g., “You are a legal analysis assistant”) to set the LLM’s role and tone.

Chain-of-Thought & Reasoning: Encourage step-by-step explanations for complex legal interpretations and consequence analysis.

Streamlit UI: Rapidly build an interactive web interface for file upload, display of results, and custom question entry.

Error Handling & Validation: Safely handle file parsing errors, oversized documents, and API failures.

Deployment & Scalability: Use Docker or cloud services to scale processing for large documents and multiple users.


## How It Works

### 1. Document Upload

The user uploads a PDF, DOCX, or TXT file through the **Streamlit file uploader**. The file is processed and converted into text using the respective extractor (PDF, DOCX, or plain text).

### 2. AI-Powered Analysis

Once the document is uploaded, the user clicks the **Analyze with OpenAI** button. The app sends the document’s text to OpenAI, where it is processed by **GPT-3.5/4** to extract:

- **Questions and Answers**: The AI scans the document for explicit or implied questions and provides answers.
- **Consequences of Signing**: The AI extracts potential outcomes if the user were to sign the document.
- **Subtopics**: The AI breaks the document down into key subtopics or sections.

### 3. Custom Questions

The app allows users to enter custom questions about the document. These questions are then sent to the OpenAI API, which provides answers based on the document's content.

---

## Example

### Document Example:
Here’s an example of the type of document you can upload:

```
This agreement allows John to borrow $5,000 from Mike. John agrees to repay the full amount within 6 months.

If John fails to repay, Mike can take legal action.

Questions:
- What happens if John doesn't repay?
- Is there a repayment deadline?
```

### Sample Questions and AI Responses:
1. **Question**: What happens if John doesn't repay the loan?
   - **Answer**: Mike can take legal action to recover the loan amount.

2. **Question**: Is there a repayment deadline?
   - **Answer**: Yes, the repayment is due within 6 months from the agreement date.

3. **Subtopics**:
   - Loan Terms
   - Repayment Deadline
   - Legal Consequences

---
Example Output

Below is an example of the Analyzer's output for a sample contract:


Figure: AI-generated summary, Q&A, and consequences panel.
![Screenshot](IMG_3444.JPG)



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

