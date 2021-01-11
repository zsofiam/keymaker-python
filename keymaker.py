import string


def shift_characters(word, shift):
    char_list = list(word)
    abc = string.ascii_lowercase
    abc_list = list(abc)
    for index, letter in enumerate(word):
        new_index = abc_list.index(letter) + shift
        if new_index >= len(abc_list) or new_index <= -1 * len(abc_list):
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
    abc = string.ascii_lowercase
    abc_list = list(abc)
    for index, letter in enumerate(word):
        new_index = len(abc_list) - 1 - abc_list.index(letter)
        if new_index >= len(abc_list) or new_index <= -1 * len(abc_list):
            new_index %= len(abc_list)
        char_list[index] = abc_list[new_index]
    return "".join(char_list)


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    pass


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


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
    #name = input("Enter your name! ").lower()
    #print(f'Your key: {hash_it(name)}')
    print(shift_characters("azcmx", 200))
    print(pad_up_to('abb', 5, 11))
    print(pad_up_to('aaa', 2, 100))
    print(abc_mirror('abcd'))
    print(abc_mirror('morpheus'))
    print(abc_mirror('azbn'))
