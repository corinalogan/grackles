########################################## Run search velocity analysis for AZ birds
 birds = c("Adobo", "Burrito", "Chalupa","Chilaquile", "Chile", "Diablo","Fideo", "Habanero", "Marisco", "Mofongo", 
           "Mole", "Pizza", "Pollito", "Queso", "Taco","Tapa", "Taquito", "Tomatillo", "Yuca")

 nbirds = length(birds)
 
####################### Latency & Duration - Individual data ####
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

##################################### Velocity Data
BNs = unique(d_az$Bird.Name)
DDs = unique(d_az$Date)

res = vector("list",1)
ticker = 1

for(b in 1:length(BNs)){
  for(d in 1:length(DDs)){
    res[[ticker]] = get_foraging_velocity(d_az, BNs[b], DDs[d])
    ticker = 1 + ticker 
  }}

res_all = do.call(rbind,res)

res_all_clean = res_all[which(res_all$FV<50),]
res_all_clean$LFV = log(res_all_clean$FV + 0.1)

# ggplot(res_all_clean, aes(LFV, colour=Bird, group=Bird)) + geom_density()

Mlfv = aggregate(res_all_clean$LFV ~ res_all_clean$Bird, FUN=mean)
Slfv = aggregate(res_all_clean$LFV ~ res_all_clean$Bird, FUN=sd)

colnames(Mlfv) = c("Bird.Name","MeanLFV")
colnames(Slfv) = c("Bird.Name","SigmaLFV")

lfv = merge(Mlfv, Slfv, by="Bird.Name")

colnames(d_cov_az)[11] = c("Bird.Name")

d_all.az = merge(d_cov_az, lfv, by="Bird.Name")

summary(lm(MeanLFV~Latency,data=d_all.az))
summary(lm(MeanLFV~Duration,data=d_all.az))
summary(lm(MeanLFV~Sex,data=d_all.az))
summary(lm(MeanLFV~History,data=d_all.az))
summary(lm(MeanLFV~Breeding.Sites,data=d_all.az))
summary(lm(MeanLFV~Food.Sites,data=d_all.az))
summary(lm(MeanLFV~SMI,data=d_all.az))
summary(lm(MeanLFV~Group.Size,data=d_all.az))
summary(lm(MeanLFV~Season2,data=d_all.az))


summary(lm(SigmaLFV~Latency,data=d_all.az))
summary(lm(SigmaLFV~Duration,data=d_all.az))
summary(lm(SigmaLFV~Sex,data=d_all.az))
summary(lm(SigmaLFV~History,data=d_all.az))
summary(lm(SigmaLFV~Breeding.Sites,data=d_all.az))
summary(lm(SigmaLFV~Food.Sites,data=d_all.az))
summary(lm(SigmaLFV~SMI,data=d_all.az))
summary(lm(SigmaLFV~Group.Size,data=d_all.az))
summary(lm(SigmaLFV~Season2,data=d_all.az))

res_df2 = res_df = data.frame(Outcome="MeanLFV", Pred="Vars", M=1.1, L=1.1, H=1.1)
res_df[1,] = make_res("MeanLFV", "Latency", lm(MeanLFV~Latency,data=d_all.az))
res_df[2,] = make_res("MeanLFV", "Duration", lm(MeanLFV~Duration,data=d_all.az))
res_df[3,] = make_res("MeanLFV", "Male", lm(MeanLFV~Sex,data=d_all.az))
res_df[4,] = make_res("MeanLFV", "History", lm(MeanLFV~History,data=d_all.az))
res_df[5,] = make_res("MeanLFV", "Breeding.Sites", lm(MeanLFV~Breeding.Sites,data=d_all.az))
res_df[6,] = make_res("MeanLFV", "Food.Sites", lm(MeanLFV~Food.Sites,data=d_all.az))
res_df[7,] = make_res("MeanLFV", "SMI", lm(MeanLFV~SMI,data=d_all.az))
res_df[8,] = make_res("MeanLFV", "Group.Size", lm(MeanLFV~Group.Size,data=d_all.az))
res_df[9,] = make_res("MeanLFV", "Season2", lm(MeanLFV~Season2,data=d_all.az))

res_df2[1,] = make_res("SigmaLFV", "Latency", lm(SigmaLFV~Latency,data=d_all.az))
res_df2[2,] = make_res("SigmaLFV", "Duration", lm(SigmaLFV~Duration,data=d_all.az))
res_df2[3,] = make_res("SigmaLFV", "Male", lm(SigmaLFV~Sex,data=d_all.az))
res_df2[4,] = make_res("SigmaLFV", "History", lm(SigmaLFV~History,data=d_all.az))
res_df2[5,] = make_res("SigmaLFV", "Breeding.Sites", lm(SigmaLFV~Breeding.Sites,data=d_all.az))
res_df2[6,] = make_res("SigmaLFV", "Food.Sites", lm(SigmaLFV~Food.Sites,data=d_all.az))
res_df2[7,] = make_res("SigmaLFV", "SMI", lm(SigmaLFV~SMI,data=d_all.az))
res_df2[8,] = make_res("SigmaLFV", "Group.Size", lm(SigmaLFV~Group.Size,data=d_all.az))
res_df2[9,] = make_res("SigmaLFV", "Season2", lm(SigmaLFV~Season2,data=d_all.az))

res_df$Site="AZ"
res_df2$Site="AZ"

res_az = rbind(res_df,res_df2)

res_az$M = as.numeric(res_az$M)
res_az$H = as.numeric(res_az$H)
res_az$L = as.numeric(res_az$L)