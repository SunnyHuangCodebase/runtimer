"""Runtimer decorators calculate a function's execution time.

Typical Usage Example:
  from runtimer import min_runtime

  @min_runtime(100, 10)
  def function():
    ...
    # Your code here

  *Runtimer will perform m = 10 tests and return the fastest runtime.
  *Each test executes function n = 100 times.


"""
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from typing import Any, Callable


def runtime(n: int):
  """Calculate the total runtime of exeucting a function n times."""

  def decorator(function: Callable[..., Any]):

    def wrapper(*args: Any, **kwargs: Any):

      start = time.perf_counter()
      for _ in range(n):
        function(*args, **kwargs)
      end = time.perf_counter()
      print(end - start)

    return wrapper

  return decorator


def average_runtime(n: int):
  """Calculate the average runtime of executing a function n times."""

  def decorator(function: Callable[..., Any]):

    def wrapper(*args: Any, **kwargs: Any):
      start = time.perf_counter()
      for _ in range(n):
        function(*args, **kwargs)
      end = time.perf_counter()
      print((end - start) / n)

    return wrapper

  return decorator


def min_runtime(n: int, m: int = 1):
  """Out of m number of tests, return the best runtime of executing a function n times."""

  def decorator(function: Callable[..., Any]):

    def wrapper(*args: Any, **kwargs: Any):
      min_time = float('inf')
      for _ in range(m):
        start = time.perf_counter()
        for _ in range(n):
          function(*args, **kwargs)
        end = time.perf_counter()
        min_time = min(end - start, min_time)

      print(min_time)

    return wrapper

  return decorator


def max_runtime(n: int, m: int = 1):
  """Out of m number of tests, return the worst runtime of executing a function n times."""

  def decorator(function: Callable[..., Any]):

    def wrapper(*args: Any, **kwargs: Any):
      max_time = float('-inf')
      for _ in range(m):
        start = time.perf_counter()
        for _ in range(n):
          function(*args, **kwargs)
        end = time.perf_counter()
        max_time = max(end - start, max_time)

      print(max_time)

    return wrapper

  return decorator
