import os

def snake_to_camel_case(list_of_words=None):

    new_list = []
    for w in list_of_words:
        term = w.lower().split("_")
        for i in range(len(term)):
            term[i] = term[i].capitalize()
        new_list.append("".join(term))
    return new_list

def write_to_zip_and_disk(zf=None,
                          copyfile=None,
                          removefile=None):

    os.system("cp {} .".format(copyfile))
    zf.write(removefile)
    os.system("rm {}".format(removefile))

def add_file_to_dwca(zf=None,
                     dataframe=None,
                     publishing_dir=None,
                     file_to_write=None):
    
    # check if your data file has been written
    if not os.path.exists("{}".format(file_to_write)):
        dataframe.to_csv("{}".format(file_to_write),index=False)

    # first, write occurrences to zip and disk
    zf.write("{}/{}".format(publishing_dir,file_to_write))