"""
AI Text Summarizer using Hugging Face Transformers
"""

import logging
from typing import Dict, Optional, Union

from transformers import pipeline
from transformers.pipelines.base import Pipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
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
                    "summarization", model=self.model_name, device=-1  # CPU by defaul
                )
                logger.info("Summarization pipeline loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load summarization pipeline: {str(e)}")
                raise
        return self._summarizer

    def summarize(
        self, text: str, max_length: int = 130, min_length: int = 30, do_sample: bool = False
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
            # Clean and preprocess tex
            text = text.strip()

            # Generate summary
            result = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=do_sample,
                early_stopping=True,
            )

            # Extract and return summary
            summary = result[0]["summary_text"]

            return {
                "summary": summary,
                "original_length": len(text.split()),
                "summary_length": len(summary.split()),
                "compression_ratio": len(summary.split()) / len(text.split()),
            }

        except Exception as e:
            logger.error(f"Summarization failed: {str(e)}")
            raise


def generate_summary(text: str, max_length: int = 130, min_length: int = 30) -> str:
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
    return result["summary"]


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
