from itertools import zip_longest
import constants

def get_metadata(files): # Returns a list containing the metadata
    path = constants.PATH + files[constants.FOLDERS] + "/" + files[constants.TEXT_FILE]
    with open(path, "r") as f:
        first_line = f.readline().strip() # Reads first line in text file

    # metadata is a list taken from the first line of textfiles
    metadata = [int(item.strip()) for item in first_line.strip().split(",")]
    return metadata

def get_img(files): # returns a list containing the image
    path = constants.PATH + files[constants.FOLDERS] + "/" + files[constants.TEXT_FILE]

    lines = list()
    with open(path, "r") as f:
        for line in f:
            lines.append(line)

    lines = lines[1:] # Slices passed the metadata
    return lines

def get_md_img(files): # returns both md and img lists as a tuple
    metadata = get_metadata(files)
    img = get_img(files)

    return img, metadata

def print_list(lst_img): # prints a lst img
    for line in lst_img:
        print(line, end="")
    print("\n") # adds two spaces after this

def indent_img(files): # returns an indented img_lst
    img_lst, md_lst = get_md_img(files)

    folder = files[constants.FOLDERS]

    # sets variables based on folder location
    if folder.startswith(constants.PLAYER_FOLDER): # player img
        indent = " " * constants.INDENT
        hand_height = md_lst[constants.META_CHARACTERS["HAND_HEIGHT"]]
        
        if hand_height != 0:
            bottom = hand_height

    elif folder.startswith(constants.CHARACTERS_FOLDER): # character img
        indent = " " * (constants.INDENT//10)
        hand_height = md_lst[constants.META_CHARACTERS["HAND_HEIGHT"]]

        if hand_height != 0:
            bottom = hand_height
        
    elif folder.startswith(constants.ITEMS_FOLDER): # item img
        indent = " " * ((constants.INDENT//3)*2)
        bottom = constants.FLOOR

    while len(img_lst) <= bottom:
        img_lst.insert(0, "\n")

    

    new_img_lst = list()

    for line in img_lst:
        if not line.startswith("\n") and line:
            new_img_lst.append(indent + line)
        else:
            new_img_lst.append(line)

    return new_img_lst

def combine_files(files1, files2): # combines two files, returns the lst

    img1_lst = indent_img(files1)
    img2_lst = indent_img(files2)

    combined = list()

    for line2, line1 in zip_longest(img2_lst, img1_lst, fillvalue=" "): # evens the lst lengths

        new_line = list()
        
        if line2.startswith("\n"):
            new_line.append(line1) # line1 overides the line if nothing on line2
        elif line1.startswith("\n"):
            new_line.append(line2) # line2 overides the line if nothing on line1
        else:
            # Strips the \n so its not in middle of line later
            line2 = line2.strip("\n")
            line1 = line1.strip("\n")

            # Loops through char to find differences
            for char2, char1 in zip_longest(line2, line1, fillvalue=" "): # Makes line2 and line1 strings even
                if char2 == char1:
                    new_line.append(char1) # Overides as char1 if chars are equal
                else:
                    if char1 != " ":
                        new_line.append(char1) # Overides if its not " "
                    else:
                        new_line.append(char2) # Secondary if char1 is " "

        combined.append("".join(new_line))

    return combined


        