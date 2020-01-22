def parse_delimited_file(filename, delimiter=","):
    # Open and read in all lines of the file
    with open(filename, 'r', encoding='utf8') as dsvfile:
        lines = dsvfile.readlines()

    # Strip off the newline from the end of each line
        lines=[i.rstrip() for i in lines]
        
    # Using list comprehension is the recommended pythonic way to iterate through lists
    # Split each line based on the delimiter (which, in this case, is the comma)
        Split_list=[]
        for i in range(len(lines)):
            Split_list.append(lines[i].split(delimiter))
    
    # Separate the header from the data
        Split_list.pop(0)
        
    # Calculate the number of data rows and columns
        num_data_rows = len(Split_list)
        num_data_cols = len(Split_list[0])
    # Sum the "age" values
    # Calculate the average age
        ave_age = 0
        Total_age=0
        for x in Split_list:
            for y in x:
                y=y.strip()
                if y.isdigit():
                    Total_age+=int(y)
                    ave_age=Total_age/len(Split_list)
            
    # Print the results
    
    print("Number of rows of data: {}".format(num_data_rows))
    print("Number of cols: {}".format(num_data_cols))
    print("Average Age: {}".format(ave_age))



def translit_names(filename,delimiter=","):
    translit_dict = {
    "ä" : "ae",
    "ö" : "oe",
    "ü" : "ue",
    "Ä" : "Ae",
    "Ö" : "Oe",
    "Ü" : "Ue", 
    "ł" : "l",
    "ō" : "o",
    }

    # Open and read in all lines of the file
    with open(filename, 'r', encoding='utf8') as csvfile:
        lines = csvfile.readlines()
        
    # Strip off the newline from the end of each line
        lines=[i.rstrip() for i in lines]

        
    # Using list comprehension is the recommended pythonic way to iterate through lists
    # Split each line based on the delimiter (which, in this case, is the comma)
        Split_list=[]
        for i in range(len(lines)):
            Split_list.append(lines[i].split(delimiter))
    
    # Separate the header from the data
        Split_list.pop(0)

    unicode_names = []
    for x in Split_list:
        unicode_names.append(x[0])
    # Iterate over the names
    translit_names = []
    for unicode_name in unicode_names:
        # Perform the replacements in the translit_dict
        for keys in translit_dict.keys():
            unicode_name=unicode_name.replace(keys,translit_dict[keys])
        translit_names.append(unicode_name)
    # Write out the names to a file named "data-ascii.txt"
    f=open("data-ascii.txt", 'w')
    for x in translit_names:
        f.writelines(x)
        f.writelines('\n')

    # Verify that the names were converted and written out correctly
    with open("data-ascii.txt", 'r') as f:
        for line in f:
            print(line.rstrip())

    

if __name__ == "__main__":
    print('Information of csv files:')
    parse_delimited_file('data.csv')
    print('==========================')
    print('Information of tsv files:')
    parse_delimited_file('data.tsv', delimiter="\t")
    print('==========================')
    print('The name after translation:')
    translit_names('data.csv')