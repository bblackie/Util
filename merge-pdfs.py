from pypdf import PdfWriter
import os

'''
This script merges all PDF files in a specified directory into a single PDF file.

pip install pypdf
'''



def merge_pdfs_in_directory(input_directory, output_filename="merged_output.pdf"):
    """
    Merges all PDF files found in a specified directory into a single PDF.
    """
    merger = PdfWriter()
    
    pdf_files = []
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(input_directory, filename))
    
    # Sort files if a specific order is desired (optional)
    pdf_files.sort() 

    for pdf_file in pdf_files:
        merger.append(pdf_file)
    
    with open(output_filename, "wb") as output_file:
        merger.write(output_file)

    print(f"PDFs merged successfully into {output_filename}")

# Example usage:
# Create a folder named 'my_pdfs' and place some PDF files inside it
# Then call the function:
# merge_pdfs_in_directory("my_pdfs", "combined_document.pdf")



if __name__ == "__main__":
    merge_pdfs_in_directory("my_pdfs", "my_pdfs\\91909 Marked Script - WP.pdf")