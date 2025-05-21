# Setting Up Your AI Text Summarizer Project

This guide will walk you through setting up and using an AI-powered text summarization tool using Hugging Face's transformers library. We'll use the BART model, which is specifically trained for summarization tasks.

## Prerequisites

- Python 3.8 or higher installed
- Basic familiarity with terminal/command line
- A text editor (VS Code, Cursor, etc.)

## Step 1: Setting Up Your Development Environment

### 1.1 Create a New Project Directory

```bash
mkdir ai-text-summarizer
cd ai-text-summarizer
```

### 1.2 Create a Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects. We'll create it inside the model directory.

```bash
# Create model directory and environment
mkdir -p model/bart-cnn
cd model/bart-cnn
python -m venv env

# Activate virtual environment
# On macOS/Linux:
source env/bin/activate
# On Windows:
.\env\Scripts\activate
```

You'll know it's activated when you see `(env)` in your terminal prompt.

### 1.3 Install Required Dependencies

```bash
# Make sure you're in the model/bart-cnn directory
pip install transformers torch
pip install streamlit  # For the web interface
pip freeze > requirements.txt  # Save model-specific dependencies
cd ../..  # Return to project root
```

## Step 2: Creating the Core Summarizer

### 2.1 Create the Main Script

Create a new file `project/summarizer.py`:

```python
from transformers import pipeline

def initialize_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, max_length=130, min_length=30):
    summarizer = initialize_summarizer()
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Example usage
if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals.
    """
    
    summary = generate_summary(sample_text)
    print("Original Text:\n", sample_text)
    print("\nSummary:\n", summary)
```

## Step 3: Adding a Web Interface

### 3.1 Create the Streamlit App

Create a new file `project/app.py`:

```python
import streamlit as st
from summarizer import generate_summary

st.title("AI Text Summarizer")

# Text input
text_input = st.text_area("Enter the text you want to summarize:", height=200)

# Sliders for customization
max_length = st.slider("Maximum summary length", 50, 500, 130)
min_length = st.slider("Minimum summary length", 10, 100, 30)

if st.button("Generate Summary"):
    if text_input:
        with st.spinner("Generating summary..."):
            summary = generate_summary(text_input, max_length, min_length)
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
```

## Step 4: Running the Application

### 4.1 Run the Command-Line Version

```bash
python project/summarizer.py
```

### 4.2 Run the Web Interface

```bash
streamlit run project/app.py
```

The web interface will automatically open in your default browser.

## Common Issues and Solutions

1. **ModuleNotFoundError**: Make sure you've activated your virtual environment and installed all requirements.
2. **CUDA/GPU Errors**: The default installation uses CPU. For GPU support, install `torch` with CUDA support.
3. **Memory Issues**: Reduce batch size or text length if you encounter memory problems.

## Next Steps

- Experiment with different models from Hugging Face
- Add support for different languages
- Implement batch processing for multiple texts
- Add export functionality for summaries

## Resources

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [BART Model Card](https://huggingface.co/facebook/bart-large-cnn)
- [Streamlit Documentation](https://docs.streamlit.io)

## Managing Virtual Environments

### Deactivating the Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

The prompt will no longer show `(env)`, indicating you're back in the global Python environment.

### Deleting the Environment

If you need to remove the virtual environment (e.g., to recreate it or clean up):

1. First, deactivate if it's active:
```bash
deactivate
```

2. Then, delete the environment directory:
```bash
# If you're in the project root:
rm -rf model/bart-cnn/env

# Or if you're in the model directory:
rm -rf env
```

### Creating a New Environment

If you need to recreate the environment after deletion:

```bash
# Navigate to model directory
cd model/bart-cnn

# Create new environment
python -m venv env

# Activate it
source env/bin/activate  # On macOS/Linux
# or
.\env\Scripts\activate   # On Windows

# Reinstall dependencies
pip install -r requirements.txt
```
