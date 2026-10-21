######################## Merge AZ and CA data
res_ca_az = rbind(res_ca, res_az)

########## Rename some variables
res_ca_az$Pred[which(res_ca_az$Pred=="Male")] = "Male (vs. Female)"
res_ca_az$Pred[which(res_ca_az$Pred=="Breeding.Season")] = "Breeding season"
res_ca_az$Pred[which(res_ca_az$Pred=="Breeding.Sites")] = "Breeding sites"
res_ca_az$Pred[which(res_ca_az$Pred=="Food.Sites")] = "Food sites"
res_ca_az$Pred[which(res_ca_az$Pred=="SMI")] = "Body condition (as SMI)"
res_ca_az$Pred[which(res_ca_az$Pred=="Group.Size")] = "Group size" 
res_ca_az$Pred[which(res_ca_az$Pred=="History")] = "Captivity History"

res_ca_az$Pred[which(res_ca_az$Pred=="Duration")] = "Duration near"   
res_ca_az$Pred[which(res_ca_az$Pred=="Latency")] = "Latency to approach"     

res_ca_az$Type = ifelse(res_ca_az$Pred %in% c("Duration near", "Latency to approach"), "Experimental\n measures", "Additional\n measures")
res_ca_az$Outcome = ifelse(res_ca_az$Outcome %in% c("MeanLFV"), "Mean of log movement velocity", "SD of log movement velocity")

honey_pal = plvs_vltra("honey_pot", rev=FALSE)
cloud_pal = plvs_vltra("summer_clouds", rev=FALSE)

 res_out_preds = ggplot(res_ca_az, aes(M, Pred)) +
 geom_vline(xintercept=0, linetype="dashed")+
  geom_linerange(
    aes(y = Pred, xmin = L, xmax = H, group = Site, color = Site), linewidth = 2, 
    position = position_dodge(0.5)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.5), size = 3
    )+
  scale_color_manual(values = c(honey_pal[1], cloud_pal[2])) +
  xlab("") + ylab("")  + theme(legend.position="bottom") + theme(text=element_text(size=18)) +
  facet_grid(Type ~ Outcome,  scales = "free", space='free_y', switch="y") +  scale_y_discrete(position = "right")
  
       
###### plot
 d_all.az$Site = "AZ"
 d_all.ca$Site = "CA"
 d_all.az_sorted = d_all.az[order(d_all.az$MeanLFV),]
 d_all.ca_sorted = d_all.ca[order(d_all.ca$MeanLFV),]

 d_all.az_sorted$ID = 1:nrow(d_all.az_sorted)
 d_all.ca_sorted$ID = 1:nrow(d_all.ca_sorted)

 d_all.sv_sorted = rbind(d_all.az_sorted, d_all.ca_sorted)

 d_all.sv_sorted$M = (d_all.sv_sorted$MeanLFV)
 d_all.sv_sorted$L = (d_all.sv_sorted$MeanLFV - 2*d_all.sv_sorted$SigmaLFV)
 d_all.sv_sorted$H = (d_all.sv_sorted$MeanLFV + 2*d_all.sv_sorted$SigmaLFV)

# Plot bird-level velocity
res_out_sv = ggplot(d_all.sv_sorted, aes(ID, M)) +
  geom_linerange(
    aes(x = ID, ymin = L, ymax = H, group = Site, color = Site), linewidth = 2, 
    position = position_dodge(0.85)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.85), size = 3
    )+
   scale_color_manual(values = c(honey_pal[1], cloud_pal[2])) +
  xlab("Bird ID (sorted, within sites)") + ylab("Log movement velocity") + theme(legend.position="bottom") + theme(text=element_text(size=18))


 combined_sv_plot = res_out_sv + res_out_preds + plot_layout(widths = c(1, 1.5))

ggsave("Results_Log_Velocity.pdf", combined_sv_plot, height=7, width=15)

write.csv(res_ca_az, "Search_Velocity_Results.csv")


fit_lfv_m = lm(MeanLFV ~ Site + Sex + History + Season2, data=d_all.sv_sorted)
write.csv(round(cbind(coef(fit_lfv_m),confint(fit_lfv_m)),3),"res_lfv_m.csv")

fit_lfv_sd = lm(SigmaLFV ~ Site + Sex + History + Season2, data=d_all.sv_sorted)
write.csv(round(cbind(coef(fit_lfv_sd),confint(fit_lfv_sd)),3),"res_lfv_sd.csv")
