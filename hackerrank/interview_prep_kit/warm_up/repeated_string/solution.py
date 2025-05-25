def repeatedString(s, n):
    # possibly a could be a constant
    number_of_a_in_s = len([ch for ch in s if ch == 'a'])

    total_number_of_as = number_of_a_in_s * (n // len(s))

    # count for substring
    sub_s = s[:n % len(s)]

    total_number_of_as += len([ch for ch in sub_s if ch == 'a'])

    return total_number_of_as 
