def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    f_s = list(first_string.lower())
    s_s = list(second_string.lower())
    len_fs = len(f_s) - 1
    len_ss = len(s_s) - 1

    quick_sort(f_s, 0, len_fs)
    quick_sort(s_s, 0, len_ss)

    return f_s == s_s


def quick_sort(lts, start, end):
    if start < end:
        previous = partition(lts, start, end)
        quick_sort(lts, start, previous - 1)
        quick_sort(lts, previous + 1, end)


def partition(lst, start, end):
    pivot = lst[end]
    delimiter = start - 1
    for index in range(start, end):
        if lst[index] <= pivot:
            delimiter += 1
            lst[delimiter], lst[index] = lst[index], lst[delimiter]
    lst[delimiter + 1], lst[end] = lst[end], lst[delimiter + 1]

    return delimiter + 1
