#Strong Password Validation using Lookahead Assertions
import re

def validate_password(password):
    pattern = r'''
        ^                       # Start of string
        (?=.*[A-Z])             # At least one uppercase letter
        (?=.*[a-z])             # At least one lowercase letter
        (?=.*\d)                # At least one digit
        (?=.*[@$!%*?&])         # At least one special character
        [A-Za-z\d@$!%*?&]{8,}   # Minimum 8 characters
        $                       # End of string
    '''

    if re.match(pattern, password, re.VERBOSE):
        print("Strong Password ✅")
    else:
        print("Weak Password ❌")

# Example
validate_password("Strong@123")


#Regular Expression Modifiers (Flags) Demonstration
import re

text = "Python is Powerful"
pattern = "python"

match = re.search(pattern, text, re.IGNORECASE)
print("IGNORECASE Match:", match.group())

#re.IGNORECASE
import re

text = "Python is Powerful"
pattern = "python"

match = re.search(pattern, text, re.IGNORECASE)
print("IGNORECASE Match:", match.group())

#re.MULTILINE
text = """Hello World
Python Programming
Welcome"""

pattern = r"^Python"

match = re.search(pattern, text, re.MULTILINE)
print("MULTILINE Match:", match.group())


#re.DOTALL
text = "Hello\nPython"
pattern = r"Hello.*Python"

match = re.search(pattern, text, re.DOTALL)
print("DOTALL Match:", match.group())
