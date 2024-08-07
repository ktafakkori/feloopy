# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import os
os.environ['PYTHON_JULIACALL_AUTOLOAD_IPYTHON_EXTENSION'] = 'yes'

try:
    from .extras import *
except ImportError:
    pass


from .feloopy import *
