import pandas as pd
import numpy as np
import json
from pprint import pprint

with open('./Data/data_0.json') as f:
    data = json.load(f)

# print(json.dumps(data, sort_keys=True, indent=4))

# print(data)
new_json_string = json.dumps(data, indent=6)
print(new_json_string)

# new_json_string = json.dumps(data, indent=6, sort_keys=True)
# print(new_json_string)
