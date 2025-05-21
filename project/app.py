"""
Streamlit web interface for the AI Text Summarizer
"""

import streamlit as st
from summarizer import TextSummarizer, generate_summary

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Header
    st.title("📝 AI Text Summarizer")
    st.markdown("""
    This app uses state-of-the-art AI to generate concise summaries of your text.
    Powered by the BART-large-CNN model from Facebook/Meta AI.
    """)
    
    # Sidebar
    st.sidebar.header("⚙️ Configuration")
    
    max_length = st.sidebar.slider(
        "Maximum summary length (words)",
        min_value=50,
        max_value=500,
        value=130,
        help="The maximum length of the generated summary"
    )
    
    min_length = st.sidebar.slider(
        "Minimum summary length (words)",
        min_value=10,
        max_value=100,
        value=30,
        help="The minimum length of the generated summary"
    )
    
    # Main content
    text_input = st.text_area(
        "Enter your text to summarize:",
        height=200,
        help="Paste your article, document, or any text you want to summarize"
    )
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if st.button("Generate Summary", type="primary"):
            if not text_input.strip():
                st.error("Please enter some text to summarize.")
            else:
                try:
                    with st.spinner("Generating summary..."):
                        summarizer = TextSummarizer()
                        result = summarizer.summarize(
                            text_input,
                            max_length=max_length,
                            min_length=min_length
                        )
                        
                        # Display summary
                        st.success("Summary generated successfully!")
                        st.markdown("### Summary")
                        st.write(result['summary'])
                        
                        # Display metrics
                        st.markdown("### Metrics")
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric(
                                "Original Length",
                                f"{result['original_length']} words"
                            )
                        
                        with col2:
                            st.metric(
                                "Summary Length",
                                f"{result['summary_length']} words"
                            )
                        
                        with col3:
                            st.metric(
                                "Compression Ratio",
                                f"{result['compression_ratio']:.2%}"
                            )
                            
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
    
    # Additional information
    with st.expander("ℹ️ About this app"):
        st.markdown("""
        ### How it works
        
        This app uses the BART-large-CNN model, which was trained on a large dataset
        of news articles and their summaries. The model uses advanced natural language
        processing techniques to understand the input text and generate a coherent,
        concise summary.
        
        ### Tips for better results
        
        1. The model works best with well-structured text
        2. Ideal input length is between 100 and 1000 words
        3. Use clear, grammatically correct text for better summaries
        4. Adjust the length parameters based on your needs
        
        ### Resources
        
        - [BART Model Paper](https://arxiv.org/abs/1910.13461)
        - [Hugging Face Model Card](https://huggingface.co/facebook/bart-large-cnn)
        - [Project Repository](https://github.com/yourusername/ai-text-summarizer)
        """)

if __name__ == "__main__":
    main() 