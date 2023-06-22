from feloopy import *

# Data (Product, Season, Order quantity, Demand)
data = np.array([(1, 1, 100, 120), 
                 (1, 2,  80,  70), 
                 (1, 1, 120, 140), 
                 (2, 1, 200, 230), 
                 (2, 2, 150, 160), 
                 (2, 2, 140, 150)])

#Estimating the jont probability distribution

from scipy.stats import gaussian_kde

num_bins = 3
order_quantity_bins = np.linspace(50, 250, num_bins + 1)
demand_bins = np.linspace(50, 300, num_bins + 1)
data[:, 2] = np.digitize(data[:, 2], order_quantity_bins) - 1
data[:, 3] = np.digitize(data[:, 3], demand_bins) - 1

kde = gaussian_kde(data.T)
joint_prob = np.zeros((2, 2, num_bins, num_bins))
for i in range(2):
    for j in range(2):
        for k in range(num_bins):
            for l in range(num_bins):
                joint_prob[i, j, k, l] = kde.evaluate([i + 1, j + 1, k, l])

joint_prob /= joint_prob.sum()

epsilon = 1e-9
P_Y_given_X = np.divide(joint_prob, joint_prob.sum(axis=(2, 3), keepdims=True) + epsilon)

#Modeling and solving 

m = target_model('exact', 'cso', 'gurobi')

x = m.pvar('x', [2,2])
z = m.pvar('z')

x_data = np.array([[1, 2], 
                   [1, 2]])

order_quantities = np.array(range(100, 201, 50))

demands = np.array(range(70, 251, 50))

def cost(z, y):
    return (z - y)**2

m.obj(sum([P_Y_given_X[i, j, k, l] * cost(z, demands[l]) for i in range(2) for j in range(2) for k in range(num_bins) for l in range(num_bins)]))

for i in range(2):
    for j in range(2):
        m.con(x[i, j] == x_data[i, j])

m.sol(['min'],'gurobi')

m.report()
