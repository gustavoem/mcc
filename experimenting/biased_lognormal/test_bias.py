from scipy.stats import lognorm
import scipy
import statistics
import numpy as np

def get_underlying_normal_params(m, v):
    m2 = m * m
    nrm_mean = 1.5 * np.log(m2) - .5 * (np.log(m2) + np.log(v + m2))
    nrm_mean = 1.5 * np.log(m2) - .5 * (np.log(m2 * (v + m2)))
    print ("v = ", v)
    print ("m2 = ", m2)
    print ("v + m2 = ", v + m2)
    print ("(v + m2) / m2 = ", ((v + m2) / m2))
    print ("m2 / sqrt(v + m2)", m2 / np.sqrt(v + m2))
    nrm_var = np.log(v / m2 + 1)
    return nrm_mean, nrm_var

def get_scipy_log_params(m, v):
    s = np.sqrt(np.log(.5 * (np.sqrt(4 * v + 1) + 1)))
    loc =  m - lognorm.mean(s)
    return loc, s

lognrm_mean = 1e-3
lognrm_var = 10
norm_params = get_underlying_normal_params(lognrm_mean, lognrm_var)
print("Calculated normal params, mu and sigma^2: ", norm_params)
# norm_mean = norm_params[0]
# norm_var = norm_params[1]
# sample = [lognorm.rvs(scale=np.exp(norm_mean), s=np.sqrt(norm_var)) \
        # for _ in range(50000)]
# print("Sample mean: ", statistics.mean(sample))
# print("Sample variance: ", statistics.variance(sample))

lognrm_mean = 1e-3
lognrm_var = 10
loc, s = get_scipy_log_params(lognrm_mean, lognrm_var)
print("Calculated scipy params, loca and s: ", loc, s)
sample = [lognorm.rvs(s, loc=loc) for _ in range(50000)]
for t in sample:
    if t < 0:
        print("oh no")
print("Sample mean: ", statistics.mean(sample))
print("Sample variance: ", statistics.variance(sample))

# print(lognorm.pdf(-0.2,s, loc=loc))
