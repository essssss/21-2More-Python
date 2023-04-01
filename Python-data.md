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

---

# Set Operations

Mathematical style ways to compare sets.

```python
moods = {"happy", "sad", "grumpy"}

dwarfs = { "happy", "grumpy", "doc"}


moods | dwarfs          # union: {"happy", "sad", "grumpy", "doc"}

moods & dwarfs          # intersection: {"happy", "grumpy"}

moods - dwarfs          # difference: {"sad"}
dwarfs - moods          # difference: {"doc"}

moods ^ dwarfs          # symmetric difference {"sad", "doc"}
```

---

-  Union

   ```python
   lemon = {'sour', 'yellow', 'fruit', 'bumpy'}
   banana = {'fruit', 'smooth', 'sweet', 'yellow'}

   In [4]: lemon | banana
   Out[4]: {'bumpy', 'fruit', 'smooth', 'sour', 'sweet', 'yellow'}
   ```

-  Union creates a set that contains **all** items.

   -  also use `banana.union(lemon)`

-  We can chain unions together with multiple pipes `|`

---

-  Intersection
   ```python
   In [5]: lemon & banana
   Out[5]: {'fruit', 'yellow'}
   ```
-  Intersection creates a set that only returns the values common to **both** sets

---

-  Difference

   ```python
   In [6]: lemon - banana
   Out[6]: {'bumpy', 'sour'}

   In [7]: banana - lemon
   Out[7]: {'smooth', 'sweet'}
   ```

-  Difference creates a set containing the elements of the **first** set that are not present in the **second** set.
   -  like subtracting the second set from the first.
   -  order matters

---

-  Symmetric Difference
   ```python
   In [8]: banana ^ lemon
   Out[8]: {'bumpy', 'smooth', 'sour', 'sweet'}
   ```
-  Symmetric Difference creates a new set that contains only elements that are in **exactly one** of the sets.

---

## **The shortcut operators only work on sets**

BUT the keywords (`set.union(set2)`) will work on any iterable for `set2`, by turning the iterable into a set.

---

```python
In [11]: lemon & orange
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[11], line 1
----> 1 lemon & orange

TypeError: unsupported operand type(s) for &: 'set' and 'list'
```

---

```python
In [12]: lemon.intersection(orange)
Out[12]: {'bumpy', 'fruit'}
```

---

```python
In [13]: orange.intersection(lemon)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[13], line 1
----> 1 orange.intersection(lemon)

AttributeError: 'list' object has no attribute 'intersection'
```

---

# sets are iterable

```python
for adj in banana:
   print(adj)

# sweet
# yellow
# fruit
# smooth
```

---

we can also add our new operations to that iterability <small>(cool word)</small>

```python
for adj in banana | lemon | set(orange):
   print(adj)

# fruit
# sweet
# sour
# orange
# yellow
# smooth
# bumpy
```

---

## There is a demonstration of how sets are **_super_** duper fast.

---

# <center> **_TUPLES_**</center>

### Tuples:

immutable, ordered sequence

-  Like lists, but _immutable_

-  created with parentheses.
-  cannot do things like "append" or change items
-  can access data with an index `tuple[0]`

```python
t1 = (1, 2, 3)
t2 = ()           # empty tuple
t3 = (1,)         # one-item tuple: note trailing comma
```

-  values do not have to be unique.
-  can turn an iterable into a tuple with `tuple(list)`

---

## why tuples?

-  slightly smaller and faster than lists.
-  Since they are immutable they can be used as keys for dictionaries, or put into sets.
-  when we look at `dictionary.items()` each key value pair is returned as a **tuple**

---

Not many methods with a tuple.
`count` and `index` which are self explanatory.

---

# <center> COMPREHENSIONS </center>

### List Comprehension:

-  Python has `filter()` and `map()` like JS
-  but _comprehensions_ are even more flexible

---

Finding the evens without `comprehension`

```python
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

evens = []
for num in nums:
   if num % 2 == 0:
      evens.append(num)

print(evens)
# [2, 4, 6, 8, 10, 12]
```

---

OR in python we can do this:

```python
evens = [num for num in nums if num % 2 == 0]
```

---

```python
 [num * 2 for num in nums]
#|       |               |
#|       |---This part---| is the looping part.
#|       |
#|-This--| part is what we add to the new list.
#|       |               |
 ['HIIII' for num in nums]
```

-  We use the brackets to make the output a list

---

```python
# [2,4,6,8] square it
[n * n for n in [2,4,6,8]]
```

---

## Mapping into a list

```python
[x for x in range(3)]
#[0, 1, 2]

[[] for x in range(3)]
#[[], [], []]

[[0 for y in range(3)] for x in range(3)]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

-  look! we made a tic tac toe board!

---

## Here is a function to create a square gameboard with varying sizes

```python
def gen_board(size, initial_val=None):
   return[[initial_val for x in range(size)] for y in range(size)]
```

```python
In [3]: gen_board(5, 0)
Out[3]:
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
```

---

## Adding in conditional logic

```python
doubled_evens = [n * 2 for n in nums if n % 2 == 0]
```

OR

```python
chickens = [
   {"name": 'Henry', "sex": 'Rooster'},
   {"name": 'Lady Gray', "sex": 'Hen'},
   {"name": 'Junior', "sex": 'Rooster'},
   {"name": 'Stevie Chicks', "sex": 'Hen'},
   {"name": 'Rocket', "sex": 'Hen'},
   {"name": 'Butters', "sex": 'Rooster'},
]
hens = [bird["name"] for bird in chickens if bird["sex"]== "Hen"]

# hens = ['Lady Gray', 'Stevie Chicks', 'Rocket']
```

For if/else style conditionals:

```python
[do_this if something else do_that for thing in things]
```

---

Hey look at this morse code!

```python
# Functions inside a comprehension:

def get_letter(ltr):
    morse_lookup = {'A':'.-', 'B':'-...', 'Z':'-.--.-'}
    return morse_lookup.get(ltr.upper(), '')

msg = [get_letter(char) for char in 'SOS']

def get_morse_code(string):
    return " ".join([get_letter(char) for char in string])
```

---

# Dictionary Comprehension:

same as list but use curly braces

```python
{day : 0 for day in 'MTWRFSU'}

# {'M': 0, 'T': 0, 'W': 0, 'R': 0, 'F': 0, 'S': 0, 'U': 0}
```

A dictionary with a number as a key and its square as a value:
`{1:1, 2:4, 3:9, 4:16, ...etc}`

```python
{num: num * num for num in range(1,10)}
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

Or only squares of even numbers:

```python
{num: num * num for num in range(1,10) if num % 2 == 0}
```

---

## Also do set comprehensions

```python
{char for char in "abracadabra"}
# {'a', 'b', 'c', 'd', 'r'}
```
