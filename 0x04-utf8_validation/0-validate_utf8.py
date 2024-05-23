#!/usr/bin/python3
""" Count the number """


def validUTF8(data):
    """Count the number"""

    def get_char_length(byte):
        """ get length """

        mask = 1 << 7
        length = 0

        while byte & mask:
            length += 1
            mask >>= 1
        return length

    def check_following_bytes(index, length):
        """ Check if the following bytes """

        for i in range(index + 1, index + length):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    index = 0
    while index < len(data):
        char_length = get_char_length(data[index])

        if char_length == 0:
            index += 1
            continue
        elif char_length == 1 or char_length > 4:
            return False
        elif not check_following_bytes(index, char_length - 1):
            return False

        index += char_length

    return True
