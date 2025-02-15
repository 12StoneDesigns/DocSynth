"""
Document Summary Creator
Author: T. Landon Love
Company: 12Stone Designs
Email: 12stonedesigns@gmail.com
Copyright © 2023 12Stone Designs. All rights reserved.

A sophisticated text summarization tool that processes documents
and generates concise summaries while preserving key information.
"""

from summary_make import create_document_summary
import os
import sys


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


def save_summary(summary, output_path):
    """Save the generated summary to a file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for sentence in summary:
                f.write(str(sentence) + '\n')
        print(f"\nSummary successfully saved to: {output_path}")
    except Exception as e:
        print(f"Error saving summary: {str(e)}")
        sys.exit(1)


def main():
    """Main execution function for the document summarizer."""
    print("\nDocument Summary Creator")
    print("=" * 50)
    
    # Get input file path
    filepath = input("\nPlease enter the path to your text file: ").strip()
    
    # Validate input file
    if not validate_file_path(filepath):
        sys.exit(1)
    
    # Process document
    print("\nProcessing document...")
    document_text = read_document(filepath)
    
    # Generate summary
    print("Generating summary...")
    summary = create_document_summary(document_text)
    
    # Save results
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
