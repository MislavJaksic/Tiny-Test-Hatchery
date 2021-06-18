import pytest

from tiny_test_hatchery import pytest_gen
from tiny_test_hatchery.pytest_gen import Function


@pytest.fixture(scope="function")
def function():
    yield Function("fun", "par")

# class TestGenerateTestFileFromFile: # ToDo working with files is time consuming
#     def test_generate_test_file_from_file(self):
#         test_file_path = None
#         program_file_path = None
#         assert pytest_gen.generate_test_file_from_file(test_file_path, program_file_path) == None
#
#
# class TestGetFunctions: # ToDo working with files is time consuming
#     def test_get_functions(self):
#         file_path = None
#         assert pytest_gen.get_functions(file_path) == None


class TestParseFunctionLine:
    def test_empty(self):
        line = ""
        assert pytest_gen.parse_function_line(line) == None

    def test_fake_function(self):
        line = "            file.write('    def test_{}(self):\n'.format(function.snake_name))"
        assert pytest_gen.parse_function_line(line) == None

    def test_true_function(self):
        line = "def parse_function_line(line: str) -> Function:"
        assert pytest_gen.parse_function_line(line) == Function("parse_function_line", "line: str")


# class TestCreateFunctionTestFile: # ToDo working with files is time consuming
#     def test_create_function_test_file(self):
#         functions = None
#         file_path = None
#         assert pytest_gen.create_function_test_file(functions, file_path) == None


class TestSnakeToCamelCase:
    def test_empty_string(self, function):
        name = ""
        assert function.snake_to_camel_case(name) == ""

    def test_single_word(self, function):
        name = "hello"
        assert function.snake_to_camel_case(name) == "Hello"

    def test_many_words(self, function):
        name = "hello_world"
        assert function.snake_to_camel_case(name) == "HelloWorld"


class TestSignatureToParameters:
    def test_empty_string(self, function):
        parameters = ""
        assert function.signature_to_parameters(parameters) == []

    def test_single_parameter(self, function):
        parameters = "var"
        assert function.signature_to_parameters(parameters) == ["var"]

    def test_many_parameters(self, function):
        parameters = "var1, var2"
        assert function.signature_to_parameters(parameters) == ["var1", "var2"]

    def test_filter_self_parameter(self, function):
        parameters = "var1, self, var2"
        assert function.signature_to_parameters(parameters) == ["var1", "var2"]
