#!/usr/bin/python3
"""Module that defines multiple_returns"""


def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character.
    If the sentence is empty, the first character is None"""
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return (length, first)
