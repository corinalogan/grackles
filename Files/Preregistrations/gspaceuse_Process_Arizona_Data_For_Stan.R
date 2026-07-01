####################### Individual data - identical to that in search velocity analysis
covariates = matrix(NA,nrow=nbirds, ncol=9)

for(n in 1:nbirds){
  covariates[n, 1:9] = c(t(d_ind[which(d_ind$Bird.Name==birds[n]),c("Latency","Duration", "Sex", "History", "Breeding.Sites", "Food.Sites", "SMI", "Group.Size", "Season2")]))
}

covariates = as.data.frame(covariates) 
colnames(covariates) = c("Latency","Duration", "Sex", "History", "Breeding.Sites", "Food.Sites", "SMI", "Group.Size", "Season2")
 
 covariates$Latency = normalize(covariates$Latency)
 covariates$Duration = normalize(covariates$Duration)
 covariates$History = normalize(covariates$History)
 covariates$Breeding.Sites = normalize(covariates$Breeding.Sites)
 covariates$Food.Sites = normalize(covariates$Food.Sites)    
 covariates$SMI = normalize(covariates$SMI)
 covariates$Group.Size = normalize(covariates$Group.Size)
 covariates$Sex = ifelse(covariates$Sex == "M", 1, 0)
 covariates$Season2 = ifelse(covariates$Season2 == "Non-breeding", 1, 0)
 covariates = cbind(Intercept = 1, covariates)

 d_cov_az = cbind(covariates,birds)


########################################################### To study auto-correlation in space use, we need to look at successive days.
# This code just figures out which days of data can be modeled
PriorSuitability = apply(results, 1, sum, na.rm=TRUE)

results[is.na(results)] = 0

# If at least 4 points in a week, then code as a 1
data_in_day = ifelse(apply(results, 2:3, sum)>4,1,0)

# If there is data for the week and week day, code as 1
data_in_day_star = array(0,c(ndays, nbirds))

data_in_day_star[1,] = rep(0, nbirds)
for(j in 2:ndays)
data_in_day_star[j,] = ifelse(data_in_day[j,] == 1 & data_in_day[j-1,] == 1, 1, 0)

# If we need to use the data in stan, code as 1
data_in_day_use = array(0,c(ndays, nbirds))

data_in_day_use[1,] = rep(0, nbirds)
for(j in 1:(ndays-1))
data_in_day_use[j,] = ifelse(data_in_day_star[j,] + data_in_day_star[j+1,] > 0, 1, 0)
data_in_day_use[j,] = data_in_day_star[j,]

estimate_locs = which(data_in_day_use==1,arr.ind=TRUE)
n_estimates = nrow(estimate_locs)

########################## Prep for stan
#"Intercept"      "Latency"   "Duration"     "Sex"      "History"    "Breeding.Sites"   "Food.Sites"     "SMI"     "Group.Size"   "Season2"
model_dat = list(
 n_days = ndays,
 n_birds = nbirds,
 n_bins = nbins^2,
 n_estimates = n_estimates,
 estimate_locs=estimate_locs,
 data_in_year = data_in_day,
 data_in_day_star = data_in_day_star,
 data_in_day_use = data_in_day_use,
 Outcomes = results,
 PriorSuitability=(PriorSuitability+1),
 Covariates = covariates,
 Z = c(1,1,0,0,0,0,0,0,0,0)
 )

