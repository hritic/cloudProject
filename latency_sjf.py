from queue import Queue

def preprocess_hosted_functions(hosted_functions):
    hosted_functions_dict = {}
    for hosted_function in hosted_functions:
        hosted_functions_dict[hosted_function.id] = hosted_function
    return hosted_functions_dict

def process_hosted_function_exec(hosted_function, queue, hosted_functions_dict):
    weights = []
    for dep in hosted_function.dependencies:
        weights.append((hosted_functions_dict[dep].exec_time, hosted_functions_dict[dep].id))
    weights = sorted(weights, key=lambda x: x[0])
    for weight in weights:
        queue.put(weight[1])
    return hosted_function.exec_time
        
def process_hosted_function_setup(hosted_function, queue, hosted_functions_dict):
    weights = []
    for dep in hosted_function.dependencies:
        weights.append((hosted_functions_dict[dep].setup_time, hosted_functions_dict[dep].id))
    weights = sorted(weights, key=lambda x: x[0])
    for weight in weights:
        queue.put(weight[1])
    return hosted_function.exec_time

def preload_queue_exec(hosted_functions):
    queue = Queue(maxsize=50)
    weights = []
    for hosted_function in hosted_functions:
        if len(hosted_function.dependencies) == 0:
            weights.append((hosted_function.exec_time, hosted_function.id))
    weights = sorted(weights, key=lambda x: x[0])
    for weight in weights:
        queue.put(weight[1])
    return queue

def preload_queue_setup(hosted_functions):
    queue = Queue(maxsize=50)
    weights = []
    for hosted_function in hosted_functions:
        if len(hosted_function.dependencies) == 0:
            weights.append((hosted_function.setup_time, hosted_function.id))
    weights = sorted(weights, key=lambda x: x[0])
    for weight in weights:
        queue.put(weight[1])
    return queue


def get_total_latency(hosted_functions):
    time1 = 0.0
    time2 = 0.0
    hosted_functions_dict = preprocess_hosted_functions(hosted_functions)
    queue1 = preload_queue_exec(hosted_functions)
    queue2 = preload_queue_setup(hosted_functions)
    while queue1.empty() is False:
        hosted_function = queue1.get()
        time1 = time1 + process_hosted_function_exec(hosted_functions_dict[hosted_function], queue1, hosted_functions_dict)

    while queue2.empty() is False:
        hosted_function = queue2.get()
        time2 = time2 + process_hosted_function_setup(hosted_functions_dict[hosted_function], queue2, hosted_functions_dict)
    
    return time1, time2
    
