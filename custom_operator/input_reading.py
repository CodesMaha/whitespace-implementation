""" reading from standard input (stdin) in a determined manner """

from custom_operator import is_7bit_ascii

from sys import stdin
from re import fullmatch
from typing import Any

class InputReader:
    """ text from stdin """
    def __init__(self, heap):
        self.heap = heap # store inp return
        self._text: str = ""
        self.text_len: int = len(self._text)
        self.pos: int = -1

    def _get(self) -> str:
        """ get new from stdin """
        self._text = stdin.readline()[:-1]
        self.text_len: int = len(self._text)
        self.pos: int = -1

    def read_character(self, top_stack) -> None:
        """ read one reg character, and store in heap """
        # if exhausted, get new inp
        self.pos += 1
        if (not self._text) or (self.pos == self.text_len):
            self._get()

        curr: str = self._text[self.pos] # single char
        while True:
            if is_7bit_ascii(ord(curr)):
                self.heap.store(top_stack, ord(curr))
                break
            else: # skip to next if not
                self._get()
                curr = self._text[self.pos]

    def read_number(self, top_stack: Any) -> None:
        """ read number, and store in heap """
        while True:
            self._get()
            # ignore spaces and underscores for thousands sep
            if fullmatch(r"[-_ \d]+", self._text) is None:
                continue
            self._text = self._text.replace(" ", "_")
            self.heap.store(top_stack, int(self._text))
            break
