########################################## Save Stan parameter estimates
results_asu = matrix(NA,nrow=9, ncol=7)
colnames(results_asu) = c("Variable",names(precis(m1,depth=2,pars="Beta")))
results_asu[1,] = c(colnames(covariates)[1+1],c(t(precis(m1,depth=2,pars="Beta")[2,])))
results_asu[2,] = c(colnames(covariates)[2+1],c(t(precis(m2,depth=2,pars="Beta")[3,])))
results_asu[3,] = c(colnames(covariates)[3+1],c(t(precis(m3,depth=2,pars="Beta")[4,])))
results_asu[4,] = c(colnames(covariates)[4+1],c(t(precis(m4,depth=2,pars="Beta")[5,])))
results_asu[5,] = c(colnames(covariates)[5+1],c(t(precis(m5,depth=2,pars="Beta")[6,])))
results_asu[6,] = c(colnames(covariates)[6+1],c(t(precis(m6,depth=2,pars="Beta")[7,])))
results_asu[7,] = c(colnames(covariates)[7+1],c(t(precis(m7,depth=2,pars="Beta")[8,])))
results_asu[8,] = c(colnames(covariates)[8+1],c(t(precis(m8,depth=2,pars="Beta")[9,])))
results_asu[9,] = c(colnames(covariates)[9+1],c(t(precis(m9,depth=2,pars="Beta")[10,])))
results_asu

results_asu = data.frame(results_asu)
for(i in 2:7){
  results_asu[,i] = as.numeric(results_asu[,i])
}

results_asu$Site = "AZ"

########################################## Export inferred suitability based on intercept-only model
########################################################################################## Density map
######################## Build the space-use matrix 
mat = matrix(log(matrix(get_posterior_mean(m0,pars="Suitability"), nrow=71, ncol=71)), nrow = 71, ncol = 71)

######################## Reshape to long format for ggplot
mat_df = melt(mat, varnames = c("Row", "Col"), value.name = "Value")

######################## Plot
post3az = ggplot(mat_df, aes(x = -Col, y = Row, fill = Value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(b) Arizona Posterior Mean Suitabilities",
    subtitle = "Cell color reflects space-use rate as log of time percentage",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey40", size = 11, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

 p3az2 = p3az + labs(
    title = "(a) In-Sample Arizona Gridded Densities",
    subtitle = "Cell color reflects space-use rate as log of GPS point counts",
    x = "Longitude",
    y = "Latitude"
  )

 combined_AZ_su = p3az2 + post3az

combined_AZ_su
