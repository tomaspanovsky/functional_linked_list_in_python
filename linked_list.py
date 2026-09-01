# Functional linked list implemented using Python lists.
# Each node is represented as [value, rest_of_list].
# The empty list is represented as an empty Python list.

empty = []

def cons(val, lst):
    """Construct a new list node with head 'val' and tail 'lst'."""
    return [val, lst]

def first(lst):
    """Return the first element (head) of the list."""
    return lst[0]

def rest(lst):
    """Return the rest (tail) of the list."""
    return lst[1]

def second(lst):
    """Return the second element of the list."""
    return first(rest(lst))

def third(lst):
    """Return the third element of the list."""
    return first(rest(rest(lst)))

def is_empty(lst):
    """Check if the list is empty."""
    return lst == empty

def comp(f, g):
    """Function composition: comp(f, g)(x) = f(g(x))."""
    return lambda x: f(g(x))

# Example: second element using composition
second2 = comp(first, rest)

def length(lst):
    """Compute the length of the list recursively."""
    return 0 if is_empty(lst) else 1 + length(rest(lst))

def is_member(val, lst):
    """Check if 'val' is present in the list."""
    return (not is_empty(lst)
            and (first(lst) == val or is_member(val, rest(lst))))

def list_map(fun, lst):
    """Apply function 'fun' to each element of the list."""
    return (empty if is_empty(lst)
            else cons(fun(first(lst)),
                      list_map(fun, rest(lst))))

def list_filter(predicate, lst):
    """Return a list containing only elements satisfying 'predicate'."""
    return (empty
            if is_empty(lst)
            else (cons(first(lst),
                       list_filter(predicate, rest(lst)))
                  if predicate(first(lst))
                  else list_filter(predicate, rest(lst))))

def list_reduce(function, init, lst):
    """Reduce the list using a binary function and initial value."""
    return (init
            if is_empty(lst)
            else function(first(lst),
                          list_reduce(function, init, rest(lst))))

lst = cons(1, cons(2, cons(3, empty)))

print("List:", lst)
print("First:", first(lst))
print("Second:", second(lst))
print("Third:", third(lst))

print("Length:", length(lst))
print("Is member 2:", is_member(2, lst))
print("Is member 5:", is_member(5, lst))

# Map: multiply each element by 10
mapped = list_map(lambda x: x * 10, lst)
print("Mapped (*10):", mapped)

# Filter: keep only even numbers
filtered = list_filter(lambda x: x % 2 == 0, lst)
print("Filtered (even):", filtered)

# Reduce: sum of elements
summed = list_reduce(lambda x, y: x + y, 0, lst)
print("Reduced (sum):", summed)

# Using composed function second2
print("Second composition:", second2(lst))