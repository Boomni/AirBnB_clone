#!/usr/bin/env python3
"""
Module __init__.py that creates a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
