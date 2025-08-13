#!/usr/bin/env python3
"""
PDF Merger Script
Merges two PDF files into a single output PDF.

SETUP: 
.venv\scripts\activate
pip install PyPDF2

USAGE:
python merge_pdfs.py file1.pdf file2.pdf output.pdf
python merge_pdfs.py portfolio.pdf cover.pdf 0245-145347166-92007.pdf


"""

import PyPDF2
import sys
import os

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    """
    Merge two PDF files into one.
    
    Args:
        pdf1_path (str): Path to the first PDF file
        pdf2_path (str): Path to the second PDF file
        output_path (str): Path for the merged output PDF
    """
    try:
        # Create a PDF merger object
        merger = PyPDF2.PdfMerger()
        
        # Check if input files exist
        if not os.path.exists(pdf1_path):
            raise FileNotFoundError(f"First PDF file not found: {pdf1_path}")
        if not os.path.exists(pdf2_path):
            raise FileNotFoundError(f"Second PDF file not found: {pdf2_path}")
        
        # Add the first PDF
        print(f"Adding {pdf1_path}...")
        merger.append(pdf1_path)
        
        # Add the second PDF
        print(f"Adding {pdf2_path}...")
        merger.append(pdf2_path)
        
        # Write the merged PDF to output file
        print(f"Writing merged PDF to {output_path}...")
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        
        merger.close()
        print(f"Successfully merged PDFs into: {output_path}")
        
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False
    
    return True

def main():
    """Main function to handle command line arguments or interactive input."""
    
    if len(sys.argv) == 4:
        print("Machine mode.")
        # Command line arguments provided
        pdf1_path = sys.argv[1]
        pdf2_path = sys.argv[2]
        output_path = sys.argv[3]
        print("Merging {} and {}".format(pdf1_path, pdf2_path))
    else:
        # Interactive input
        print("PDF Merger Tool")
        print("-" * 20)
        
        pdf1_path = input("Enter path to first PDF file: ").strip()
        pdf2_path = input("Enter path to second PDF file: ").strip()
        output_path = input("Enter output file path (e.g., merged.pdf): ").strip()
        
        # Add .pdf extension if not provided
        if not output_path.endswith('.pdf'):
            output_path += '.pdf'
    
    # Perform the merge
    success = merge_pdfs(pdf2_path, pdf1_path, output_path)
    
    if success:
        print("\n✅ PDF merge completed successfully!")
    else:
        print("\n❌ PDF merge failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()