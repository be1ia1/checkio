def backward_string_by_word(text: str) -> str:
    # your code here
    words = [word for word in text.split()]
    bwords = [word[::-1] for word in words]
    answer = ''
    for i, word in enumerate(words):
         = text.replace(word, bwords[i])
        print('text now: ' + text)
    # return text

print(backward_string_by_word("olleH Hello"))




# if __name__ == '__main__':
    # print("Example:")
    # print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert backward_string_by_word('') == ''
    # assert backward_string_by_word('world') == 'dlrow'
    # assert backward_string_by_word('hello world') == 'olleh dlrow'
    # assert backward_string_by_word('"olleH Hello"') == 'Hello olleH'
#     assert backward_string_by_word('hello   world') == 'olleh   dlrow'
#     assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
#     print("Coding complete? Click 'Check' to earn cool rewards!")