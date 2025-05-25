def countingValleys(steps, path):
    # Write your code here

    valleys = 0
    is_valley = False
    current_level = 0

    for step in path:
        if step == "D":
            current_level -= 1
            if current_level == -1 and not is_valley:
                is_valley = True
                valleys += 1
        else:
            current_level += 1
            if current_level == 0 and is_valley:
                is_valley = False

    return valleys
