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
pdf("CA_Suitability.pdf",height=8,width=8)
imageF(log(matrix(m0ca$summary("Suitability", "mean"), nrow=58, ncol=58))) # Overall
dev.off()

