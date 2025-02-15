"""
DocSynth
Author: T. Landon Love
Company: 12Stone Designs
Email: 12stonedesigns@gmail.com
Copyright © 2023 12Stone Designs. All rights reserved.

A sophisticated document synthesis tool that processes documents
and generates concise summaries while preserving key information.
"""

from summary_make import SummaryCreator
import os
import sys
import argparse
import time


def validate_file_path(filepath):
    """Validate the input file path and ensure it's a text file."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return False
    
    if not filepath.lower().endswith('.txt'):
        print("Error: Please provide a valid text (.txt) file.")
        return False
    
    return True


def generate_output_path(input_path):
    """Generate the output file path for the summary."""
    base_path = os.path.splitext(input_path)[0]
    return f"{base_path}_summary.txt"


def read_document(filepath):
    """Read and process the input document."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return ' '.join(f.readlines())
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)


def format_sentence(sentence):
    """Format a sentence for better readability."""
    text = str(sentence).strip()
    
    # Basic text cleanup
    text = text.replace("  ", " ")
    text = text.replace(" 's", "'s")
    
    # Ensure proper sentence ending
    if not text.endswith((".", "!", "?")):
        text += "."
        
    return text


def save_summary(summary, output_path):
    """Save the generated summary to a file."""
    print("\nSummary:")
    
    # Format each sentence
    formatted_sentences = [format_sentence(sentence) for sentence in summary]
    
    # Group sentences by section
    current_section = []
    sections = []
    
    for sentence in formatted_sentences:
        # Check if this is a new section
        if any(marker in sentence for marker in ["Key Features", "Common Applications", "In conclusion"]):
            if current_section:
                sections.append(current_section)
            current_section = [sentence]
        else:
            current_section.append(sentence)
    
    if current_section:
        sections.append(current_section)
    
    # Print sections with proper formatting
    for section in sections:
        # Print each section with a blank line between
        print()
        for sentence in section:
            print(f"• {sentence}")
    
    try:
        # Save to file with same formatting
        with open(output_path, 'w', encoding='utf-8') as f:
            for section in sections:
                f.write("\n")
                for sentence in section:
                    f.write(f"{sentence}\n")
        print(f"\nSaved to: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


def main():
    """Main execution function for the document summarizer."""
    parser = argparse.ArgumentParser(description="DocSynth")
    parser.add_argument("filepath", type=str, help="Input file path")
    parser.add_argument("--compression_ratio", type=float, default=0.3, help="Compression ratio for summary")
    parser.add_argument("--min_sentences", type=int, default=5, help="Minimum number of sentences in summary")
    
    args = parser.parse_args()
    
    filepath = args.filepath
    
    if not validate_file_path(filepath):
        sys.exit(1)
    
    document_text = read_document(filepath)
    
    # Create summary
    summary_creator = SummaryCreator()
    start_time = time.time()
    summary = summary_creator.create_document_summary(
        document_text,
        compression_ratio=args.compression_ratio,
        min_sentences=args.min_sentences
    )
    end_time = time.time()
    
    print(f"Summary generated in {end_time - start_time:.2f} seconds.")
    
    output_path = generate_output_path(filepath)
    save_summary(summary, output_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)
