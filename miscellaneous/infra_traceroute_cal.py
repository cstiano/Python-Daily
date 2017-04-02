import numpy as np 
ufpe = [54.976, 50.216, 50.091, 40.026, 39.764, 45.465, 30.715, 32.733]
ufrj = [64.995, 65.656, 68.124, 67.428, 67.415, 72.672, 65.335, 66.055, 68.514]
franca = [213.583, 218.202, 218.158, 209.712, 204.060, 217.985, 199.820, 209.319, 216.286]
japao = [270.315, 272.152, 278.087, 278.421, 268.932, 274.245, 270.535, 272.553, 276.923]

print np.mean(ufpe, axis = 0)
print np.std(ufpe, axis = 0)

print np.mean(ufrj, axis = 0)
print np.std(ufrj, axis = 0)

print np.mean(franca, axis = 0)
print np.std(franca, axis = 0)

print np.mean(japao, axis = 0)
print np.std(japao, axis = 0)
