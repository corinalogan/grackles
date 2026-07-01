########################################## Fit Baseline Stan model first, then add in Covariates via Z
iter = 2000
warmup = 1000
adapt_delta = 0.95
max_treedepth = 13

library(cmdstanr)
set_cmdstan_path(path = "/Users/kelseymccune/.cmdstan/cmdstan-2.35.0")
library(rstan)
model_dat$Z = c(1,1,0,0,0,0,0,0,0,0) # this one took 6 hours
 m1 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,1,0,0,0,0,0,0,0) # also took 6 hours
 m2 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,1,0,0,0,0,0,0) # took 11.5 hours!
 m3 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,0,1,0,0,0,0,0) # took 6.5hrs
 m4 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,0,0,1,0,0,0,0)
 m5 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,0,0,0,1,0,0,0) # only took 4 hrs
 m6 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,0,0,0,0,1,0,0)
 m7 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,0,0,0,0,0,1,0)
 m8 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,0,0,0,0,0,0,1) # 5.6 hrs
 m9 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat$Z = c(1,0,0,0,0,0,0,0,0,0) # only 4.8 hrs
 m0 = stan( file="stan_model_covars.stan", data=model_dat, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

