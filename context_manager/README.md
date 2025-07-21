# In-depth work with context managers
## 📌 Objective:
* Work out **nested and combined context managers**.
* Practise handling **exceptions** inside __exit__.
* Learn how to create a **middleware-style context manager**.
* Repeat usage as a **decorator** and as a **with-block**.
---
## 🔧 Part 1: Basic Practice
### ✅ Task 1: Context manager for error suppression
Create a `suppress_errors` context manager that:
- Suppresses exceptions of specified types.
- When suppressing, prints:<br><br>
  `[!] Error of type <ErrorType> suppressed`

Use case:

```python
with suppress_errors(ZeroDivisionError, ValueError):
    1 / 0
    int("abc") # both exceptions are suppressed
```
📌  Implement via 
`@contextmanager`.
---
### ✅ Task 2: Nested resources
Create two context managers:
- `open_log_file(filename)`
- `open_data_file(filename)`

And implement them in such a way that:
- `open_log_file(filename)` opens the log file and writes `"Log opened"` to it
- `open_data_file(filename)` opens the data file and writes `"Data file opened"` to the log file

Implement **nested** usage so that everything is logged in the correct sequence.

The **goal** is to learn how to manage multiple nested resources and transfer data
between managers (for example, a `logger` in `open_data_file`).
---
## 🛠 Part 2: In-depth implementation
### ✅ Task 3: Manager "profiler"
Create a `Profiler` context manager that:
- Measures the execution time of a block
- Saves the result to the `profile.log` file in the following format:

`Block “save_users” — 0.342 sec`

Example of use:

```python
with Profiler("save_users"):
    some_heavy_function()
```

🎯 Implement via a **class**.

📌 Complication (optional): implement support for **nested profiles** with indents.
---
### ✅ Task 4: Security check context-decorator
Create a `SafeExecutor` class that inherits from `ContextDecorator`, which:
- Checks for the presence of the ALLOW_EXECUTION environment variable.
- If the variable is not set, throws an exception when entering the block/decorator.
- Supports both usage methods: with and @decorator.

Example:
```python
@SafeExecutor()
def do_sensitive_work():
    ...

with SafeExecutor():
    do_sensitive_work()
```
---
