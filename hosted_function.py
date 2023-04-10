from uuid import uuid4

class HostedFunction:
    def __init__(self) -> None:
        self.id = 0
        self.exec_time = 0.0
        self.setup_time = 0.0
        self.resources = 0
        self.env = "env0"
        self.dependencies = []
    
    def assign_weights(self, id, exec_time, setup_time, resources, env, dependencies):
        self.id = id
        self.exec_time = exec_time
        self.setup_time = setup_time
        self.resources = resources
        self.env = env
        self.dependencies = dependencies


def create_hosted_function(data):
    hf = HostedFunction()
    hf.assign_weights(data["id"], data["exec_time"], data["setup_time"], data["resources"], data["env"], data["dependencies"])
    return hf