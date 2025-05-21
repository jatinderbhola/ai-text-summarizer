# AI Text Summarizer Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Transformers-orange)](https://huggingface.co/)
[![Model](https://img.shields.io/badge/Model-BART--CNN-green)](https://huggingface.co/facebook/bart-large-cnn)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyTorch](https://img.shields.io/badge/PyTorch-Framework-red)](https://pytorch.org/)
[![AI](https://img.shields.io/badge/AI-Text%20Summarization-brightgreen)](https://github.com/jatinderbhola/ai-text-summarizer)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen)](https://github.com/jatinderbhola/ai-text-summarizer)

[![Author](https://img.shields.io/badge/Author-Jatinder%20(Jay)%20Bhola-blue)](https://www.linkedin.com/in/jatinderbhola)
[![Website](https://img.shields.io/badge/Website-DiceCape.com-lightgrey)](https://www.dicecape.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jatinderbhola-blue)](https://linkedin.com/in/jatinderbhola)

## Project Overview

A learning-focused project implementing an AI-powered text summarization tool using state-of-the-art natural language processing models. This project uses the BART-large-CNN model from Hugging Face to generate concise and accurate summaries of text content.

## Project Purpose

This project serves as a practical learning experience in:
- Working with modern NLP models and transformers
- Understanding model deployment and integration
- Building user interfaces for AI applications
- Managing Python virtual environments
- Following best practices in project structure and documentation
- Learning Git workflow and meaningful commit practices

## Project Structure

```
ai-text-summarizer/
├── how-to/                 # Learning and Documentation
│   ├── steps.md           # Step-by-step setup and implementation guide
│   ├── learnings.md       # Key insights and learning points
│   └── changelog.md       # Project progress and changes
│
├── model/                  # Model-specific Components
│   └── bart-cnn/          # BART-CNN Model Implementation
│       ├── config.txt     # Model configuration and parameters
│       ├── requirements.txt # Model-specific dependencies
│       └── env/           # Virtual environment (not tracked)
│
├── project/               # Core Application Code
│   ├── summarizer.py     # Main summarization logic
│   ├── app.py           # Streamlit web interface
│   └── README.md        # Application-specific documentation
│
└── .gitignore           # Git ignore configuration
```

## Documentation Quick Links

- [Setup Guide](how-to/steps.md) - Detailed instructions for setting up and running the project
- [Learning Journal](how-to/learnings.md) - Key insights about GenAI development, best practices, and technical concepts
- [Project Progress](how-to/changelog.md) - Chronological record of project development and changes

## Requirements

### System Requirements
- Python 3.8 or higher
- Git
- Sufficient RAM for model operations (minimum 8GB recommended)

### Key Dependencies
- `transformers` - Hugging Face Transformers library for NLP
- `torch` - PyTorch for deep learning operations
- `streamlit` - Web interface framework
- See `model/bart-cnn/requirements.txt` for complete list

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/jatinderbhola/ai-text-summarizer.git
cd ai-text-summarizer
```

2. Set up the virtual environment:
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

4. Run the application:
```bash
streamlit run project/app.py
```

## Project Features

- 📝 Text summarization using BART-CNN model
- 🌐 Interactive web interface
- ⚡ Efficient processing pipeline
- 🔧 Customizable summary parameters
- 📊 Summary statistics and metrics

## Learning Focus

This project emphasizes:
1. **Model Understanding**
   - BART architecture and capabilities
   - Transfer learning in NLP
   - Model configuration and parameters

2. **Software Engineering**
   - Clean code practices
   - Project structure
   - Documentation standards
   - Version control

3. **User Experience**
   - Web interface design
   - Error handling
   - User feedback

## Contributing

While this is primarily a learning project, suggestions and improvements are welcome:
1. Fork the repository
2. Create your feature branch
3. Commit your changes with meaningful messages
4. Push to your branch
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for the transformers library
- [BART Model Team](https://arxiv.org/abs/1910.13461) for the base model
- [Streamlit](https://streamlit.io/) for the web framework 