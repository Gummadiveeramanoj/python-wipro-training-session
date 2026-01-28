#Using re.match()
import re

emp_id = "EMP123"

pattern = r"EMP\d{3}"

match = re.match(pattern, emp_id)

if match:
    print("Valid Employee ID")
    print("Matched Group:", match.group())
else:
    print("Invalid Employee ID")
#Using re.search()
import re

text = "Please contact us at support123@gmail.com for help."

pattern = r"\w+@\w+\.\w+"

search = re.search(pattern, text)

if search:
    print("Email Found:", search.group())
else:
    print("No Email Found")
#Demonstrating Meta-characters & Special Sequences
import re

text = "User1 has 3 files"

pattern = r"\w+\s\d+\s\w+"

match = re.search(pattern, text)

if match:
    print("Matched Text:", match.group())
#Capturing Groups (Parentheses)
import re

text = "EMP456 works in IT"

pattern = r"(EMP)(\d{3})"

match = re.search(pattern, text)

if match:
    print("Full Match:", match.group())
    print("Group 1 (Prefix):", match.group(1))
    print("Group 2 (Digits):", match.group(2))
