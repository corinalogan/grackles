######################## Merge AZ and CA data
 res_all = rbind(results_ca, results_asu)
 colnames(res_all) = c("Variable", "M", "sd", "L", "H", "n_eff", "Rhat4", "Site")
 res_all$Variable[which(res_all$Variable=="Sex")]="Male"

# Plot effects of covariates on exploratoryness
res_out_preds = ggplot(res_all, aes(Variable, M)) +
 geom_hline(yintercept=0,linetype="dashed")+
  geom_linerange(
    aes(x = Variable, ymin = L, ymax = H, group = Site, color = Site), linewidth = 2, alpha=0.5,
    position = position_dodge(0.5)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.5), size = 3
    )+
  scale_color_manual(values = c("darkcyan", "darkgoldenrod2")) +
  xlab("Predictor variable") + ylab("Estimated value") + coord_flip() + theme(legend.position="bottom") + theme(text=element_text(size=18))

ggsave("Preds.pdf",res_out_preds, height=6,width=6)


# Extract bird-specific parameters
res_df = summary(m0ca,pars="B")$summary
res_df = as.data.frame(res_df)
res_df$Version = rep(c(1,2),22)
res_df = res_df[which(res_df$Version==1),]
res_df$Site = "CA"
res_df_ca = res_df
res_df_ca = res_df_ca[order(res_df_ca$mean),]
res_df_ca$ID = 1:22

res_df = summary(m0,pars="B")$summary
res_df = as.data.frame(res_df)
res_df$Version = rep(c(1,2),22)
res_df = res_df[which(res_df$Version==1),]
res_df$Site = "AZ"
res_df_az = res_df
res_df_az = res_df_az[order(res_df_az$mean),]
res_df_az$ID = 1:22

# Merge CA and AZ data
res_df = rbind(res_df_az,res_df_ca)
colnames(res_df) = c("mean", "se_mean", "sd", "L", "25%", "M", "75%", "H", "n_eff", "Rhat", "Version", "Site", "ID")

# Plot bird-level exploratoryness
res_out = ggplot(res_df, aes(ID, M)) +
  geom_linerange(
    aes(x = ID, ymin = L, ymax = H, group = Site, color = Site), linewidth = 2, alpha=0.5,
    position = position_dodge(0.5)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.5), size = 3
    )+
  scale_color_manual(values = c("darkcyan", "darkgoldenrod2")) +
  xlab("Bird ID (sorted, within sites)") + ylab("Exploratory measure") + theme(legend.position="bottom") + theme(text=element_text(size=18))

ggsave("Explore.pdf",res_out,height=6,width=6)


write.csv(res_all, "Space_Use_Results.csv")
write.csv(res_df, "Space_Use_Bird_Results.csv")
