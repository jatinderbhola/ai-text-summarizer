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

Create a new file `project/summarizer.py`. We'll implement a professional-grade summarizer with proper logging, error handling, and type safety:

```python
"""
AI Text Summarizer using Hugging Face Transformers
"""

import logging
from typing import Dict, Optional, Union

from transformers import pipeline
from transformers.pipelines.base import Pipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TextSummarizer:
    """A class to handle text summarization using the BART model."""
    
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Initialize the summarizer with a specific model.
        
        Args:
            model_name (str): The name/path of the model to use
        """
        self.model_name = model_name
        self._summarizer: Optional[Pipeline] = None
        logger.info(f"Initializing summarizer with model: {model_name}")
    
    @property
    def summarizer(self) -> Pipeline:
        """Lazy loading of the summarization pipeline."""
        if self._summarizer is None:
            try:
                self._summarizer = pipeline(
                    "summarization",
                    model=self.model_name,
                    device=-1  # CPU by default
                )
                logger.info("Summarization pipeline loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load summarization pipeline: {str(e)}")
                raise
        return self._summarizer
    
    def summarize(
        self,
        text: str,
        max_length: int = 130,
        min_length: int = 30,
        do_sample: bool = False
    ) -> Dict[str, Union[str, float]]:
        """
        Generate a summary of the input text.
        
        Args:
            text (str): The text to summarize
            max_length (int): Maximum length of the summary
            min_length (int): Minimum length of the summary
            do_sample (bool): Whether to use sampling in generation
            
        Returns:
            Dict containing the summary text and metadata
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty")
            
        try:
            # Clean and preprocess text
            text = text.strip()
            
            # Generate summary
            result = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=do_sample,
                early_stopping=True
            )
            
            # Extract and return summary with metadata
            summary = result[0]['summary_text']
            
            return {
                'summary': summary,
                'original_length': len(text.split()),
                'summary_length': len(summary.split()),
                'compression_ratio': len(summary.split()) / len(text.split())
            }
            
        except Exception as e:
            logger.error(f"Summarization failed: {str(e)}")
            raise

def generate_summary(
    text: str,
    max_length: int = 130,
    min_length: int = 30
) -> str:
    """
    Convenience function to quickly generate a summary.
    
    Args:
        text (str): The text to summarize
        max_length (int): Maximum length of the summary
        min_length (int): Minimum length of the summary
        
    Returns:
        str: The generated summary
    """
    summarizer = TextSummarizer()
    result = summarizer.summarize(text, max_length, min_length)
    return result['summary']

if __name__ == "__main__":
    # Example usage
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals.
    """
    
    try:
        summary = generate_summary(sample_text)
        print("Original Text:\n", sample_text)
        print("\nSummary:\n", summary)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

This implementation includes several professional features:
1. Type hints for better code maintainability
2. Proper logging configuration
3. Class-based design with lazy loading
4. Comprehensive error handling
5. Summary metadata (length, compression ratio)
6. Clean separation between class implementation and convenience function

For detailed explanations of the code concepts used, see `how-to/code-explanations.md`.

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
