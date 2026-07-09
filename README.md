This is an implementation of the esoteric programming language [Whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language)).

# Usage
Only one instruction is interpreted at a time.
To finish one instruction, `-1` can be appended on a separate line as a sentinel value.
Conversely, the program can be terminated by the Whitespace instruction `\n\n\n`.

For example:
```
$ \32\32\32\t\32\n
-1
pushed 2
$ \n\n\n
-1
```

For convenience, this implementation accepts the following:
* `\32` is a space;
* `\t` is a tab;
* `\n` is a newline.
However, literal whitespace characters are also accepted directly.

# Features

Only basic arithmetic is supported so far.

---

Python 3.13.1.