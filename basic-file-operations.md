* 
* Courtesy:
  * https://wellsr.com/python/basics/python-io-input-output-examples/

## Open
```python
fooFile = open(path, mode, ...) # fooFile is object

# work with file

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

## Readability check
```python
fooFile = "C:\\path\\to\\FooFile.txt"
if os.access(fooFile, mode=os.R_OK):  # mode=os.R_OK specifically checks readability
  # open file and process
```

## Reading content
**`read()`:** reads whole file content at once
```python
fooFile = open("foo.txt", mode="r")
fileContent = fooFile.read()

# Be sure to close the file
fooFile.close()

print(fileContent)
```

**Line-by-line:** file object iterator calls `readline()`
```python
fooFile = open("foo.txt", mode="r")
fileContent = ""
for line in fooFile: # iterator will call fooFile.readline()
  # can perform operations on each line
  fileContent += line
 
# Be sure to close the file 
fooFile.close()

print(all)
```

## Write
```python
fooFile = open("foo.txt", mode="a")
contentToWrite: str = "foo bar baz"
fooFile.write(contentToWrite) # appending since opened with mode="a"

fooFile.close()
```

## With Statement
* similar to C# using or java try-with-resources or swift deferred execution
* with context manager - sub-environment” under which the code is executed
* The with statement allows a special instantiation of an object, where:
  * `__enter__` method is executed when the object is instantiated
  * `__exit__` method is executed when the with statement is exited
  * these methods are executed whether an exception is raised or not
  * The open object has a close method contained within its `__exit__` method (therefore if any exception is raised, Python will cleanly close the file and exit)

A with statement has the format:
```text
with [object] as [variable]:
	[execution]
```
