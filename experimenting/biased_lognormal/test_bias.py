from scipy.stats import lognorm
import scipy
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
print("norm_mu = ", norm_mean)
print("norm_var = ", norm_var)
sample = [lognorm.rvs(scale=np.exp(norm_mean), s=np.sqrt(norm_var)) \
        for _ in range(50000)]
print("Sample mean: ", statistics.mean(sample))
print("Sample variance: ", statistics.variance(sample))

log_sample = np.log(sample)
est_mu = statistics.mean(log_sample)
est_var = statistics.variance(log_sample)
print("Estimated mu = ", est_mu)
print("Estimated var = ", est_var)

sampletimes100 = np.array(sample) * 10000
print("sample_variance = ", statistics.variance(sampletimes100) / 1e8)


lognrm_mean = np.longdouble(1e-5)
lognrm_var = np.longdouble(10)
norm_mean, norm_var = get_underlying_normal_params(lognrm_mean, \
        lognrm_var)
print(norm_mean, norm_var)
sample = [lognorm.rvs(scale=np.exp(norm_mean), s=np.sqrt(norm_var)) \
    for _ in range(50000)]

mean = 0
for val in sample:
    mean += val
mean /= len(sample)

var = 0
for val in sample:
    var += (val - mean) ** 2
var /= len(sample)
print ("Sample mean: ", mean)
print ("Sample variance: ", var)


lognrm_mean = 1e-5
lognrm_var = 10
norm_mean, norm_var = get_underlying_normal_params(lognrm_mean, \
        lognrm_var)
# This time, instead of sampling from X ~ Lognormal (mu, s2), we'll
# sample from Y = 1 / X ~ Lognormal (-mu, s2)
sample = [lognorm.rvs(scale=np.exp(-norm_mean), s=np.sqrt(norm_var)) \
        for _ in range(50000)]
sample = np.array (sample)
sample = 1 / sample
print("Sample mean: ", statistics.mean(sample))
print("Sample variance: ", statistics.variance(sample))


lognrm_mean = 1e-5
lognrm_var = 10
norm_mean, norm_var = get_underlying_normal_params(lognrm_mean, \
        lognrm_var)
# This time, instead of sampling from X ~ Lognormal (mu, s2), we'll
# sample from Y ~ Lognormal (0, s2) then X = Y / exp (mu)
sample = [lognorm.rvs(scale=1, s=np.sqrt(norm_var)) \
        for _ in range(50000)]
sample = np.array (sample)
sample *= np.exp (norm_mean)
print("Sample mean: ", statistics.mean(sample))
print("Sample variance: ", statistics.variance(sample))



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
