######################## Merge AZ and CA data
res_ca_az = rbind(res_ca, res_az)

res_out_preds = ggplot(res_ca_az[which(res_ca_az$Outcome=="MeanLFV"),], aes(Pred, M)) +
 geom_hline(yintercept=0, linetype="dashed")+
  geom_linerange(
    aes(x = Pred, ymin = L, ymax = H, group = Site, color = Site), linewidth = 2, alpha=0.5,
    position = position_dodge(0.5)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.5), size = 3
    )+
  scale_color_manual(values = c("darkcyan", "darkgoldenrod2")) +
  xlab("Predictor variable") + ylab("Slope coefficient") + coord_flip() + theme(legend.position="bottom") + theme(text=element_text(size=18))
  

ggsave("Preds_Mean_Log_Velocity.pdf",res_out_preds,height=5,width=5)


res_out_preds = ggplot(res_ca_az[which(res_ca_az$Outcome=="SigmaLFV"),], aes(Pred, M)) +
 geom_hline(yintercept=0,linetype="dashed")+
  geom_linerange(
    aes(x = Pred, ymin = L, ymax = H, group = Site, color = Site), linewidth = 2, alpha=0.5,
    position = position_dodge(0.5)
    )+
  geom_point(
    aes(color = Site),
    position = position_dodge(0.5), size = 3
    )+
  scale_color_manual(values = c("darkcyan", "darkgoldenrod2")) +
  xlab("Predictor variable") + ylab("Slope coefficient") + coord_flip() + theme(legend.position="bottom") + theme(text=element_text(size=18))

ggsave("Preds_SD_Log_Velocity.pdf",res_out_preds,height=5,width=5)


write.csv(res_ca_az, "Search_Velocity_Results.csv")
