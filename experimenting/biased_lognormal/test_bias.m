lognrm_mu = 1e-5;
lognrm_s2 = 10;

lognrm_mu2 = lognrm_mu * lognrm_mu;
norm_mu = log(lognrm_mu2 / sqrt(lognrm_s2 + lognrm_mu2))
norm_s2 = log((lognrm_s2 + lognrm_mu2) / lognrm_mu2)
norm_s = sqrt(norm_s2);

sample = normrnd(norm_mu, norm_s, 50000000, 1);
e_sample = exp (sample);
sample_mean = mean(e_sample)
std_sample = std(e_sample)
