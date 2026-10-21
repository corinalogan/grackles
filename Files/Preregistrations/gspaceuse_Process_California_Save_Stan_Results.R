########################################## Save Stan parameter estimates
results_ca = matrix(NA,nrow=9, ncol=7)
colnames(results_ca) = c("Variable",names(precis(m1ca,depth=2,pars="Beta")))
results_ca[1,] = c(colnames(covariates)[1+1],c(t(precis(m1ca,depth=2,pars="Beta")[2,])))
results_ca[2,] = c(colnames(covariates)[2+1],c(t(precis(m2ca,depth=2,pars="Beta")[3,])))
results_ca[3,] = c(colnames(covariates)[3+1],c(t(precis(m3ca,depth=2,pars="Beta")[4,])))
results_ca[4,] = c(colnames(covariates)[4+1],c(t(precis(m4ca,depth=2,pars="Beta")[5,])))
results_ca[5,] = c(colnames(covariates)[5+1],c(t(precis(m5ca,depth=2,pars="Beta")[6,])))
results_ca[6,] = c(colnames(covariates)[6+1],c(t(precis(m6ca,depth=2,pars="Beta")[7,])))
results_ca[7,] = c(colnames(covariates)[7+1],c(t(precis(m7ca,depth=2,pars="Beta")[8,])))
results_ca[8,] = c(colnames(covariates)[8+1],c(t(precis(m8ca,depth=2,pars="Beta")[9,])))
results_ca[9,] = c(colnames(covariates)[9+1],c(t(precis(m9ca,depth=2,pars="Beta")[10,])))
results_ca

results_ca = data.frame(results_ca)
for(i in 2:7){
  results_ca[,i] = as.numeric(results_ca[,i])
}

results_ca$Site = "CA"


########################################## Export inferred suitability based on intercept-only model
########################################################################################## Density map
######################## Build the space-use matrix 
mat = matrix(log(matrix(get_posterior_mean(m0ca,pars="Suitability"), nrow=66, ncol=66)), nrow = 66, ncol = 66)

######################## Reshape to long format for ggplot
mat_df = melt(mat, varnames = c("Row", "Col"), value.name = "Value")

######################## Plot
post3ca = ggplot(mat_df, aes(x = -Col, y = Row, fill = Value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(d) California Posterior Mean Suitabilities",
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

 p3ca2 = p3ca + labs(
    title = "(c) In-Sample California Gridded Densities",
    subtitle = "Cell color reflects space-use rate as log of GPS point counts",
    x = "Longitude",
    y = "Latitude"
  )

 combined_CA_su = p3ca2 + post3ca

combined_CA_su
