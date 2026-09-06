########################################## Fit Baseline Stan model first, then add in Covariates via Z
iter = 2000
warmup = 1000
adapt_delta = 0.95
max_treedepth = 13
refresh = 300

model_covs = cmdstanr::cmdstan_model(stan_file="Code/stan_model_covars.stan")

model_dat_ca$Z = c(1,1,0,0,0,0,0,0,0,0)
fit_1ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m1ca = brms:::read_csv_as_stanfit(fit_1ca$output_files())

model_dat_ca$Z = c(1,0,1,0,0,0,0,0,0,0)
fit_2ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m2ca = brms:::read_csv_as_stanfit(fit_2ca$output_files())

model_dat_ca$Z = c(1,0,0,1,0,0,0,0,0,0)
fit_3ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m3ca = brms:::read_csv_as_stanfit(fit_3ca$output_files())

model_dat_ca$Z = c(1,0,0,0,1,0,0,0,0,0)
fit_4ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m4ca = brms:::read_csv_as_stanfit(fit_4ca$output_files())

model_dat_ca$Z = c(1,0,0,0,0,1,0,0,0,0)
fit_5ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m5ca = brms:::read_csv_as_stanfit(fit_5ca$output_files())

model_dat_ca$Z = c(1,0,0,0,0,0,1,0,0,0)
fit_6ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m6ca = brms:::read_csv_as_stanfit(fit_6ca$output_files())

model_dat_ca$Z = c(1,0,0,0,0,0,0,1,0,0)
fit_7ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m7ca = brms:::read_csv_as_stanfit(fit_7ca$output_files())

model_dat_ca$Z = c(1,0,0,0,0,0,0,0,1,0)
fit_8ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m8ca = brms:::read_csv_as_stanfit(fit_8ca$output_files())

model_dat_ca$Z = c(1,0,0,0,0,0,0,0,0,1)
fit_9ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m9ca = brms:::read_csv_as_stanfit(fit_9ca$output_files())

model_dat_ca$Z = c(1,0,0,0,0,0,0,0,0,0)
fit_0ca = model_covs$sample(data = model_dat_ca, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m0ca = brms:::read_csv_as_stanfit(fit_0ca$output_files())



