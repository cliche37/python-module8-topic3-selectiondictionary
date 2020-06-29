def switch_average(keyinput):

    switch_dict = {
        'A': "first",
        'a': "first",
        'B': "second",
        'b': "second",
        'C': "third",
        'c': "third",
        'D': "fourth",
        'd': "fourth"
    }

    return switch_dict.get(keyinput, "Key input not found")
