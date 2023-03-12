#!/usr/bin/env python3
"""
Module that creates a unique FileStorage instance for the application
"""
import models.engine.file_storage
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
