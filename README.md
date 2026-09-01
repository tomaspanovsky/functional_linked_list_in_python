This project demonstrates a simple functional linked list implementation in Python.
The project includes basic list operations such as construction, traversal, mapping, filtering, reducing, and membership checking — all implemented in a purely functional style.

cons(val, lst) – construct a new list node
first(lst) – get the first element
rest(lst) – get the remainder of the list
second(lst), third(lst) – convenience accessors
is_empty(lst) – check if the list is empty
length(lst) – compute list length recursively
is_member(val, lst) – check if a value is in the list
list_map(fun, lst) – apply a function to each element
list_filter(predicate, lst) – filter elements by predicate
list_reduce(function, init, lst) – reduce the list to a single value
comp(f, g) – function composition
second2 – example of composition (first(rest(x)))
