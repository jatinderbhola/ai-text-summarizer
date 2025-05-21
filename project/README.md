# AI Text Summarizer

A powerful text summarization tool built using state-of-the-art natural language processing models. This project uses the BART-large-CNN model from Hugging Face to generate concise and accurate summaries of text content.

## Features

- 📝 Text summarization using advanced AI models
- 🌐 Web interface built with Streamlit
- ⚡ Fast processing with optimized pipeline
- 🔧 Customizable summary length
- 📊 Interactive user interface

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-text-summarizer.git
cd ai-text-summarizer
```

2. Create and activate virtual environment:
```bash
cd model/bart-cnn
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
cd ../..  # Return to project root
```

4. Run the web interface:
```bash
streamlit run project/app.py
```

## Project Structure

```
ai-text-summarizer/
├── how-to/               # Documentation and guides
├── project/             # Source code
├── model/              # Model-specific files
│   └── bart-cnn/      # BART-CNN model
│       ├── env/       # Virtual environment
│       ├── requirements.txt  # Model dependencies
│       └── config.txt # Model configuration
└── .gitignore         # Git ignore file
```

## Usage

### Web Interface

1. Start the Streamlit app:
```bash
streamlit run project/app.py
```

2. Open your browser and navigate to the displayed URL
3. Enter or paste your text
4. Adjust summary length parameters if needed
5. Click "Generate Summary"

### Python API

```python
from summarizer import generate_summary

text = """Your long text here..."""
summary = generate_summary(text, max_length=130, min_length=30)
print(summary)
```

## Documentation

- Detailed setup instructions: [steps.md](how-to/steps.md)
- Project progress: [changelog.md](how-to/changelog.md)
- Learning resources: [learnings.md](how-to/learnings.md)
- Model details: [config.txt](model/config.txt)

## Requirements

- Python 3.8+
- PyTorch
- Transformers
- Streamlit

See `model/bart-cnn/requirements.txt` for complete list of dependencies.

## Contributing

1. Fork the repository
2. Create your feature branch (`