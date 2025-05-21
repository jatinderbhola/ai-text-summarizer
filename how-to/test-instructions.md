# Testing the AI Text Summarizer

This guide explains how to run all types of tests in this project, including unit tests, script-style tests, and manual playgrounds.

## Test Types

### 1. Unit Tests
- **Location:** `project/tests/test_summarizer.py`
- **Framework:** Python `unittest`
- **Purpose:** Automated, repeatable checks for summarizer correctness and edge cases.
- **How to run:**
  - From the `project` directory:
    ```bash
    python -m unittest discover -s tests -p "test_*.py"
    # or
    python -m tests.test_summarizer
    ```

### 2. Script-Style Tests
- **Location:** `project/tests/test_summarizer_script.py`
- **Framework:** Plain Python script (print-based)
- **Purpose:** Manual, console-based inspection of summarizer output for all sample texts.
- **How to run:**
  - From the `project` directory:
    ```bash
    python -m tests.test_summarizer_script
    # or
    python tests/test_summarizer_script.py
    ```

### 3. Manual Playground
- **Location:** `project/tests/sample_texts.py`
- **Purpose:** For quick, ad-hoc experiments and trying new sample texts file.

## Notes
- Always run test commands from the `project` directory (not from inside `tests`).
- The `tests` folder must contain an `__init__.py` file (it does by default).
- The `test_data.py` file contains all shared sample texts for both unit and script tests.

## Summary Table

| Test Type      | File                                 | How to Run (from `project/`)           | Output Style         |
|----------------|--------------------------------------|----------------------------------------|----------------------|
| Unit tests     | `tests/test_summarizer.py`           | `python -m tests.test_summarizer`      | Pass/fail, asserts   |
| All unit tests | `tests/`                             | `python -m unittest discover -s tests` | Pass/fail, asserts   |
| Script test    | `tests/test_summarizer_script.py`    | `python -m tests.test_summarizer_script` | Console printouts    |
| Manual test    | `tests/sample_texts.py`              | `python tests/sample_texts.py`         | Console printouts    | 