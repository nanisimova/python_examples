#!/usr/bin/env python
import os
import sys

import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

from catalog.models import Catalog

def main():
    Catalog.objects.filter(is_active=0).delete()

if __name__ == '__main__':
    main()
