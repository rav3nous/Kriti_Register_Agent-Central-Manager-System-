import json
from agents import function_tool
with open('tools/phone_number/country_codes_for_poc.json','r') as file:
# with open('country_codes_for_poc.json','r') as file:
    data= json.load(file)
@function_tool
def get_country_codes():
    result=""
    for country,code in data.items():
        result+=f"{country} : {code}\n"
    return result

# print(get_country_codes())