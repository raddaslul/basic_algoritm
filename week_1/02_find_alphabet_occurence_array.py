def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        else:
            index_array = ord(char) - ord("a")
            alphabet_occurrence_array[index_array] += 1

    print(chr(alphabet_occurrence_array.index(max(alphabet_occurrence_array)) + ord("a")))

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))