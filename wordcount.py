# This function is simple and does not account for the punctuation issues
# def word_count(file_name):
# """Function takes in a text file reads though each line and creates a dicitonary word and word count pairs.
#     Returns None but prints the key-value pairs """
#     file_content = open(file_name)
#     word_count_dict = {}
#     for file_line in file_content:
#         #clean_line is a list of words
#         clean_line = file_line.rstrip().split(" ")

#         for word in clean_line:
#             word_count_dict[word] = word_count_dict.get(word, 0) + 1
   
#         for word_key in sorted(word_count_dict):
#             print word_key, word_count_dict[word_key]


# word_count("test.txt")
def open_file_tokenized(file_name):
    """ Function takes arguement file and Returns a list of all words in file white space removed. """
    file_content = open(file_name)
    for file_line in file_content:
        #clean_line is a list of words
        return file_line.rstrip().split(" ")

def word_cleaner(file_name):
    clean_line = open_file_tokenized(file_name) 
    
    clean_list = []
    for word in clean_line:
        if word == "&":
            word = "and"
            #CLEAN THIS UP STRIP DOESN"T WORK THIS WAY NEED TO DO A LIST LOOP OVER OR REGULAR EXPRESSIONS
        word = word.lower().strip("#", ".", ",", "!", "\"", "\'", ":", ";")

        clean_word = ""
        if word.isalpha() == False:
            for char in word:
               if char.isalpha():
                    clean_word = clean_word + char 
            word = clean_word
            clean_list.append(word)
    return clean_list
print word_cleaner("test.txt")

def word_count(file_name):
    word_list = word_cleaner(file_name)

    word_count_dict = {}
    for word in word_list:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    for word_key in sorted(word_count_dict):
        print word_key, word_count_dict[word_key]


word_count("test.txt")








