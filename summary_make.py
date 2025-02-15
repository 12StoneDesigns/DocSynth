"""
Document Summary Creator - Summarization Module
Author: T. Landon Love
Company: 12Stone Designs
Email: 12stonedesigns@gmail.com
Copyright © 2023 12Stone Designs. All rights reserved.

This module implements the core summarization logic using
the LexRank algorithm with enhanced preprocessing.
"""

from preprocessing import DocumentProcessor
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer
from typing import List, Optional


def create_document_summary(
    text: str,
    language: str = "english",
    compression_ratio: float = 0.2,
    min_sentences: int = 3
) -> List[str]:
    """
    Generate a summary of the input text using LexRank algorithm.
    
    Args:
        text (str): The input text to summarize
        language (str): Language of the input text
        compression_ratio (float): Target ratio of summary to original length
        min_sentences (int): Minimum number of sentences in summary
        
    Returns:
        List[str]: List of summary sentences
    
    Raises:
        ValueError: If input parameters are invalid
        RuntimeError: If summarization fails
    """
    # Validate inputs
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty")
    
    if not 0 < compression_ratio < 1:
        raise ValueError("Compression ratio must be between 0 and 1")
    
    if min_sentences < 1:
        raise ValueError("Minimum sentences must be at least 1")

    try:
        # Initialize document processor
        processor = DocumentProcessor()
        
        # Preprocess the text
        clean_text = processor.preprocess_text(text)
        
        # Extract and analyze sentences
        sentences = processor.extract_sentences(clean_text)
        
        # Create processed corpus
        corpus = processor.create_sentence_corpus()
        
        # Get sentence metadata for potential refinement
        metadata = processor.get_sentence_metadata()
        
        # Calculate target summary length
        total_sentences = len(corpus)
        target_sentences = max(
            min_sentences,
            int(total_sentences * compression_ratio)
        )
        
        # Initialize parser with processed text
        parser = PlaintextParser.from_string(
            " ".join(corpus),
            Tokenizer(language)
        )
        
        # Configure and run summarizer
        summarizer = LexRankSummarizer()
        summarizer.stop_words = get_stop_words(language)
        
        # Generate summary
        summary = summarizer(
            document=parser.document,
            sentences_count=target_sentences
        )
        
        return summary

    except Exception as e:
        raise RuntimeError(f"Summarization failed: {str(e)}") from e
