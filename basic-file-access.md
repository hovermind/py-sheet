## open()
```python
fooFile = open(path, mode, ...) # fooFile is object

# close file when done using
fooFile.close()
```
* **path:** A string containing the pathname to the file we wish to open (pathname: relative to the system working directory)
* **mode:** The operation we intend to perform on the file. It has the following options:
  * "r": Read the file. This is the default setting.
  * "w": Write to the file. Creates the file if it doesn’t exist, and erases it if it does.
  * "a": Write to the end of a file. Creates the file if it doesn’t exist.
  * "r+": Read and write to the file. Starting position is at the start of the file.
  * "w+": Read and write to the file. Erases the file if it already exists. Starting position is at the start of the file.
  * "a+": Read and write to the file. Starting position is at the end of the file.
  * "t": Read\Write data as text. This option can be added to the above (e.g. “r+t”). This is the default option.
  * "b": Read\Write data as binary. This option can be added to the above (e.g. “r+b”).
* `...`: This refers to other less common options available within the open function call
* While the file is opened, no other program will allowed to access it (Close it: `fooFile.close()`)
