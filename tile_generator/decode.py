import json

def replace_placeholders(input_string, data):
    for key, value in data.items():
        placeholder = "{" + key + "}"
        unicode_char = value
        input_string = input_string.replace(placeholder, unicode_char)
    return input_string

# Load data from data.json
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Test input string
input_string = "10 {steak} = {emerald_block}"

# Replace placeholders with Chinese characters
output_string = replace_placeholders(input_string, data)

# Print the output string
print(output_string)
