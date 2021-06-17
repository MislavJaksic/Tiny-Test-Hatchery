import re
from typing import Tuple, List

from loguru import logger

log_message = "what={}, why={}, how={}"


def generate_test_file_from_file(test_file_path: str, program_file_path: str):
    logger.info(log_message, "Generate test file here {} for program here {}".format(test_file_path, program_file_path),
                "Inspection", "Log inputs")
    functions = get_functions(program_file_path)
    create_function_test_file(functions, test_file_path)


def get_functions(file_path: str) -> List[Tuple[str, str]]:
    functions = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.search("^[\s]*def (.*)\((.*)\).*:", line)
            if match:
                function = (match.group(1), match.group(2))
                functions.append(function)
                logger.info(log_message, "Line: <{}> -> function/parameter {}".format(line, str(function)), "Parsing",
                            "Parse function text line")
    return functions


def create_function_test_file(functions: List[Tuple[str, str]], file_path: str):
    with open(file_path, "w") as file:
        file.write("# Auto-generated pytest file\n")
        for function in functions:
            file.write("\n")
            class_name = snake_case_to_camel_case(function[0])
            file.write("class Test{}:\n".format(class_name))
            file.write("    def test_{}(self):\n".format(function[0]))
            calling_params = filter_parameters(function[1])
            for param in calling_params:
                file.write("        {} = \n".format(param))
            file.write(
                "        assert class_under_test.{}({}) == None\n".format(
                    function[0], ", ".join(calling_params)
                )
            )


def snake_case_to_camel_case(name: str) -> str:
    return "".join([x.capitalize() for x in name.split("_")])


def filter_parameters(parameters: str) -> List[str]:
    return [x.split(":")[0] for x in parameters.split(", ") if x != "self"]
