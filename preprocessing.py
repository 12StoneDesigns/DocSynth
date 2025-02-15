"""
Document Summary Creator - Text Preprocessing Module
Author: T. Landon Love
Company: 12Stone Designs
Email: 12stonedesigns@gmail.com
Copyright © 2023 12Stone Designs. All rights reserved.

This module handles text preprocessing and document analysis
for the document summarization process.
"""

import spacy
import neologdn
from typing import List, Optional


class DocumentProcessor:
    """Handles document preprocessing and linguistic analysis."""
    
    def __init__(self, model: str = "en_core_web_sm"):
        """Initialize the document processor with specified language model.
        
        Args:
            model (str): The spaCy language model to use for processing
        """
        try:
            self.nlp = spacy.load(model)
        except OSError as e:
            raise RuntimeError(f"Failed to load language model '{model}'. Please ensure it's installed.") from e
        
        self._processed_doc = None
        self._sentence_objects = None

    def preprocess_text(self, text: str) -> str:
        """Clean and normalize input text.
        
        Args:
            text (str): Raw input text
            
        Returns:
            str: Preprocessed and normalized text
        """
        # Remove excessive whitespace and normalize line breaks
        text = ' '.join(text.split())
        
        # Normalize text using neologdn
        text = neologdn.normalize(text)
        
        return text

    def extract_sentences(self, text: str) -> List[spacy.tokens.span.Span]:
        """Split text into sentences while preserving linguistic analysis.
        
        Args:
            text (str): Preprocessed input text
            
        Returns:
            List[spacy.tokens.span.Span]: List of sentence objects
        """
        # Process the text with spaCy
        self._processed_doc = self.nlp(text)
        self._sentence_objects = list(self._processed_doc.sents)
        
        return self._sentence_objects

    def create_sentence_corpus(self) -> List[str]:
        """Generate a corpus of properly tokenized sentences.
        
        Returns:
            List[str]: List of processed sentences with proper word spacing
        """
        if not self._sentence_objects:
            raise RuntimeError("No processed sentences available. Call extract_sentences() first.")
        
        corpus = []
        for sent in self._sentence_objects:
            # Extract tokens while preserving important linguistic features
            tokens = [
                token.text for token in sent
                if not (token.is_space or token.is_punct)
            ]
            corpus.append(" ".join(tokens))
        
        return corpus

    def get_sentence_metadata(self) -> List[dict]:
        """Extract metadata about each sentence for potential analysis.
        
        Returns:
            List[dict]: List of sentence metadata including length, complexity indicators
        """
        if not self._sentence_objects:
            raise RuntimeError("No processed sentences available. Call extract_sentences() first.")
        
        metadata = []
        for sent in self._sentence_objects:
            metadata.append({
                'length': len(sent),
                'word_count': len([token for token in sent if not token.is_punct and not token.is_space]),
                'has_named_entities': bool(sent.ents),
                'root_verb': str(sent.root) if sent.root.pos_ == 'VERB' else None
            })
        
        return metadata
