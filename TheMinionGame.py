def minion_game(string):
    # your code goes here
    consonants_letters = ['A', 'E', 'O', 'U', 'I']
    vowels_count = 0
    consonants_count = 0
    for i in range(len(string)):
        if string[i] not in consonants_letters:
            vowels_count += (len(string)-i)
        else:
            consonants_count += (len(string)-i)
    if vowels_count > consonants_count:
        print('Stuart {}').format(vowels_count)
    elif vowels_count < consonants_count:
        print('Kevin {}').format(consonants_count)
    else:
        print('Draw')
