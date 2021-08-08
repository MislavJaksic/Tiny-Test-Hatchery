"""
    tiny-test-hatchery.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys

from tiny_test_hatchery import pytest_gen


def main(args):
    """main() will be run if you run this script directly"""
    test_file_path = "test_eggs.py"
    program_file_path = "D:/Repositories/rapdevpy/rapdevpy/api_file_cache.py"
    pytest_gen.generate_test_file_from_file(test_file_path, program_file_path)


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
