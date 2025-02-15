# DocSynth

A sophisticated document synthesis tool that creates concise summaries of text documents using advanced NLP techniques.

## Author
T. Landon Love  
12Stone Designs  
12stonedesigns@gmail.com

## Overview
DocSynth uses state-of-the-art natural language processing to analyze text documents and generate meaningful summaries. It employs the LexRank algorithm to identify and extract the most significant sentences, producing a summary that captures the essential information while maintaining the document's key insights and structure.

## Prerequisites
This application requires Python 3.x and the following dependencies:
* sumy - For text summarization
* spacy - For natural language processing
* neologdn - For text normalization
* PyMuPDF - For PDF processing
* python-docx - For Word document processing

## Installation

1. Install required Python packages:
```bash
pip install -r requirements.txt
```

2. Download required language model:
```bash
python -m spacy download en_core_web_trf
```

## Usage
Run the application with a text file:
```bash
python main.py <filepath> [--compression_ratio 0.3] [--min_sentences 5]
```

Arguments:
- `filepath`: Path to the input text file
- `--compression_ratio`: Target ratio of summary to original length (default: 0.3)
- `--min_sentences`: Minimum number of sentences in summary (default: 5)

The program will generate a summary file with the suffix '_summary.txt' in the same directory as your input file.

## Features
* Intelligent sentence selection using LexRank algorithm
* Customizable compression ratio and minimum sentence count
* Preserves document structure and section formatting
* Advanced text preprocessing for optimal results
* Support for section markers and hierarchical content
* Clean and readable output formatting

© 2023 12Stone Designs. All rights reserved.
