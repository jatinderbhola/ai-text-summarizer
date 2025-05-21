# Development Guide

This document provides guidance for contributors and maintainers working on the AI Text Summarizer project. It covers changelog automation, testing, and other development best practices.

## 🛠️ Developer Environment Setup

### 📝 Required deps

**Lint and Formatting**

Before contributing, install the following tools in your virtual environment:

```bash
pip install flake8
pip install black
```

- Use `make lint` to check code style with flake8.
- Use `make format` to auto-format code with black (if enabled in Makefile).


**Changelog Automation**

This project uses [auto-changelog](https://github.com/CookPete/auto-changelog) to generate and update `CHANGELOG.md` from commit history.

**To update the changelog:**
1. Make sure you have [Node.js](https://nodejs.org/) installed.
2. Install auto-changelog globally (one-time):
   ```bash
   npm install -g auto-changelog
   ```
3. Run:
   ```bash
   make changelog
   # or
   auto-changelog -p
   ```

**Note:**
- You only need this if you want to update the changelog (e.g., for releases or PRs).
- Regular users and contributors do **not** need Node.js or auto-changelog to use the Python app or run tests.

---

## 🧪 Testing

All test types are documented in [how-to/test-instructions.md](how-to/test-instructions.md).

- **Unit tests:**
  - Location: `project/tests/test_summarizer.py`
  - Run: `make test` or `python -m project.tests.test_summarizer`
- **Script-style tests:**
  - Location: `project/tests/test_summarizer_script.py`
  - Run: `make test-script` or `python -m project.tests.test_summarizer_script`
- **Manual playground:**
  - Location: `project/tests/sample_texts.py`
  - Run: `make test-manual` or `python project/tests/sample_texts.py`

---

## 🧹 Linting & Cleaning

- **Lint the codebase:**
  - Run: `make lint` (requires `flake8`)
- **Clean Python cache files:**
  - Run: `make clean`

### 🧹 Lint, Format, and Auto-Fix

**Install these tools in your virtual environment:**

```bash
pip install flake8 black autoflake
```

- Use `make lint` to check code style with flake8.
- Use `make format` to auto-format code with black.
- Use `make autoflake` to remove unused imports and variables.
- Use `make fix` to run autoflake, black, and flake8 in sequence for a full auto-fix and lint check.

---

## 🛠️ Other Development Notes

- **Virtual Environment:**
  - All Python dependencies are managed in `model/bart-cnn/requirements.txt`.
  - Activate the virtual environment before running or developing.
- **Commit Messages:**
  - Use [Conventional Commits](https://www.conventionalcommits.org/) for clarity and better changelog automation.
- **Project Structure:**
  - See the root `README.md` for a detailed project structure and file descriptions.
- **Documentation:**
  - All user and developer documentation is in the `how-to/` folder and the root `README.md`.

---

For any questions or to propose improvements, please open an issue or pull request on [GitHub](https://github.com/jatinderbhola/ai-text-summarizer). 