# Makefile for AI Text Summarizer Project

.PHONY: app summarizer test test-script test-manual lint clean

# Run the Streamlit web app
app:
	streamlit run project/app.py

# Run the summarizer as a script (example usage)
summarizer:
	python project/summarizer.py

# Run the main unit test module (so relative imports work)
test:
	python -m project.tests.test_summarizer

# Run the script-style test (console printout)
test-script:
	python -m project.tests.test_summarizer_script


# Remove Python cache files
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete 