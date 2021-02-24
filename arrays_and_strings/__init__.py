def question_1_3(input_string, input_string_len):
    output_string = []
    for i in range(input_string_len):
        if input_string[i] == ' ':
            output_string.append("%20")
        else:
            output_string.append(input_string[i])

    print(''.join(output_string))
