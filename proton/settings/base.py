"""
Proton manages a number of base settings, which will be set here, and auto-magically incorporated into your project. 
"""

import os

# Used in main settings file as 'BASE_DIR'
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROTON_INSTALLED_APPS = [
  # any installed apps Proton adds/removes
  'sass_processor'
]

PROTON_MIDDLEWARE = [
  # any middleware Proton adds/removes
]

"""
+----------------------------------------
| Sass Settings
+----------------------------------------
| This section outlines the settings for the
| django-sass-processor
|
"""

SASS_PROCESSOR_ROOT = [ os.path.join(PROJECT_PATH, 'proton/bootstrap/dist/css') ]
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
SASS_OUTPUT_STYLE = 'compact'
SASS_PRECISION = 8

SASS_PROCESSOR_INCLUDE_DIRS = [
  os.path.join(PROJECT_PATH, 'proton/bootstrap/scss'),
]

