# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter


def Huffman(string):

    class Node:
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self):
            return f'Node[{self.value:^5}]'

    def get_tree(string):
        string_count = Counter(string)
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

            string_count = {node: 1}

        while len(string_count) != 1:
            node = Node(None)

            string_sorted = string_count.most_common()

            left_key = string_sorted[-1][0]
            right_key = string_sorted[-2][0]

            left_freq = string_sorted[-1][1]
            right_freq = string_sorted[-2][1]

            if isinstance(left_key, str):
                node.left = Node(left_key)
            else:
                node.left = left_key

            if isinstance(right_key, str):
                node.right = Node(right_key)
            else:
                node.right = right_key

            del string_count[left_key]
            del string_count[right_key]

            string_count[node] = left_freq + right_freq
        return [key for key in string_count][0]

    def get_code(tree, codes={}, code=''):
        if tree is None:
            return 0

        if isinstance(tree.value, str):
            codes[tree.value] = code
            return codes

        get_code(tree.left, codes, code + '0')
        get_code(tree.right, codes, code + '1')
        return codes

    def encode(string, codes):
        encoded_str = ''
        for i in string:
            encoded_str += codes[i]
        return encoded_str

    tree = get_tree(string)
    codes = get_code(tree)
    encoded_str = encode(string, codes)

    return codes, encoded_str


string = input('Введите строку:\n')
(codes, encoded_str) = Huffman(string)
print(f'Ключи:\n{codes}')
print(f'Закодированная строка:\n{encoded_str}')
