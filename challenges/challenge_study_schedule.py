def study_schedule(permanence_period, target_time):
    count = 0

    if target_time is None:
        return None

    for index, i in permanence_period:
        if type(index) != int or type(i) != int:
            return None
        if index <= target_time <= i:
            count += 1

    return count
