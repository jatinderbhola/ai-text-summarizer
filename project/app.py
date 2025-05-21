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

# Custom CSS for layout and styling
st.markdown("""
<style>
    /* Main container styling */
    .main-content {
        margin-bottom: 100px;
    }
    
    /* Header and description styling */
    .app-header {
        margin-bottom: 1rem;
    }
    .app-description {
        margin-bottom: 2rem;
        color: #444;
        font-size: 1.1em;
        line-height: 1.5;
    }
    
    /* Footer styling */
    footer {
        position: fixed;
        bottom: 0;
        left: 0;
        /* On large screens, leave space for sidebar */
        margin-left: 21rem;
        right: 0;
        background-color: white;
        padding: 1.5rem 0;
        border-top: 1px solid #ddd;
        z-index: 1000;
        width: auto;
        transition: margin-left 0.2s;
    }
    @media (max-width: 1200px) {
        footer {
            margin-left: 0;
        }
    }
    .main-content, .block-container {
        padding-bottom: 120px !important; /* Adjust to footer height */
    }
    @media (max-width: 768px) {
        footer {
            position: static;
            width: 100%;
            margin-left: 0;
            padding: 1.5rem 0;
        }
        .main-content, .block-container {
            padding-bottom: 0 !important;
        }
    }
    .footer-content {
        display: flex;
        justify-content: space-around;
        align-items: start;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    .footer-section {
        flex: 1;
        padding: 0 1rem;
    }
    .footer-section h3 {
        color: #24292e;
        font-size: 1rem;
        margin-bottom: 0.75rem;
        font-weight: 600;
    }
    .footer-section a {
        color: #0366d6;
        text-decoration: none;
        display: block;
        margin: 0.5rem 0;
        font-size: 0.9rem;
        transition: color 0.2s ease;
    }
    .footer-section a:hover {
        color: #1b1f23;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .footer-content {
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        .footer-section {
            margin-bottom: 1.5rem;
        }
    }
    
    /* Streamlit component overrides */
    .stTextArea > label {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .stButton > button {
        margin-top: 1rem;
    }
    .stAlert {
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="app-header">', unsafe_allow_html=True)
    st.title("📝 AI Text Summarizer")
    st.markdown(
        '<div class="app-description">'
        'This app uses state-of-the-art AI to generate concise summaries of your text. '
        'Powered by the BART-large-CNN model from Facebook/Meta AI.'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Main content
    
    # Sidebar configuration
    st.sidebar.header("⚙️ Configuration")
    
    min_length = st.sidebar.slider(
        "Minimum summary length (words)",
        min_value=10,
        max_value=100,
        value=30,
        help="The minimum length of the generated summary"
    )

    max_length = st.sidebar.slider(
        "Maximum summary length (words)",
        min_value=50,
        max_value=500,
        value=130,
        help="The maximum length of the generated summary"
    )
    
    # Text input and summary generation
    text_input = st.text_area(
        "Enter your text to summarize:",
        height=200,
        help="Paste your article, document, or any text you want to summarize"
    )
    
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
                    
                    # Display metrics in a wider layout
                    st.markdown("### Metrics")
                    metrics_cols = st.columns([1, 1, 1])
                    
                    with metrics_cols[0]:
                        st.metric(
                            "Original Length",
                            f"{result['original_length']} words"
                        )
                    
                    with metrics_cols[1]:
                        st.metric(
                            "Summary Length",
                            f"{result['summary_length']} words"
                        )
                    
                    with metrics_cols[2]:
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
        
        ### Technical Resources
        
        - [BART Model Paper](https://arxiv.org/abs/1910.13461)
        - [Hugging Face Model Card](https://huggingface.co/facebook/bart-large-cnn)
        """)
    
    # Footer with author details (sticky)
    st.markdown("""
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>Author</h3>
                <p><strong>Jatinder (Jay) Bhola</strong></p>
                <a href="https://linkedin.com/in/jatinderbhola" target="_blank">LinkedIn Profile</a>
            </div>
            <div class="footer-section">
                <h3>Connect</h3>
                <a href="https://github.com/jatinderbhola" target="_blank">GitHub</a>
                <a href="https://www.dicecape.com" target="_blank">Website</a>
            </div>
            <div class="footer-section">
                <h3>Project</h3>
                <a href="https://github.com/jatinderbhola/ai-text-summarizer" target="_blank">Repository</a>
                <a href="https://github.com/jatinderbhola/ai-text-summarizer/issues" target="_blank">Report Issues</a>
            </div>
        </div>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 