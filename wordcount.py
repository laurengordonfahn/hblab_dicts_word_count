def word_count(file_name):
    file_content = open(file_name)
    word_count_dict = {}
    for file_line in file_content:
        #clean_line is a list of words
        clean_line = file_line.rstrip().split(" ")

        for word in clean_line:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
   
        for word_key in sorted(word_count_dict):
            print word_key, word_count_dict[word_key]


word_count("test.txt")






