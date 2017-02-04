# Session 1: Basics 1

Welcome to the very first session of our course, based on Udacity's MOOC [Programming Foundations with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036). Here you'll find a description of what we worked the first session.

## Conditionals

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
```



## References:
1. [More Control Flow Tools: if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
