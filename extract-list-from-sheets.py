# spreadsheet of comic page info and links to images for embedding in pages

def parse_csv(filename):
    
    # comic_title = [(file_name, file_link), (file_name, file_link), ..]
    space_story_paso    = []
    space_story_tix     = []
    self_destruct       = []
    loose_end           = []
    rat_boy_holiday     = []
    rat_boy_hourlies_22 = []
    rat_boy_hourlies_23 = []
    
    # open and read csv
    file = open(filename, 'r').readlines()

    row = 1
    for row_text in file:

        row_text = row_text.strip().split(',')

        if row > 1:
            column = 1
            for cell in row_text:
                if cell != "":
                    ## Space Story: Piss and Shit Olympics
                    if   column == 1: 
                        file_name = 'space-story-1-'+str(row-2).zfill(3)
                    elif column == 3:
                        file_link = cell
                        name_file = (file_name, file_link)
                        space_story_paso.append(name_file)
                    
                    ## Space Story: Termina IX
                    elif column == 4: 
                        file_name = 'space-story-2-'+str(row-2).zfill(3)
                    elif column == 6:
                        file_link = cell
                        name_file = (file_name, file_link)
                        space_story_tix.append(name_file)

                    ## Self-Destruct Sequence
                    elif column == 7: 
                        file_name = 'self-destruct-1-'+str(row-2).zfill(3)
                    elif column == 9:
                        file_link = cell
                        name_file = (file_name, file_link)
                        self_destruct.append(name_file)
                    
                    ## Loose End
                    elif column == 10: 
                        file_name = 'loose-end-1-'+str(row-2).zfill(3)
                    elif column == 12:
                        file_link = cell
                        name_file = (file_name, file_link)
                        loose_end.append(name_file)
                    
                    ## Rat Boy Holiday
                    elif column == 13: 
                        file_name = 'holiday-1-'+str(row-2).zfill(3)
                    elif column == 15:
                        file_link = cell
                        name_file = (file_name, file_link)
                        rat_boy_holiday.append(name_file)

                    ## Rat Boy Hourlies 2022
                    elif column == 16: 
                        file_name = 'hourlies-22-1-'+str(row-2).zfill(3)
                    elif column == 18:
                        file_link = cell
                        name_file = (file_name, file_link)
                        rat_boy_hourlies_22.append(name_file)
                    
                    ## Rat Boy Hourlies 2023
                    elif column == 19: 
                        file_name = 'hourlies-23-1-'+str(row-2).zfill(3)
                    elif column == 21:
                        file_link = cell
                        name_file = (file_name, file_link)
                        rat_boy_hourlies_23.append(name_file)
                column += 1
        row += 1
    
    all_comics = [space_story_paso, space_story_tix, self_destruct, loose_end, rat_boy_holiday, rat_boy_hourlies_22, rat_boy_hourlies_23]

    return all_comics

def write_to_file(all_comics):
    # all_comics = [[comic], [comic]]
    #  comic     = [comic_title, (page), (page)]
    #    page    = (name, link)

    comic_titles = ['Space Story: Piss and Shit Olympics', 'Space Story: Termina IX', 'Self Destruct Sequence', 'Loose End', 'Rat Boy: Holiday', 'Rat Boy: Hourlies 2022', 'Rat Boy: Hourlies 2023']

    destination_file = 'all-page-locations.txt'
    with open(destination_file, 'w') as f:
        for comic in range(len(all_comics)):
            f.write(comic_titles[comic])
            for page in all_comics[comic]:
                f.write('\n')
                new_line = ' '.join([page[0]+' '+page[1]])
                f.write(new_line)
            f.write('\n\n')

def main():
    filename = 'comic-embed-links.csv'
    all_comics = parse_csv(filename)
    write_to_file(all_comics)

    print("complete")

main()