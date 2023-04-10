# cloudProject
The paper "Reducing response latency of composite functions-as-a-service through scheduling" by Pawel Zuk and Krzysztof Rzadca proposes a scheduling mechanism that reduces the response latency of serverless functions when they are composed into a larger application. The authors identify that the delay incurred in function composition can be a significant bottleneck for composite applications and propose an approach that uses scheduling to reduce latency.

The authors propose a scheduling algorithm that selects the optimal execution order of functions in a composite application, based on the expected execution times of each function. The algorithm uses Shortest Job First (SJF) and First In First Out (FIFO) scheduling policies to minimize the response latency of the composite application.

To evaluate their approach, the authors implement a prototype using the OpenWhisk FaaS platform and conduct experiments to measure the response latency of composite applications with and without their scheduling mechanism. The results show that their approach reduces the response latency by up to 60%, demonstrating the effectiveness of the proposed scheduling mechanism.

Overall, the paper highlights the importance of scheduling in reducing the response latency of composite applications and proposes a novel approach that uses SJF and FIFO policies to minimize response latency. The experimental results demonstrate the effectiveness of the approach and provide insights for future research in this area.
