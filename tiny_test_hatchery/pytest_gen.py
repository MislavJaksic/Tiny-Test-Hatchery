import re
from typing import Tuple, List

from loguru import logger

log_message = "what={}, why={}, how={}"


class Function:
    def __init__(self, name: str, signature: str):
        self.snake_name = name
        self.camel_name = self.snake_to_camel_case(name)
        self.signature = signature
        self.parameters = self.signature_to_parameters(signature)

    def snake_to_camel_case(self, name: str) -> str:
        return "".join([x.capitalize() for x in name.split("_")])

    def signature_to_parameters(self, signature: str) -> List[str]:
        return [
            x.split(":")[0] for x in signature.split(", ") if x != "self" if x != ""
        ]

    def __eq__(self, other):
        if self.snake_name == other.snake_name and self.signature == other.signature:
            return True
        return False

    def __repr__(self):
        return "Function[snake_name: {}, camel_name: {}, signature: {}, parameters: {}]".format(
            self.snake_name, self.camel_name, self.signature, self.parameters
        )


def generate_test_file_from_file(test_file_path: str, program_file_path: str):
    logger.info(
        log_message,
        "Generate test file here {} for program here {}".format(
            test_file_path, program_file_path
        ),
        "Inspection",
        "Log inputs",
    )
    functions = get_functions(program_file_path)
    create_function_test_file(functions, test_file_path)


def get_functions(file_path: str) -> List[Function]:
    functions = []
    with open(file_path, "r") as file:
        for line in file:
            function = parse_function_line(line)
            if function:
                functions.append(function)
    return functions


def parse_function_line(line: str) -> Function:
    match = re.search("^[\s]*def (.*)\((.*)\).*:", line)
    if match:
        function = Function(match.group(1), match.group(2))
        logger.info(
            log_message,
            "Line: <{}> -> {}".format(line, str(function)),
            "Parsing",
            "Parse function text line",
        )
        return function
    else:
        return None  # ToDo do not return null!!!


def create_function_test_file(functions: List[Function], file_path: str):
    with open(file_path, "w") as file:
        file.write("# Auto-generated pytest file\n")
        for function in functions:
            file.write("\n")
            file.write("class Test{}:\n".format(function.camel_name))
            file.write("    def test_{}(self):\n".format(function.snake_name))
            for param in function.parameters:
                file.write("        {} = None\n".format(param))
            file.write(
                "        assert class_under_test.{}({}) == None\n".format(
                    function.snake_name, ", ".join(function.parameters)
                )
            )
