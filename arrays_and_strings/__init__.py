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

def question_1_4(input_string):
    char_occur_count = {}
    for c in input_string:
        if c == ' ':
            continue
        if c not in char_occur_count:
            char_occur_count[c] = 1
        else:
            char_occur_count[c] = char_occur_count[c] + 1

    has_pivot = False
    for c in char_occur_count.values():
        if c % 2 != 0 and (not has_pivot):
            has_pivot = True
        elif c % 2 != 0 and has_pivot:
            return False
    return True

def question_1_6(input_string):
    prev_seen_char = ''
    return_string = []
    current_char_count = 0

    first_run = True
    for c in input_string:
        if prev_seen_char == c:
            current_char_count = current_char_count + 1
        else:
            if first_run:
                current_char_count = 1
                first_run = False
            else:
                return_string.append(str(prev_seen_char) + str(current_char_count))
                current_char_count = 1

        prev_seen_char = c

    return_string.append(str(prev_seen_char) + str(current_char_count))

    return_str = str(''.join(return_string))
    return return_str if len(input_string) > len(return_str) else input_string

