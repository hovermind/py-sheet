## Running a module with command line arguments
```python
if __name__ == '__main__':
    arguments_count = len(sys.argv)
    # script name: sys.argv[0]
    # config file name: sys.argv[1]
    if arguments_count >= 2 and sys.argv[1].strip():
        # get first argument
        configuration_file = sys.argv[1]
        foo: Foo = Foo(configuration_file)
        foo.start()
```
