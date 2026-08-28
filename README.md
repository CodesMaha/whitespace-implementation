This is an implementation of the esoteric programming language [Whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language)).

For convenience, this implementation accepts these optional aliases:
* `\32` as a space;
* `\t` as a tab;
* `\n` as a newline.

However, literal whitespace characters are also accepted directly.

# Usage for `main.py`
To finish one set of instructions, `-1` can be appended on a separate line as a sentinel value. Conversely, the program itself can be terminated by the Whitespace instruction `\n\n\n`.

## Example

For example, with aliases…
```
$ \32\32\32\t\32\n
-1
pushed 2
$ \n\n\n
-1
```
and without aliases…
```
$    	 

-1
pushed 2
$



-1
```

# Usage for `read.py`
Run the `read.py` file with the filepath to the source code.
```py
cd REPO_DIR
python read.py FILEPATH
```

# Features
* Stack manipulation.
* Arithmetic.
* Printing numbers and characters.

---

Python 3.13.1.