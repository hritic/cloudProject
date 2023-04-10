from hosted_function import HostedFunction, create_hosted_function
from uuid import uuid4
from latency_sjf import get_total_latency

function_ids = []

for i in range(9):
    function_ids.append(uuid4())

function_data = [
    {
        "id": function_ids[0],
        "exec_time": 10.12,
        "setup_time": 5.23,
        "resources": 51.3,
        "env": "env0",
        "dependencies": []
    },
    {
        "id": function_ids[1],
        "exec_time": 8.56,
        "setup_time": 2.34,
        "resources": 23.3,
        "env": "env1",
        "dependencies": [function_ids[0]]
    },
    {
        "id": function_ids[2],
        "exec_time": 12.78,
        "setup_time": 1.92,
        "resources": 66.4,
        "env": "env0",
        "dependencies": [function_ids[1]]
    },
    {
        "id": function_ids[3],
        "exec_time": 9.43,
        "setup_time": 1.76,
        "resources": 0.41,
        "env": "env2",
        "dependencies": [function_ids[0], function_ids[6]]
    },
    {
        "id": function_ids[4],
        "exec_time": 11.21,
        "setup_time": 0.81,
        "resources": 51.3,
        "env": "env3",
        "dependencies": [function_ids[1], function_ids[5]]
    },
    {
        "id": function_ids[5],
        "exec_time": 18.5,
        "setup_time": 8.89,
        "resources": 72.3,
        "env": "env2",
        "dependencies": [function_ids[3], function_ids[8]]
    },
    {
        "id": function_ids[6],
        "exec_time": 5.32,
        "setup_time": 0.56,
        "resources": 23.5,
        "env": "env4",
        "dependencies": [function_ids[2], function_ids[4], function_ids[5]]
    },
    {
        "id": function_ids[7],
        "exec_time": 8.32,
        "setup_time": 0.8,
        "resources": 34.5,
        "env": "env5",
        "dependencies": []
    },
    {
        "id": function_ids[8],
        "exec_time": 12.23,
        "setup_time": 11.56,
        "resources": 62.0,
        "env": "env4",
        "dependencies": []
    }
]

hosted_functions = []

for data in function_data:
    h = create_hosted_function(data)
    hosted_functions.append(h)

# Using Shortest Job First
latency1 = get_total_latency(hosted_functions)
latency1_exec = latency1[0]
latency1_setup = latency1[1]
print("Latency using SJF on Execution Time(ms): ", latency1_exec)
print("Latency using SJF on Setup Time(ms): ", latency1_setup)