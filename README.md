# AI Text Summarizer Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Transformers-orange)](https://huggingface.co/)
[![Model](https://img.shields.io/badge/Model-BART--CNN-green)](https://huggingface.co/facebook/bart-large-cnn)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyTorch](https://img.shields.io/badge/PyTorch-Framework-red)](https://pytorch.org/)
[![AI](https://img.shields.io/badge/AI-Text%20Summarization-brightgreen)](https://github.com/jatinderbhola/ai-text-summarizer)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen)](https://github.com/jatinderbhola/ai-text-summarizer)
[![Tests: documented](https://img.shields.io/badge/Tests-documented-blueviolet)](how-to/test-instructions.md)

[![Author](https://img.shields.io/badge/Author-Jatinder%20(Jay)%20Bhola-blue)](https://www.linkedin.com/in/jatinderbhola)
[![Website](https://img.shields.io/badge/Website-DiceCape.com-lightgrey)](https://www.dicecape.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jatinderbhola-blue)](https://linkedin.com/in/jatinderbhola)

## 🎯 Quick Start

1. **Clone and Setup:**
   ```bash
   git clone https://github.com/jatinderbhola/ai-text-summarizer.git
   cd ai-text-summarizer
   ```

2. **Run the App:**
   ```bash
   cd model/bart-cnn
   python -m venv env && source env/bin/activate  # On Windows: .\env\Scripts\activate
   pip install -r requirements.txt
   cd ../.. && streamlit run project/app.py
   ```

## ⭐ Support & Feedback

If you find this project useful or interesting:

<div align="center">

### Show Your Support

⭐ Star this repository to show your appreciation and help others discover it! ⭐

</div>

> Your support motivates me to create more open-source AI projects and educational content. Every star makes a difference and helps this project reach more developers interested in AI and NLP.

<div align="center">

[![Stargazers](https://img.shields.io/github/stars/jatinderbhola/ai-text-summarizer?style=for-the-badge)](https://github.com/jatinderbhola/ai-text-summarizer/stargazers)
[![Forks](https://img.shields.io/github/forks/jatinderbhola/ai-text-summarizer?style=for-the-badge)](https://github.com/jatinderbhola/ai-text-summarizer/network/members)

</div>

<details>
<summary>📖 Project Overview</summary>

A learning-focused project implementing an AI-powered text summarization tool using state-of-the-art natural language processing models. This project uses the BART-large-CNN model from Hugging Face to generate concise and accurate summaries of text content.

### Key Features
- 📝 Text summarization using BART-CNN model
- 🌐 Interactive web interface
- ⚡ Efficient processing pipeline
- 🔧 Customizable summary parameters
- 📊 Summary statistics and metrics

### Learning Objectives
- Working with modern NLP models and transformers
- Understanding model deployment and integration
- Building user interfaces for AI applications
- Managing Python virtual environments
- Following best practices in project structure and documentation
- Learning Git workflow and meaningful commit practices
</details>

## 🧪 Testing Philosophy

This project values both **robust automated testing** and **practical manual inspection**:

- **Unit tests** (in `tests/test_summarizer.py`) ensure core summarization logic is correct, edge cases are handled, and regressions are caught early. These are run automatically and use assertions for reliability.
- **Script-style tests** (in `tests/test_summarizer_script.py`) allow for quick, human-readable inspection of summarizer output on a variety of real-world texts.
- **Manual playgrounds** (in `tests/sample_texts.py`) provide a space for experimentation and rapid prototyping of new test cases or edge scenarios.

All test types are documented in [how-to/test-instructions.md](how-to/test-instructions.md) for easy onboarding and reproducibility.

<details>
<summary>🏗️ Project Structure</summary>

```
ai-text-summarizer/
├── how-to/                              # Learning and Documentation
│   ├── steps.md                         # Step-by-step setup and implementation guide
│   ├── learnings.md                     # Key insights and learning points
│   └── test-instructions.md             # How to run all tests and test types
│
├── model/                               # Model-specific Components
│   └── bart-cnn/                        # BART-CNN Model Implementation
│       ├── config.txt                   # Model configuration and parameters
│       ├── requirements.txt             # Model-specific dependencies
│       └── env/                         # Virtual environment (not tracked)
│
├── project/                             # Core Application Code
│   ├── summarizer.py                    # Main summarization logic
│   ├── app.py                           # Streamlit web interface
│   └── README.md                        # Application-specific documentation
│   └── tests/                           # All tests for the project
│       ├── __init__.py                  # Makes tests a package
│       ├── test_data.py                 # Shared sample texts for tests
│       ├── test_summarizer.py           # Unit tests (unittest framework)
│       ├── test_summarizer_script.py    # Script-style/print-based tests
│       └── sample_texts.py              # Manual playground for new test cases
├── DEVELOPMENT.md                       # Developer/contributor documentation (changelog, testing, dev tools)
├── changelog.md                         # Project progress and changes
├── package.json                         # minimal package json to support auto-changelog
└── .gitignore                           # Git ignore configuration
```

**Test documentation:** See [how-to/test-instructions.md](how-to/test-instructions.md) for how to run all tests and test types.
**Development documentation:** See [DEVELOPMENT.md](DEVELOPMENT.md) for changelog, dev tools, and contributor info.
</details>

<details>
<summary>📚 Documentation & Resources</summary>

### Implementation Guides
- [Step-by-Step Setup Guide](how-to/steps.md) - Complete setup instructions
- [Code Concepts & Explanations](how-to/code-explanations.md) - Advanced Python features explained
- [Learning Journal](how-to/learnings.md) - Development insights and best practices
- [Project Progress](how-to/changelog.md) - Development timeline and changes
- [Test Instructions](how-to/test-instructions.md) - **How to run all tests and test types**
- [Development Guide](DEVELOPMENT.md) - **Dev tools, changelog, and contributor info**

### Key Topics Covered
- Type hints and static typing in Python
- Professional logging practices
- Object-oriented design patterns
- Error handling best practices
- Model deployment considerations
- Performance optimization techniques

### External Resources
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [BART Model Documentation](https://huggingface.co/facebook/bart-large-cnn)
- [Streamlit Guide](https://docs.streamlit.io)
</details>

<details>
<summary>⚙️ Technical Requirements</summary>

### System Requirements
- Python 3.8 or higher
- Git
- Sufficient RAM (minimum 8GB recommended)

### Key Dependencies
- `transformers` - Hugging Face Transformers library for NLP
- `torch` - PyTorch for deep learning operations
- `streamlit` - Web interface framework

See `model/bart-cnn/requirements.txt` for complete list
</details>

<details>
<summary>🎓 Learning Focus</summary>

### Model Understanding
- BART architecture and capabilities
- Transfer learning in NLP
- Model configuration and parameters

### Software Engineering
- Clean code practices
- Project structure
- Documentation standards
- Version control

### User Experience
- Web interface design
- Error handling
- User feedback
</details>

<details>
<summary>🤝 Contributing</summary>

While this is primarily a learning project, suggestions and improvements are welcome:
1. Fork the repository
2. Create your feature branch
3. Commit your changes with meaningful messages
4. Push to your branch
5. Open a Pull Request

[More details](./CONTRIBUTING.md)
</details>

<details>
<summary>📜 License & Acknowledgments</summary>

### License
This project is open source and available under the MIT License.

### Acknowledgments
- [Hugging Face](https://huggingface.co/) for the transformers library
- [BART Model Team](https://arxiv.org/abs/1910.13461) for the base model
- [Streamlit](https://streamlit.io/) for the web framework
</details> 