try:
  
    input_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]


    list_vow = []
    list_cons = []
    list_sym = []

  
    def is_vowel(char):
        return char in 'aeiouAEIOU'

    
    for char, count in input_list:
        if char.isalpha():
            if is_vowel(char):
                list_vow.append((char, count))
            else:
                list_cons.append((char, count))
        else:
            list_sym.append((char, count))

  
    print("list_vow =", list_vow)
    print("list_cons =", list_cons)
    print("list_sym =", list_sym)

except Exception as e:
    
    print("An error occurred:", e)
