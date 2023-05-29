from PyPDF2 import PdfMerger
import glob
import os

def get_pdf_names(folder):
    path = os.path.join(folder, '*.pdf')
    pdf_files = glob.glob(path)
    return [os.path.basename(file) for file in pdf_files]  # Return only file names

def merge_pdf(files, output_name):
    merger = PdfMerger()
    
    for file in files:
        merger.append(file)

    merger.write(output_name)
    merger.close()

# Folder where the PDF files are located
folder = './docs'

# Call the function to get the PDF file names
pdf_names = get_pdf_names(folder)

# Print the PDF file names
print(pdf_names)

# Output file name
output_name = 'final_file.pdf'

# Build the full path for each PDF file
file_paths = [os.path.join(folder, file) for file in pdf_names]

# Call the function to merge the PDFs
merge_pdf(file_paths, output_name)

print('The files were merged successfully!')
