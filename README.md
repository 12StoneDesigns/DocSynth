# Document Summary Creator

A Python-based document summarization tool that creates concise summaries of text documents using advanced NLP techniques.

## Author
T. Landon Love  
12Stone Designs  
12stonedesigns@gmail.com

## Overview
This tool uses state-of-the-art natural language processing to analyze text documents and generate meaningful summaries. It employs the LexRank algorithm to identify and extract the most significant sentences, producing a summary that captures the essential information while reducing the content to approximately 20% of the original length.

## Prerequisites
This application requires Python 3.x and the following dependencies:
* sumy - For text summarization
* spacy - For natural language processing
* neologdn - For text normalization

## Installation

1. Install required Python packages:
```bash
pip install -r requirements.txt
```

2. Download required language models:
```bash
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt')"
```

## Usage
1. Run the application:
```bash
python main.py
```
2. When prompted, enter the path to your text file
3. The program will generate a summary file with the suffix '_summary.txt' in the same directory as your input file

## Features
* Intelligent sentence selection using LexRank algorithm
* Preserves context and meaning while reducing text length
* Handles complex document structures
* Maintains original text formatting
* Automated preprocessing for optimal results

© 2023 12Stone Designs. All rights reserved.
