"""
Test script for the AI Text Summarizer using sample texts.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from summarizer import TextSummarizer
from .test_data import (
    SHORT_TEXT,
    TECHNICAL_TEXT,
    HISTORICAL_TEXT,
    NEWS_TEXT,
    SCIENTIFIC_TEXT,
    MULTI_TOPIC_TEXT,
    DIALOGUE_TEXT,
)


def test_text(summarizer, text, name="Text", max_length=130, min_length=30):
    """Test summarization on a specific text."""
    print(f"\nTesting {name}:")
    print("-" * 50)
    try:
        result = summarizer.summarize(text, max_length=max_length, min_length=min_length)
        print(f"Original length: {result['original_length']} words")
        print(f"Summary length: {result['summary_length']} words")
        print(f"Compression ratio: {result['compression_ratio']:.2%}")
        print("\nSummary:")
        print(result['summary'])
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    """Run tests on all sample texts."""
    summarizer = TextSummarizer()

    # Test cases with different lengths
    test_text(summarizer, SHORT_TEXT, "Short Text (Photosynthesis)", max_length=50, min_length=20)
    test_text(summarizer, TECHNICAL_TEXT, "Technical Text (Neural Networks)")
    test_text(summarizer, HISTORICAL_TEXT, "Long Text (Industrial Revolution)", max_length=150, min_length=50)

    # Test cases with different styles
    test_text(summarizer, NEWS_TEXT, "News Article (Quantum Computing)")
    test_text(summarizer, SCIENTIFIC_TEXT, "Scientific Abstract (AlphaFold)")
    test_text(summarizer, MULTI_TOPIC_TEXT, "Multi-topic Text (Climate & Tech)")
    test_text(summarizer, DIALOGUE_TEXT, "Dialogue Text (Apollo 11)")


if __name__ == "__main__":
    main()
