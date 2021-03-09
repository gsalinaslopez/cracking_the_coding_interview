def question_1_1(input_string):
    # hashmap = {}
    #
    # for character in input:
    #     if character not in hashmap:
    #         hashmap[character] = True
    #     else:
    #         return False
    #
    # return True

    for i in range(len(input_string)):
        char_to_check = input_string[i]
        for j in range(i + 1, len(input_string)):
            if input_string[j] == char_to_check:
                return False

    return True


def question_1_2(string1, string2):
    if len(string1) != len(string2):
        return False

    string1_charcount_dict = {}
    string2_charcount_dict = {}

    for c in string1:
        if c not in string1_charcount_dict:
            string1_charcount_dict[c] = 1
        else:
            string1_charcount_dict[c] = string1_charcount_dict[c] + 1

    for c in string2:
        if c not in string2_charcount_dict:
            string2_charcount_dict[c] = 1
        else:
            string2_charcount_dict[c] = string2_charcount_dict[c] + 1

    for key in string1_charcount_dict.keys():
        if key not in string2_charcount_dict:
            return False
        elif string1_charcount_dict[key] != string2_charcount_dict[key]:
            return False

    return True


def question_1_3(input_string, string_len):
    input_string_array = list(input_string)
    j = len(input_string_array) - 1

    for i in reversed(range(string_len)):
        print(i)
        print(j)
        if input_string_array[i] == ' ':
            input_string_array[j] = '0'
            input_string_array[j - 1] = '2'
            input_string_array[j - 2] = '%'
            j = j - 3
        else:
            input_string_array[j] = input_string_array[i]
            j = j - 1
        # print(input_string_array)
        # input()

    print(''.join(input_string_array))


    # print(list(reversed(range(string_len))))
