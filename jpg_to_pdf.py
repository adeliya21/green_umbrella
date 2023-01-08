import os
from fpdf import FPDF
from os import listdir

# CREATE A FOLDER FOR PDF FILES
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'pdf_folder')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

# CREATE A LIST OF image_folders by removing non-image_folders in current directory
folders = sorted(os.listdir())
#print(folders)

list_remove = ['.DS_Store', '.idea', 'chapters_url.txt', 'jpg_to_pdf.py', 'main.py', 'pdf_folder', 'r.txt', 'soup.txt', 'venv']
for x in list_remove:
    folders.remove(x)
#print(folders)

# CONVERT IMAGES TO PDF FILES
for folder in folders:

    path = f"{folder}/"
    imagelist = listdir(path) # gets list of all images (in arbitrary order)
    #print(imagelist)
    sorted_imagelist = sorted(imagelist, key = lambda x: (len (x), x))
    #print(sorted_imagelist)

    pdf = FPDF('P','mm', (750.0,850.0)) # create 750,850-size pdf document

    x,y,w,h = 0,0,750,850

    for image in sorted_imagelist:
        pdf.add_page()
        pdf.image(f"{path}/{image}",x,y,w,h)

    pdf.output(f"pdf_folder/{folder}.pdf","F")

dir = os.listdir("pdf_folder/")
    if (len(dir) != 0):
        print(f'pdf_folder has {len(dir)} elements:')
        print(f'{dir}')
    else:
        print('pdf_folder is empty')