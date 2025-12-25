from Function import math_operations
from Function import string_operations

result1 = math_operations.add(5, 3)
result2 = math_operations.multiply(4, 6)
result3 = math_operations.is_even(7)

text1 = string_operations.reverse_string('Привет')
text2 = string_operations.capitalize_words('привет мир')
print(result1,result2,result3)
print(text1,text2)