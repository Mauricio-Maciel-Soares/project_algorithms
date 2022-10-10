def study_schedule(permanence_period, target_time):
    array_range = []
    repeat_numbers = []

    for index in permanence_period:
        array_range.append(list(index))

    for index in array_range:
        for i in index:
            if type(i) != int:
                return None

        numbers = range(index[0], index[1] + 1, 1)

        for num in numbers:
            if target_time is None:
                return None
            if target_time == num:
                repeat_numbers.append(num)
                count = repeat_numbers.count(target_time)

    return count
