import string


def get_abc_list():
    abc = string.ascii_lowercase
    abc_list = list(abc)
    return abc_list


def shift_characters(word, shift):
    char_list = list(word)
    abc_list = get_abc_list()
    for index, letter in enumerate(word):
        new_index = abc_list.index(letter) + shift
        #if new_index >= len(abc_list) or new_index <= -1 * len(abc_list):
        new_index %= len(abc_list)
        char_list[index] = abc_list[new_index]
    return "".join(char_list)


def pad_up_to(word, shift, n):
    new_word = word
    while len(new_word) < n:
        appendix = shift_characters(word, shift)
        new_word += appendix
        word = appendix
    return new_word[:n]


def abc_mirror(word):
    char_list = list(word)
    abc_list = get_abc_list()
    for index, letter in enumerate(word):
        new_index = len(abc_list) - 1 - abc_list.index(letter)
        if new_index >= len(abc_list) or new_index <= -1 * len(abc_list):
            new_index %= len(abc_list)
        char_list[index] = abc_list[new_index]
    return "".join(char_list)


def create_matrix(word1, word2):
    abc_list = get_abc_list()
    matrix = []
    for letter in word2:
        shift = abc_list.index(letter)
        shifted_word = shift_characters(word1, shift)
        matrix.append(shifted_word)
    return matrix


def zig_zag_concatenate(matrix):
    new_word = ""
    for column in range(len(matrix[0])):
        for j in range(len(matrix)):
            if not column % 2 == 0:
                row = len(matrix) - 1 - j
            else:
                row = j
            new_word += matrix[row][column]
    return new_word


def rotate_right(word, n):
    new_list = []
    for i in range(len(word)):
        new_list.append('a')
    for i in range(len(word)):
        new_index = i + n
        new_index %= len(word)
        new_list[new_index] = word[i]
    """ for i in range(n):
        last_char = word_list[len(word_list)-1]
        word_list[1:len(word_list)] = word_list[:len(word_list)-1]
        word_list[0] = last_char """
    return "".join(new_list)


def get_square_index_chars(word):
    new_word = ""
    new_index = 0
    while new_index ** 2 < len(word):
        new_word += word[new_index**2]
        new_index += 1
    return new_word


def remove_odd_blocks(word, block_length):
    new_word = ""
    skip = True
    for index, letter in enumerate(word):
        if index % block_length == 0:
            skip = not skip
        if not skip:
            new_word += word[index]
    return new_word


def reduce_to_fixed(word, n):
    shift = -1 * n // 3
    new_word = rotate_right(word[:n], shift)
    return new_word[::-1]


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
    print(shift_characters("abby", 5))
    print(shift_characters("a", 27))
    print(shift_characters("azcmx", 2))
    print(shift_characters("azcmx", -200))
    print(pad_up_to('abb', 5, 11))
    print(pad_up_to('aaa', 2, 100))
    print(abc_mirror('abcd'))
    print(abc_mirror('morpheus'))
    print(abc_mirror('azbn'))
    print(create_matrix('mamas', 'papas'))
    print(create_matrix("az", "abz"))
    print(zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']))
    print(zig_zag_concatenate(['aaa', 'bbb', 'ccc', 'ddd']))
    print(rotate_right('abcdefgh', 1))
    print(rotate_right('abcdefgh', 3))
    print(rotate_right('abcdefgh', 8))
    print(rotate_right('abcd', 1))
    print(rotate_right('abcd', 4))
    print(rotate_right('abcd', 100))
    print(rotate_right('abcd', 5))
    print(rotate_right('abcdefgh', 3))
    print(rotate_right('abcdefgh', 11))
    print(rotate_right('abcdefgh', -5))
    print(rotate_right('abcdefgh', -13))
    print(get_square_index_chars('abcdefghijklm'))
    print(remove_odd_blocks('abcdefghijklm', 3))
    print(reduce_to_fixed('abcdefghijklm', 6))
    print(hash_it("morpheus"))
    print(hash_it("trinity"))
    print(hash_it("neo"))
