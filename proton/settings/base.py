"""
Proton manages a number of base settings, which will be set here, and auto-magically incorporated into your project. 
"""

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

SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
SASS_OUTPUT_STYLE = 'compact'
SASS_PRECISION = 8