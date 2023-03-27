from .func_register import *
from .gitcomment import *
from .log import *
from .multiprocess_utils import *
from .vim_utils import *

@vim_register(name="Test", command="Hello"):
    print("Hello world")


