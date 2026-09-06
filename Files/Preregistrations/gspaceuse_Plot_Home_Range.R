HR = read.csv(url("https://raw.githubusercontent.com/corinalogan/grackles/refs/heads/master/Files/Preregistrations/gspaceuse_HRdataSheet.csv"), header=T, sep=",", stringsAsFactors=F)
HR$Season2 = ifelse(HR$Season_ratio > 0.5, "Breeding", "Non-breeding")

HR$hr = log(HR$hr)

HR_CA = HR[which(HR$Site=="CA"),]
HR_AZ = HR[which(HR$Site=="AZ"),]

HR_CA$Latency = normalize(HR_CA$Latency)
HR_CA$Duration = normalize(HR_CA$Duration)
HR_CA$History = normalize(HR_CA$History)
HR_CA$Breeding.Sites = normalize(HR_CA$Breeding.Sites)
HR_CA$Food.Sites = normalize(HR_CA$Food.Sites)    
HR_CA$SMI = normalize(HR_CA$SMI)
HR_CA$Group.Size = normalize(HR_CA$Group.Size)
HR_CA$Sex = ifelse(HR_CA$Sex == "M", 1, 0)
HR_CA$Season2 = ifelse(HR_CA$Season2 == "Breeding", 1, 0)

HR_AZ$Latency = normalize(HR_AZ$Latency)
HR_AZ$Duration = normalize(HR_AZ$Duration)
HR_AZ$History = normalize(HR_AZ$History)
HR_AZ$Breeding.Sites = normalize(HR_AZ$Breeding.Sites)
HR_AZ$Food.Sites = normalize(HR_AZ$Food.Sites)    
HR_AZ$SMI = normalize(HR_AZ$SMI)
HR_AZ$Group.Size = normalize(HR_AZ$Group.Size)
HR_AZ$Sex = ifelse(HR_AZ$Sex == "M", 1, 0)
HR_AZ$Season2 = ifelse(HR_AZ$Season2 == "Breeding", 1, 0)


res_hr_az = res_hr_ca = data.frame(Site="HR", Pred="Vars", M=1.1, L=1.1, H=1.1)
res_hr_az[1,] = make_res("AZ", "Latency", lm(hr~Latency,data=HR_AZ))
res_hr_az[2,] = make_res("AZ", "Duration", lm(hr~Duration,data=HR_AZ))
res_hr_az[3,] = make_res("AZ", "Male", lm(hr~Sex,data=HR_AZ))
res_hr_az[4,] = make_res("AZ", "History", lm(hr~History,data=HR_AZ))
res_hr_az[5,] = make_res("AZ", "Breeding.Sites", lm(hr~Breeding.Sites,data=HR_AZ))
res_hr_az[6,] = make_res("AZ", "Food.Sites", lm(hr~Food.Sites,data=HR_AZ))
res_hr_az[7,] = make_res("AZ", "SMI", lm(hr~SMI,data=HR_AZ))
res_hr_az[8,] = make_res("AZ", "Group.Size", lm(hr~Group.Size,data=HR_AZ))
res_hr_az[9,] = make_res("AZ", "Breeding.Season", lm(hr~Season2,data=HR_AZ))

res_hr_ca[1,] = make_res("CA", "Latency", lm(hr~Latency,data=HR_CA))
res_hr_ca[2,] = make_res("CA", "Duration", lm(hr~Duration,data=HR_CA))
res_hr_ca[3,] = make_res("CA", "Male", lm(hr~Sex,data=HR_CA))
res_hr_ca[4,] = make_res("CA", "History", lm(hr~History,data=HR_CA))
res_hr_ca[5,] = make_res("CA", "Breeding.Sites", lm(hr~Breeding.Sites,data=HR_CA))
res_hr_ca[6,] = make_res("CA", "Food.Sites", lm(hr~Food.Sites,data=HR_CA))
res_hr_ca[7,] = make_res("CA", "SMI", lm(hr~SMI,data=HR_CA))
res_hr_ca[8,] = make_res("CA", "Group.Size", lm(hr~Group.Size,data=HR_CA))
res_hr_ca[9,] = make_res("CA", "Breeding.Season", lm(hr~Season2,data=HR_CA))

res_hr = rbind(res_hr_ca,res_hr_az)

res_hr$M = as.numeric(res_hr$M)
res_hr$H = as.numeric(res_hr$H)
res_hr$L = as.numeric(res_hr$L)

res_hr$Pred[which(res_hr$Pred=="Male")] = "Male (vs. Female)"
res_hr$Pred[which(res_hr$Pred=="Breeding.Season")] = "Breeding season"
res_hr$Pred[which(res_hr$Pred=="Breeding.Sites")] = "Breeding sites"
res_hr$Pred[which(res_hr$Pred=="Food.Sites")] = "Food sites"
res_hr$Pred[which(res_hr$Pred=="SMI")] = "Body condition (as SMI)"
res_hr$Pred[which(res_hr$Pred=="Group.Size")] = "Group size" 
res_hr$Pred[which(res_hr$Pred=="History")] = "Captivity History"

res_hr$Pred[which(res_hr$Pred=="Duration")] = "Duration near"   
res_hr$Pred[which(res_hr$Pred=="Latency")] = "Latency to approach"  

res_hr$Type = ifelse(res_hr$Pred %in% c("Duration near", "Latency to approach"), "Experimental\n measures", "Additional\n measures")
res_hr$Outcome = "Log home-range size"

honey_pal = plvs_vltra("honey_pot", rev=FALSE)
cloud_pal = plvs_vltra("summer_clouds", rev=FALSE)

res_out_preds_hr = ggplot(res_hr, aes(M, Pred)) +
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

  
 HR_CA_sorted = HR_CA[order(HR_CA$hr),] 
 HR_CA_sorted$ID = 1:nrow(HR_CA_sorted)

 HR_AZ_sorted = HR_AZ[order(HR_AZ$hr),] 
 HR_AZ_sorted$ID = 1:nrow(HR_AZ_sorted)

 HR_AZCA_sorted = rbind(HR_AZ_sorted, HR_CA_sorted)

 HR_AZCA_sorted$M = HR_AZCA_sorted$hr

# Plot bird-level velocity
res_out_hr = ggplot(HR_AZCA_sorted, aes(ID, M)) +
  geom_point(
    aes(color = Site),
    position = position_dodge(0.85), size = 3
    )+
   scale_color_manual(values = c(honey_pal[1], cloud_pal[2])) +
  xlab("Bird ID (sorted, within sites)") + ylab("Log home-range size") + theme(legend.position="bottom") + theme(text=element_text(size=18))


 combined_hr_plot = res_out_hr + res_out_preds_hr + plot_layout(widths = c(1, 1))

ggsave("Results_Log_HR.pdf", combined_hr_plot, height=7, width=15)


fit_hr = lm(hr ~ Site + Sex + History + Season2, data=HR_AZCA_sorted)
write.csv(round(cbind(coef(fit_hr),confint(fit_hr)),3),"res_hr.csv")
