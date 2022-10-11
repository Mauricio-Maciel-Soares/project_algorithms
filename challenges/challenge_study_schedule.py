def study_schedule(permanence_period, target_time):
    array_range = []
    count = 0

    for index in permanence_period:
        array_range.append(list(index))

    for index in array_range:
        for i in index:
            if type(i) != int:
                return None

    if target_time is None:
        return None

    for num in array_range:
        if num[0] <= target_time <= num[1]:
            count += 1

    return count
