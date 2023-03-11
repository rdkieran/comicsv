# spreadsheet of comic page info and links to images for embedding in pages

import os
import shutil

def parse_csv(csv_file):
    all_pages = []
    accepted_file_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp', 'ico', 'tif', 'tiff']

    ## account for files with spaces
    if csv_file.startswith('&') == True:
            csv_file = csv_file.split("'")[1]

    # open and read csv
    file = open(csv_file, 'r').readlines()
    
    for line in file:
        file_extension = line.strip().split(',')[0].split('.')[-1]

        if file_extension in accepted_file_extensions:

            link = line.strip().split(',')[1]
            key  = link.split('/d/')[-1].split('/view?')[0]
            link = 'https://drive.google.com/uc?export=view&id='+key

            all_pages.append(link)
    
    all_pages.reverse()

    return all_pages

def make_directory(csv_file, project_name):

    if csv_file.startswith('&') == True:
            csv_file = csv_file.split("'")[1]

    folder_path = '\\'.join(csv_file.split('\\')[:-1])
    destination_folder = '-'.join(project_name.split(' '))

    destination_path = os.path.join(folder_path, destination_folder)
    try: 
        shutil.rmtree(destination_path)
        os.mkdir(destination_path)
    except:
        os.mkdir(destination_path)

    return destination_path

def write_to_file(all_pages, project_name, destination_path):
    # all_pages = [page1, page2, ..]
    # project_name = 'example name 1'

    # 'example name 1' > 'example-name-1.txt'
    destination_file = destination_path+'\\'+'-'.join(project_name.split(' '))+'.txt'
    
    # start page naming system for output info
    page_number = 1
    number_of_pages = len(all_pages)
    page_number_digit_count = len(str(number_of_pages))

    with open(destination_file, 'w') as f:
        for link in all_pages:
            page_info = project_name+','+str(page_number).zfill(page_number_digit_count)+','+link+'\n'

            f.write(page_info)

            page_number += 1

def write_html(all_pages, project_name, destination_path):
    # all_pages = [page1, page2, ..]
    # project_name = 'example name 1'
    
    # 'example name 1' > 'example-name-1'
    project_name_joined = '-'.join(project_name.split(' '))

    project_name = project_name.split(' ')
    project_name_capitalized = []
    for word in project_name:
        project_name_capitalized.append(word.capitalize())
    project_name = ' '.join(project_name_capitalized)
    
    # get template
    template = 'convert-to-html\\template.html'
    template = ''.join(open(template).readlines())

    page_number = 1
    number_of_pages = len(all_pages)
    page_number_digit_count = len(str(number_of_pages))

    for page in range(len(all_pages)):

        page_html = project_name.join(template.split('[[PROJECT NAME]]'))
        page_html = str(page_number).join(page_html.split('[[PAGE NUMBER]]'))

        page_html = all_pages[page].join(page_html.split('[[SOURCE]]'))
        page_html = (project_name+', Page '+str(page_number)).join(page_html.split('[[ALT]]'))

        destination_file = destination_path+'\\'+str(page_number).zfill(page_number_digit_count)+'.html'
        with open(destination_file, 'w') as f:
            f.write(page_html)

        page_number += 1
            
def main():
    project_name = input("comic name: ")
    csv_file = input("input .csv file: ")
    
    destination_path = make_directory(csv_file, project_name)

    all_pages = parse_csv(csv_file)
    write_to_file(all_pages, project_name, destination_path)
    write_html(all_pages, project_name, destination_path)

    destination_file = '-'.join(project_name.split(' '))+'.txt'
    print("\ncomplete")

main()