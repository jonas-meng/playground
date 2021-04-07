#!/usr/bin/env python

import collections
import bisect
from random import choice
from array import array
from collections import deque

# classes of objects without custom methods, like database records
# a namedtuple contains a class name and a list of field names
Card = collections.namedtuple('Card', ['rank', 'suit'])
# _fields list field names
# print(Card._fields)
card = ('2', 'diamonds')
# print(card)
# convert iterable to namedtuple
card = Card._make(card)
# print(card)
# convert namedtuple to ordered dict
# print(card._asdict())

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# implicitly inherit from object
class FrenchDeck(object):
    """
    two special methods __len__ and __getitem__ enable FrenchDeck to behave like a standard Python sequence,
    benefiting from core language features (e.g. iteration and slicing)

    special methods are meant to be called by Python interpreter
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def deck_test():
    deck = FrenchDeck()
    print(choice(deck))

    print(deck[:3])

    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)

    # if a collection has no __contains__ method, in operator does a sequential scan
    if Card('Q', 'hearts') in deck:
        print('yes')

    for card in sorted(deck, key=spades_high):
        print(card)


# immutable sequences: tuple, str, and bytes
# mutable sequences: list, bytearray, array.array, collections.deque, and memoryview

def function_with_multiple_return(a, b, c):
    return a, b, c


def sequence_test():
    symbols = '$%^&*'
    # list comprehension
    codes = [ord(symbol) for symbol in symbols]
    print(codes)

    # listcomps is the shorthand for list comprehension
    # in Python 3, list, set and dict comprehensions and generator expressions have own local scope like function
    # variables assigned in expression are local variables, but variables in outside scope can still be referenced
    # variable shadowing will not happen, see example below
    # x variable in _for_ expression is a local variable
    # the last x variable reference to x in the outside scope
    # compared with the use of _map_ and _filter_ function, list comprehension has more readability
    x = 'ABC'
    dummy = [ord(x) for x in x]
    print(x)
    print(dummy)

    colors = ['black', 'white']
    sizes = 'SML'
    # nested for loop is possible in list comprehension
    # tuples as field-less records
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)
    # tuple unpacking
    for color, size in tshirts:
        print(color, size)

    # tuple unpacking: parallel assignment
    coordinates = (1, 2)
    latitude, longitude = coordinates
    print(latitude, longitude)

    # tuple unpacking: value swapping
    latitude, longitude = longitude, latitude

    data = (1, 2, 3)
    # tuple unpacking: prefixing star on argument
    # tuple unpacking: return multiple values
    # _ underscore can be used as placeholder for undesired values
    a, b, _ = function_with_multiple_return(*data)
    # use *args to capture arbitrary excess arguments
    a, *rest = function_with_multiple_return(*data)
    print(rest)
    # * prefix can only be used on one variable, but it can appear in any position
    *rest, a = function_with_multiple_return(*data)
    print(rest)

    # nested tuple unpacking is allowed if the expression matches the nesting structure
    nested_tuple = (1, 2, (3, 4))
    a, b, (c, d) = nested_tuple
    print(a, b, c, d)

    # genexp is the shorthand for generator expression
    # generator expression saves memory by using iterator protocol, instead of building a whole list
    # if generator expression is the single argument in a function call, then there is no need to duplicate the enclosing parentheses
    tuple_code = tuple(ord(symbol) for symbol in symbols)
    print(tuple_code)


def slicing_test():
    s = 'bicycle'
    # s[::3] is converted to a slice object s.__getitem__(slice(0, len(s), 3))
    print(s[::3])
    print(s[::-1])
    print((s[::-2]))
    s1 = ['a'] * 6
    # slice can be on the right side, but the size of sequences on the both sides of assignment must be equal
    # both + and * create new sequence instead of changing operands
    # * n would produces n copies of the original sequence items, might result in n copies referencing to same items
    s1[::2] = ['b'] * 3
    print(s1)
    # to create a list of lists, the recommended way is list comprehension
    board = [[''] * 3 for i in range(3)]
    board = []
    for i in range(3):
        board.append(['_'] * 3)

    # below the wrong example is equivalent to the extended for loop code
    # same content (_row_) is appended three times
    wrong_example = [['_'] * 3] * 3
    row = ['_'] * 3
    board = []
    for i in range(3):
        board.append(row)

    a = 1
    b = 2
    # if the special method __iadd__ is not implemented on the object, then it will fall back to __add__
    a += b
    a = a + b
    # repeated concatenation of immutable sequences causes performance-inefficiency
    # putting mutable item in tuple is not advisable
    t = (1, [2, 3])
    # list.sort is a in place sorting, whereas built-in _sorted_ always returns a new sequence
    # two optional, keyword-only arguments: reverse (boolean) and key (one-argument function)
    unordered_haystack = reversed([1, 2, 3, 4, 5, 6])
    haystack = []
    for val in unordered_haystack:
        # bisec.insort is an alias for bisect.insort_right
        # similarly, there is a bisect.insort_left
        bisect.insort(haystack, val)
    needles = [3, 5, 10]
    print(haystack)
    for needle in needles:
        # bisect.bisect is an alias for bisect.bisect_right
        # sister function bisect.bisect_left, the difference is when comparing equal, which side the returned position will locate
        pos = bisect.bisect(haystack, needle)
        print(f'position is {pos}, value is {needle}')
    # array.array is more efficient with regards to memory and access than a list when only contain a huge amount of numbers
    # array.tofile and array.fromfile reads faster from binary files than text file
    floats = array('d', [2.5, 3.5, 4.5, 5.5])
    print(floats[0])

    # deque can be bounded by providing the parameter maxlen, then when the list is full,
    # elements will be discarded from the opposite end when inserting new ones
    # deque is a thread-safe double-ended queue designed for fast inserting and removing from both ends
    # similar data structures worthy of exploration: Queue, LifoQueue and PriorityQueue from package queue, asyncio, and heapq


if __name__ == '__main__':
    slicing_test()
    pass
