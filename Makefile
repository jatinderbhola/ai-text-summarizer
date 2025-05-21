# Makefile for AI Text Summarizer Project

.PHONY: app summarizer test test-script test-manual lint format autoflake fix clean changelog

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

# Format the project (requires black)
format:
	black project/

# Lint the project (requires flake8)
lint:
	flake8 project/

# Remove unused imports and variables (requires autoflake)
autoflake: 
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r project/

# Auto-fix: autoflake, then black, then flake8
fix: autoflake format lint

# Remove Python cache files
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

# Update the changelog (requires auto-changelog)
changelog:
	auto-changelog -p 