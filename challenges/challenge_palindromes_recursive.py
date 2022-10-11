def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if word[low_index] == word[high_index] and low_index <= high_index:
        if len(word) == 1:
            return True
        if low_index + 1 == high_index - 1 or low_index + 1 == high_index:
            return True
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
