#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    settings_local_path = 'pyist/settings_local.py'
    settings_name = 'pyist.settings'
    if os.path.exists(settings_local_path):
        settings = settings_name + '_local'
    else:
        settings = settings_name
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
