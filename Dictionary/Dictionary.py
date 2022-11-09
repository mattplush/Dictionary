# uses Python dictionary collection to simulate an english dictionary. Enter a word to see its definitions


my_dict = {}
keep_going = True

path = __file__[0:len(__file__)-13] + 'Input\\fullfile.txt'
with open(path,'r') as dictFile:

    for line in dictFile:
        line = line.strip()
        if line:
            d_name = ""
            d_def = ""
            line_length = len(line)
            i = 0
            while i in range(line_length) and line[i] != '(':
                d_name += line[i]
                i = i + 1
            d_name = d_name.strip()
            for i in range(i,len(line)):
                d_def += line[i]

            if d_name in my_dict:
                my_dict[d_name].append(d_def)
            else:
                my_dict[d_name] = [d_def]

dictFile.close()

while keep_going:

    print("Get word definition (1 to quit)")
    in_word = input().capitalize()
    if in_word == '1':
        keep_going = False
    elif in_word in my_dict:
        definitions = my_dict[in_word]
        def_length = len(definitions)
        for definition in definitions:
            print(definition)

