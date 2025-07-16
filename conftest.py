import sys
import os

# Добавляем путь к директории src в sys.path (аналог pythonpath)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))