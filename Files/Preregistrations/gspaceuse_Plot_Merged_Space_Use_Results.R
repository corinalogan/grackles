######################## Merge AZ and CA data
 res_all = rbind(results_ca, results_asu)
 colnames(res_all) = c("Variable", "M", "sd", "L", "H", "n_eff", "Rhat4", "Site")

############### Rename some stuff
res_all$Variable[which(res_all$Variable=="Sex")] = "Male (vs. Female)"
res_all$Variable[which(res_all$Variable=="Season2")] = "Breeding season"
res_all$Variable[which(res_all$Variable=="Breeding.Sites")] = "Breeding sites"
res_all$Variable[which(res_all$Variable=="Food.Sites")] = "Food sites"
res_all$Variable[which(res_all$Variable=="SMI")] = "Body condition (as SMI)"
res_all$Variable[which(res_all$Variable=="Group.Size")] = "Group size"   
res_all$Variable[which(res_all$Variable=="History")] = "Captivity History"

res_all$Variable[which(res_all$Variable=="Duration")] = "Duration near"   
res_all$Variable[which(res_all$Variable=="Latency")] = "Latency to approach"     

res_all$Type = ifelse(res_all$Variable %in% c("Duration near", "Latency to approach"), "Experimental\n measures", "Additional\n measures")
res_all$Outcome = "Temporal auto-correlation measure"

# Plot effects of covariates on exploratoryness
honey_pal = plvs_vltra("honey_pot", rev=FALSE)
cloud_pal = plvs_vltra("summer_clouds", rev=FALSE)

res_out_preds = ggplot(res_all, aes(M, Variable)) +
 geom_vline(xintercept=0, linetype="dashed")+
  geom_linerange(
    aes(y = Variable, xmin = L, xmax = H, group = Site, color = Site), linewidth = 2, alpha=0.99,
    position = position_dodge(0.5)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.5), size = 3
    )  +
   scale_color_manual(values = c(honey_pal[1], cloud_pal[2])) +
  ylab("") + xlab("Estimated value") + theme(legend.position="bottom") + theme(text=element_text(size=18)) +
   facet_grid(Type ~ Outcome,  scales = "free", space='free_y', switch="y") +  scale_y_discrete(position = "right")
res_out_preds

#ggsave("Preds.pdf",res_out_preds, height=6,width=6)


# Extract bird-specific parameters
res_df = summary(m0ca,pars="B")$summary
res_df = as.data.frame(res_df)
res_df$Version = rep(c(1,2),22)
res_df = res_df[which(res_df$Version==2),]
res_df$Site = "CA"
res_df_ca = res_df
res_df_ca$ID = 1:22
res_df_ca = res_df_ca[which(!res_df_ca$ID %in% c(2,15)),] # drop birds with super wide posteriors, probably from not having sequential weeks of data
res_df_ca = res_df_ca[order(res_df_ca$"50%"),]
res_df_ca$ID = 1:20                                       # re-label the IDS 

res_df = summary(m0,pars="B")$summary
res_df = as.data.frame(res_df)
res_df$Version = rep(c(1,2),19)
res_df = res_df[which(res_df$Version==2),]
res_df$Site = "AZ"
res_df_az = res_df
res_df_az = res_df_az[order(res_df_az$"50%"),]
res_df_az$ID = 1:19

# Merge CA and AZ data
res_df = rbind(res_df_az,res_df_ca)
colnames(res_df) = c("mean", "se_mean", "sd", "L", "25%", "M", "75%", "H", "n_eff", "Rhat", "Version", "Site", "ID")

# Plot bird-level exploratoryness
res_out = ggplot(res_df, aes(ID, M)) +
  geom_linerange(
    aes(x = ID, ymin = L, ymax = H, group = Site, color = Site), linewidth = 2, 
    position = position_dodge(0.5)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.5), size = 3
    )+
   scale_color_manual(values = c(honey_pal[1], cloud_pal[2])) +
  xlab("Bird ID (sorted, within sites)") + ylab("Temporal auto-correlation measure") + theme(legend.position="bottom") + theme(text=element_text(size=18))

# ggsave("Explore.pdf",res_out,height=6,width=6)


write.csv(res_all, "Space_Use_Results.csv")
write.csv(res_df, "Space_Use_Bird_Results.csv")


  full_grid = (res_out + res_out_preds ) + plot_layout(nrow = 1)

ggsave("Space_Use_Results.pdf", plot = full_grid, height = 9, width = 18)

########################################### Now merge to get vals for table 2
res_df = summary(m0ca,pars="B")$summary
res_df = as.data.frame(res_df)
res_df$Version = rep(c(1,2),22)
res_df = res_df[which(res_df$Version==2),]
res_df$Site = "CA"
res_df_ca = res_df

res_df = summary(m0,pars="B")$summary
res_df = as.data.frame(res_df)
res_df$Version = rep(c(1,2),19)
res_df = res_df[which(res_df$Version==2),]
res_df$Site = "AZ"
res_df_az = res_df

su_covs = rbind(model_dat_ca$Covariates, model_dat$Covariates)
su_outcomes = rbind(res_df_ca, res_df_az)

su_merg = cbind(su_covs,su_outcomes)
su_merg$ID = 1:nrow(su_merg)

su_merg = su_merg[which(!su_merg$ID %in% c(2,15)),] # drop birds with super wide posteriors, probably from not having sequential weeks of data

fit_su = lm(mean ~ Site + Sex + History + Season2, data=su_merg)
write.csv(round(cbind(coef(fit_su),confint(fit_su)),3),"res_su.csv")
