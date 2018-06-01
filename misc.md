## Module
Modules refer to a file containing Python statements and definitions i.e. `math.py`    

See: 
* [Module details](https://www.programiz.com/python-programming/modules)
* [Python standard modules](https://docs.python.org/3/py-modindex.html)

#### Python import statement
```
import math
print(math.pi)

import math as m
print(m.pi)  # math.pi is invalid

from math import pi
print(pi)

from math import *  # not good practice
# everything from math module is available
print(pi)
```

## Package
* Python has packages for directories for modules
* A directory must contain a file named __init__.py in order for Python to consider it as a package
* Package can have sub-packages and modules
```
import package.module
package.module.function()

from package import module
module.function()

from package.module import function
function()
```
See: [Package details](https://www.programiz.com/python-programming/package)

## Help
python interactive interpreter
```
help
help(function)
```

## Style guide
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) has the following convention:
```
module_name
package_name
ClassName
method_name
ExceptionName
function_name
GLOBAL_CONSTANT_NAME
global_var_name
instance_var_name
function_parameter_name
local_var_name
```
A similar naming scheme should be applied to a `CLASS_CONSTANT_NAME`    

[Python PEP 8](http://www.python.org/dev/peps/pep-0008/)
> Function names should be lowercase, with words separated by underscores as necessary to improve readability.
> mixedCase is allowed only in contexts where that's already the prevailing style
