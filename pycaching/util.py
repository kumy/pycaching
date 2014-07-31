#!/usr/bin/env python3


class Util(object):

    _rot13codeTable = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")

    @staticmethod
    def rot13(text):
        """Returns a text encoded by rot13 cipher."""
        return str.translate(text, Util._rot13codeTable)

    @staticmethod
    def to_decimal(deg, min):
        """Returns a decimal interpretation of coordinate in MinDec format."""
        return round(deg + min / 60, 5)

    @staticmethod
    def to_mindec(decimal):
        """Returns a DecMin interpretation of coordinate in decimal format."""
        return int(decimal), round(60 * (decimal - int(decimal)), 3)