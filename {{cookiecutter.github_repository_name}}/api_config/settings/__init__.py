"""API configurations."""
from .django import * # All django related settings
from .environment import *
from .project import * # All custom {{cookiecutter.github_repository_name}} related settings
from .third_party import * # DRF, Celery & other 3rd Party Apps settings
