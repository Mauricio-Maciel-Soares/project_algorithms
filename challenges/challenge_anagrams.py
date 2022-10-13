def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    f_s = list(first_string.lower())
    s_s = list(second_string.lower())

    str_list = [f_s, s_s]

    def merge_sort(string, start=0, end=None):
        if end is None:
            end = len(string)
        if (end - start) > 1:
            mid = (start + end) // 2
            merge_sort(string, start, mid)
            merge_sort(string, mid, end)
            merge(string, start, mid, end)

    def merge(string, start, mid, end):
        left = string[start:mid]
        right = string[mid:end]

        left_index, right_index = 0, 0

        for general_index in range(start, end):
            if left_index >= len(left):
                string[general_index] = right[right_index]
                right_index = right_index + 1
            elif right_index >= len(right):
                string[general_index] = left[left_index]
                left_index = left_index + 1
            elif left[left_index] < right[right_index]:
                string[general_index] = left[left_index]
                left_index = left_index + 1
            else:
                string[general_index] = right[right_index]
                right_index = right_index + 1

    for index in str_list:
        merge_sort(index, 0, len(index))

    equality = True
    for i in range(len(f_s)):
        if f_s[i] == s_s[i] and equality:
            i += 1
        else:
            equality = False

    return equality
