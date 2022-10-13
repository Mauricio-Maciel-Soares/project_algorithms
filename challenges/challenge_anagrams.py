def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    f_s = list(first_string.lower())
    s_s = list(second_string.lower())

    str_list = [f_s, s_s]

    for index in str_list:
        n = len(index)
        for i in range(n):
            for j in range(n - i - 1):
                if index[j] > index[j + 1]:
                    index[j], index[j + 1] = index[j + 1], index[j]

    # equality = True
    # for i in range(len(f_s)):
    #     if f_s[i] == s_s[i] and equality:
    #         i += 1
    #     else:
    #         equality = False

    return f_s == s_s
