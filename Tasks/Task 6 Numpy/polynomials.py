import numpy as np
a = list(map(float, input().split()))
print(np.polyval(a, float(input())))
