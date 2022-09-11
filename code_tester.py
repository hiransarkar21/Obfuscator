import python_obfuscator
from python_obfuscator.techniques import add_random_variables, variable_renamer
obfuscator = python_obfuscator.obfuscator()

code_to_obfuscate = "print('hello world')"
obfuscated_code = obfuscator.obfuscate(code_to_obfuscate)
print(obfuscated_code)