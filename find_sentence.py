def disemvowel(string_):
    
    # setting a, e, i, o, u
    ristrict = ['a', 'e', 'i', 'o', 'u']
    list = ""
    get_signal = 0
    # get string in separately (in lowercase)
    # find aeiou on string_
    for word in string_:
        for k in ristrict:
            if word.lower() == k:                
                get_signal = 1
                break
            else:
                get_signal = 0
                
        print(get_signal)
        if get_signal == 0:
            list += word
   
    print(list)
    
    return list

def basic_tests():
    disemvowel("This website is for losers LOL!")
    print("Expected Result: ")
    print("Ths wbst s fr lsrs LL!")

basic_tests()