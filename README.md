This is an implementation of the esoteric programming language [Whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language)).

# Usage
Only one instruction is interpreted at a time. 

To finish one instruction, `-1` can be appended on a separate line as a sentinel value. Conversely, the program itself can be terminated by the Whitespace instruction `\n\n\n`.

---

For convenience, this implementation accepts these optional aliases:
* `\32` as a space;
* `\t` as a tab;
* `\n` as a newline.

However, literal whitespace characters are also accepted directly.

## Example

For example, with aliases,
```
$ \32\32\32\t\32\n
-1
pushed 2
$ \n\n\n
-1
```
and without aliases,
```
$    	 

-1
pushed 2
$



-1
```

# Features
Only basic arithmetic is supported so far.

---

Python 3.13.1.