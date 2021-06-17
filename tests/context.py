import os
import sys

# Adds "tiny_test_hatchery" to sys.path
# Now you can do import with "from tiny_test_hatchery.Sub-Package ..."
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tiny_test_hatchery"))
)
