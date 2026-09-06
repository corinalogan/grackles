########################################## Fit Baseline Stan model first, then add in Covariates via Z
iter = 2000
warmup = 1000
adapt_delta = 0.95
max_treedepth = 13
refresh = 300

model_covs = cmdstanr::cmdstan_model(stan_file="Code/stan_model_covars.stan")

model_dat$Z = c(1,1,0,0,0,0,0,0,0,0)
fit_1 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m1 = brms:::read_csv_as_stanfit(fit_1$output_files())

model_dat$Z = c(1,0,1,0,0,0,0,0,0,0)
fit_2 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m2 = brms:::read_csv_as_stanfit(fit_2$output_files())

model_dat$Z = c(1,0,0,1,0,0,0,0,0,0)
fit_3 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m3 = brms:::read_csv_as_stanfit(fit_3$output_files())

model_dat$Z = c(1,0,0,0,1,0,0,0,0,0)
fit_4 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m4 = brms:::read_csv_as_stanfit(fit_4$output_files())

model_dat$Z = c(1,0,0,0,0,1,0,0,0,0)
fit_5 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m5 = brms:::read_csv_as_stanfit(fit_5$output_files())

model_dat$Z = c(1,0,0,0,0,0,1,0,0,0)
fit_6 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m6 = brms:::read_csv_as_stanfit(fit_6$output_files())

model_dat$Z = c(1,0,0,0,0,0,0,1,0,0)
fit_7 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m7 = brms:::read_csv_as_stanfit(fit_7$output_files())

model_dat$Z = c(1,0,0,0,0,0,0,0,1,0)
fit_8 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m8 = brms:::read_csv_as_stanfit(fit_8$output_files())

model_dat$Z = c(1,0,0,0,0,0,0,0,0,1)
fit_9 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m9 = brms:::read_csv_as_stanfit(fit_9$output_files())

model_dat$Z = c(1,0,0,0,0,0,0,0,0,0)
fit_0 = model_covs$sample(data = model_dat, chains = 1, parallel_chains = 1, refresh = refresh, iter_warmup = warmup, iter_sampling = iter, max_treedepth = max_treedepth, adapt_delta = adapt_delta)
m0 = brms:::read_csv_as_stanfit(fit_0$output_files())


