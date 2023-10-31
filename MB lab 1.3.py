try:
    # Sample Input
    input_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

    # Initialize empty lists for vowels, consonants, and symbols
    list_vow = []
    list_cons = []
    list_sym = []

    # Define a function to check if a character is a vowel
    def is_vowel(char):
        return char in 'aeiouAEIOU'

    # Separate characters into respective lists
    for char, count in input_list:
        if char.isalpha():
            if is_vowel(char):
                list_vow.append((char, count))
            else:
                list_cons.append((char, count))
        else:
            list_sym.append((char, count))

    # Output the results
    print("list_vow =", list_vow)
    print("list_cons =", list_cons)
    print("list_sym =", list_sym)

except Exception as e:
    # Handle exceptions if they occur
    print("An error occurred:", e)