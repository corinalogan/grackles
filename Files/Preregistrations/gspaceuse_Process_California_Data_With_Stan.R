########################################## Fit Baseline Stan model first, then add in Covariates via Z
iter = 2000
warmup = 1000
adapt_delta = 0.95
max_treedepth = 13

set_cmdstan_path(path = "/Users/kelseymccune/.cmdstan/cmdstan-2.35.0")

model_dat_ca$Z = c(1,1,0,0,0,0,0,0,0,0) #took 3.6 hrs
 m1ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,1,0,0,0,0,0,0,0)
 m2ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,1,0,0,0,0,0,0)
 m3ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,0,1,0,0,0,0,0)
 m4ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,0,0,1,0,0,0,0) # took 3.6hrs
 m5ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,0,0,0,1,0,0,0)
 m6ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,0,0,0,0,1,0,0)
 m7ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,0,0,0,0,0,1,0)
 m8ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,0,0,0,0,0,0,1)
 m9ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)

model_dat_ca$Z = c(1,0,0,0,0,0,0,0,0,0) # took 3.3 hrs
 m0ca = stan( file="stan_model_covars.stan", data=model_dat_ca, refresh=1, chains=1, control = list(adapt_delta = adapt_delta, max_treedepth = max_treedepth), iter=iter, warmup=warmup)




