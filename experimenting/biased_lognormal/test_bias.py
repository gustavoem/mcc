from scipy.stats import lognorm
import statistics
import numpy as np

def get_underlying_normal_params(mu, s2):
    mu2 = mu * mu
    nrm_mean = np.log(mu2 / np.sqrt(s2 + mu2))
    nrm_s2 = np.log((s2 + mu2) / mu2)
    return nrm_mean, nrm_s2


lognrm_mean = 1e-5
lognrm_var = 10
norm_mean, norm_var = get_underlying_normal_params(lognrm_mean, \
        lognrm_var)
sample = [lognorm.rvs(scale=np.exp(norm_mean), s=np.sqrt(norm_var)) \
        for _ in range(50000)]
print ("Sample mean: ", statistics.mean(sample))
print ("Sample variance: ", statistics.variance(sample))


# lognrm_mean = 3
# lognrm_var = 10
# norm_mean, norm_var = get_underlying_normal_params(lognrm_mean, \
        # lognrm_var)
# sample = [lognorm.rvs(scale=np.exp(norm_mean), s=np.sqrt(norm_var)) \
        # for _ in range(50000)]
# print ("Sample mean: ", statistics.mean(sample))
# print ("Sample variance: ", statistics.variance(sample))



# lognrm_mean = 1
# lognrm_var = 5
# norm_mean, norm_var = get_underlying_normal_params(lognrm_mean, \
        # lognrm_var)
# sample = [lognorm.rvs(scale=np.exp(norm_mean), s=np.sqrt(norm_var)) \
        # for _ in range(50000)]
# print ("Sample mean: ", statistics.mean(sample))
# print ("Sample variance: ", statistics.variance(sample))
