def is_anagram(first_string, second_string):

    f_s = list(first_string.lower())
    s_s = list(second_string.lower())

    def ordena(lts):
        length_lst = len(lts)
        if length_lst > 0:
            quick_sort(lts, 0, length_lst - 1)
        else:
            return False

    def quick_sort(lts, start, end):
        if start > end:
            return
        previous = start
        posterior = end
        pivot = lts[start]

        while previous < posterior:
            while previous < posterior and lts[posterior] > pivot:
                posterior = posterior - 1

            if previous < posterior:
                lts[previous] = lts[posterior]
                previous = previous + 1

            while previous < posterior and lts[previous] <= pivot:
                previous = previous + 1

            if previous < posterior:
                lts[posterior] = lts[previous]
                posterior = posterior - 1

            lts[previous] = pivot

        quick_sort(lts, start, previous - 1)
        quick_sort(lts, previous + 1, end)

    ordena(f_s)
    ordena(s_s)

    return f_s == s_s
