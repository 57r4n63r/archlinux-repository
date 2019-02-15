#!/usr/bin/env python

import os
import sys
import json
import validator
import environment

from core import config
from core import contextual

contextual = contextual.new(
   pwd = __file__
)

config = config.new(
   path_base = contextual.path_base
)

validate = validator.new(
   config = config.get,
   path_base = contextual.path_base
)

environment = environment.new(
   config = config.get,
   path_base = contextual.path_base
)
