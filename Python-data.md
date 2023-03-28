# **Python Data Structure!!!**

### Python includes excellent, high performance data structures as part of the language.

---

## **Length of Structure**

### Generic `len(x)` returns length of `x`

-  \# chars in string
-  \# items in list
-  \# items in dictionary
-  \# items in set

```python
len("HELLO WORLD")
```

##### `len()` is a function we execute, not a property.

---

## **Lists**

### Like JS arrays:

-  Mutable, ordered sequence
-  `O(n)` to search, add, delete
   -  Except when at end: `O(1)`

## **Making Lists**

`alpha = ['a', 'b', 'c']`

Can use constructor function `list()`  
This will make list from iterating over argument:

```python
letters = list("apple")
#['a', 'p', 'p', 'pl', 'e']
```

## **`in`**

-  check for membership in a list with `in` keyword

## **index**

-  same `[]` notation as I'm used to
-  Python gives an error if the index is "out of range"
-  negative indeces will count backward from the end of the list. _(cool!)_
-  change an element using the index (`vegan_no_nos[2] = 'dairy'`)
-  can NOT add an item using an index (`vegan_no_nos[5]= 'butter'`)

---

A list is stored as a reference, like in JS.

---

## **SLICING**

Can retrieve list from list:

```python
lst[start:stop:step]
```

-  **start**: index to begin retrieval (_default: start_)
-  **stop**: index to end retrieval before (_default: end_)
-  **step**: number to step (_defaul: 1_)

### skip by leaving blanks...the `:` is important though.

```python
alpha = ['a', 'b', 'c', 'd', 'e']

alpha[2:]       # ['c', 'd', 'e']
alpha[2:4]      # ['c', 'd']
alpha[:3]       # ['a', 'b','c']
alpha[::2]      # ['a', 'c', 'e']
alpha[3:0:-1]   # ['d', 'c', 'b']
alpha[::-2]     # ['e', 'c', 'a']
```

-  none of this mutates the original. We can save it to a new var
-  note how start and stop points work with a negative step value

---

# **SPLICING**

Same slice notation but we can update or retrieve that information.

```python
alpha = ['a', 'b', 'c', 'd', 'e']

alpha[2:] = ['y', 'z']
print(alpha)            # ['a', 'b', 'y', 'z']

alpha[1:3] = []
print(alpha)            #['a', 'z']
```

-  splice will take a slice of a list and replace elements.
-  adding an empty list will remove those elements.

---

# **LIST METHODS**

Every list has access to these methods:

|                  |                                                       |
| ---------------- | ----------------------------------------------------- |
| `l.append(x)`    | Add `x` to end of list                                |
| `l.copy()`       | Return shallow copy of list `l`                       |
| `l.count(x)`     | Return # times `x` appears in `l`                     |
| `l.extend(l2)`   | Add items of `l2` to `l`                              |
| `l.index(x)`     | Return (0-based) index of `x` in `l`                  |
| `l.insert(i, x)` | Insert `x` at position `i`                            |
| `l.pop(i)`       | Remove and return item at index `i` (default to last) |
| `l.reverse()`    | Reverse list (change in place)                        |
| `l.sort()`       | Sort list in place                                    |

---

Nothing here is revolutionary from JS

## - random things to take into account:

-  append takes exactly one object
-  `copy_list = list` will make a duplicate reference to the original list
   -  `copy_list = list.copy()` is what we really want to do to make a true copied list

---

# <center>**STRINGS**</center>

```python
msg = "Hello!"
also = 'Oh, hi!'

long_msg = """This can continue over several
lines of text"""

greet = f"Hi, {fname} {lname}"

email = f"""Dear {user},
You owe us ${owed}. Please remit."""
```

-  Can use `in` to check for membership
-  Can use slice but cannot use splice. --can't change characters.
-  Can multiply a string with a number
-  Can iterate over, letter by letter

# <center>**STRING METHODS**</center>

-  there are more str methods than we will cover. so use the help function!

| method                | usage                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| `s.count(t)`          | Returns # times `t` occurs in string `s` (case sensitive)                                         |
| `s.endswith(t)`       | Does `s` end with string `t`? (boolean)                                                           |
| `s.startswith(t)`     | Does `s` start with string `t`? (boolean)                                                         |
| `s.find(t)`           | Finds string `t` and returns index. Only returns first index. if it is not found, it returns `-1` |
| `s.isdigit()`         | Returns whether entire string consists of digits                                                  |
| `s.join(seq)`         | Make new string of `seq` joined by `s` (`"\|".join(nums)`)                                        |
| `s.lower()`           | Make lower case                                                                                   |
| `s.replace(t, count)` | Replace `count` (default: all) occurences of `t` in `s`                                           |
| `s.split(sep)`        | Return list of items made from splitting `s` on `sep`                                             |
| `s.splitlines()`      | Split `s` at newlines                                                                             |
| `s.strip()`           | Remove whitespace at start/end of `s`                                                             |

---

# <center>**DICTIONARIES**</center>

Dictionaries are :

-  Mutable ordered mapping of keys -> values
-  `O(1)` runtime for adding, retrieving, deleting items
   -  like JS object or `Map`

## To make a new Dictionary:

```python
fruit_colors = {
    "apple": "red",
    "berry": "blue",
    "cherry": "red"
}
```

-  Values can be _any type_
-  Keys can be any **immutable type**

---

### <center>**Membership and Retrieval**</center>

-  `in` checks for membership of key (`"apple" in  fruit_colors`)

-  `[ ]` retrieves item by key (`fruit_colors['apple']`)
   -  cannot use dot notation
   -  failure to find results in an error()

---

## Dictionary methods:

-  `d.copy()` - Return a new copy of `d`

   -  this is a shallow copy

-  `d.get(x, default)` - Retrieve value of `x` (return optional `default` if missing)

-  `d.items()` - Return iterable of (key, value) pairs

-  `d.keys()` - Return iterable of keys

-  `d.values()` - Return iterable of values

   -  these iterables are **not** lists. But they can be turned into a list and saved to a variable: `list(chicken.items())`

-  There are some other valuable things : `dict.pop()`, `dict.popitem()`

   ##### (pop item is like random? why would I want that, lol)

-  `d.fromkeys('MTWHF', True)` - Set a key from an iterable, and then sets the value
-  `d.clear()` - empties a dictionary

---

# <center>**SETS**</center>

## <center> Unordered, unique collection of items, like JS **_Set_** </center>

## <center> `O(1)` runtime for adding, retrieving, deleting

</center>

---

## Making Sets:

Use `{}`, but with **`only`** keys, not `key:value`  
`colors = {'red', 'green', 'blue'}`

-  duplicate items will simply not be added. No errors.
-  We can also use the constructor function to make a set from an iterable
   ```python
   set("apple")   # {"a", "p", "p", "l", "e"}
   ```

```python
voted_languages = ['ruby', 'python', 'javascript', 'scala', 'ruby', 'python', 'python', 'python']
# a list with duplicates

set(voted_languages)
# {'javascript', 'python', 'ruby', 'scala'}
# returned SET with no duplicates and no real particular order
```

Sets are SO FAST!!!

-  they are fast because only IMMUTABLE things can go into sets _(no dictionaries or lists)_

## Set Membership

-  use `in` operator to check for membership

   -  `'ruby' in voted_languages`

-  `set.add(item)` - adds item
-  `set.pop()` - removes and returns arbitrary item
-  `set.remove(item)` - removes item from set
-  `len(set)` - returns length of set
-  `set.copy()` - makes a copy ... this time it doesn't matter that it's a shallow copy, because we won't have mutable data types
