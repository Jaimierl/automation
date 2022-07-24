from ast import parse
from os import removedirs
import re


def read_file(file_path):
    """Example from Madlibs on how to read a file from a path."""
    #This takes in a file_path which it uses to open the file, strip the contents, and returns the stripped contents. Stripping is just removing the leading and trailing characters, which are spaces unless otherwise specified. 
    try:
        with open(file_path) as f:
            contents = f.read()
            # print (contents)
            return contents.strip()
    except FileNotFoundError:
       raise FileNotFoundError("This path leads to a dead end and cannot be followed") 


def parse_emails(input_text):
    """This reads the emails and exports them on new lines to the emails.txt file."""
    # \S matches any non-whitespace character 
    # @ for as in the Email 
    # + for Repeats a character one or more times 
    find_emails = re.findall('\S+@\S+', input_text)
    find_emails.sort()
    # .sort works IN PLACE!!!! DO NOT!!! assign to a new variable.

    single = set(find_emails)
    unique = list(single)
    unique.sort()

    print(unique)

    with open("emails.txt", mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(unique))
        myfile.write('\n')


def parse_numbers(input_text):
    """This reads the input TEXT (not file) returns the phone numbers (just 7 or 10 digit numbers - extensions are not handled) into the numbers.txt file."""
    # find_numnums = re.findall('(\d{3})[-. ]*(\d{4})\S+', input_text)
    # This gives the middle three and last 4 numbers as tuples

    
    find_numnums = re.findall('(\d{3})?(\d{3})[-. ]*(\d{4})\S+', input_text)
    # This is looking for an optional three initial numbers (with a question mark), three numbers, 4 numbers, possibly divided by some symbol for the second two sets of numbers. This gives back a tuple with three list seperted strings of 0/3 (maybe) then 3, then 4 numbers.
    set_hut = set(find_numnums)
    listify = list(set_hut)

    listify.sort()
    # Remember, this is happening in place.

    lists_only = []
    for i in listify:
        lists_only.append(list(i))
    # Turns all of the phone number tuples into lists

    for i in lists_only:
        if i[0]=='':
            i[0]='206'    
    
    numbers_list = []
    for i in lists_only:
        numbers_list.append('-'.join(i))

    print(numbers_list)

    with open("numbers.txt", mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(numbers_list))
        myfile.write('\n')


def file_save(funny_string):
    """Example from Madlibs on how to write to a file at a path."""
    with open ("assets/funny_file.txt", "w") as f:
        text = f.write(funny_string)



if __name__=="__main__":
    read = read_file("potential-contacts.txt")
    # parse_emails(read)
    parse_numbers(read)