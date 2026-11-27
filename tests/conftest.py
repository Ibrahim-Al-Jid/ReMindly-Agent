"""Test configuration.

The app validates its settings at import time, so a dummy key is set before
any test module imports it. Tests never call a real model.
"""

import os

os.environ.setdefault("MODEL_API_KEY", "test-key-not-real")
