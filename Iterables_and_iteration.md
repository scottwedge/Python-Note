# iterables and iteration
## multi-input comprehensions
what is the comprehensions?
short-hand syntax for creating collections and iterablem and comprehensions can use multiple input sequences and multiple if-clauses, for instance:
```python
x = [(x,y) for x in range(5) for y in range(3)]
>>> [(x,y) for x in range(5) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)]
```

