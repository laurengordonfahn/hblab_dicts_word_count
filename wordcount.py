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



def word_count(file_name):
    file_content = open(file_name)
    word_count_dict = {}
    for file_line in file_content:
        #clean_line is a list of words
        clean_line = file_line.rstrip().split(" ")

        for word in clean_line:
            word_count_dict[lower(word)] = word_count_dict.get(word, 0) + 1
   
        for word_key in sorted(word_count_dict):
            print word_key, word_count_dict[word_key]


word_count("test.txt")








