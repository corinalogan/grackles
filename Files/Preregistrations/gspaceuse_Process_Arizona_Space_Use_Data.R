######################## ASU GPS Limits
 NW = c(33.425868, -111.939172)
 NE = c(33.425868, -111.9135225)
 SW = c(33.411756, -111.939137)
 SE = c(33.411791, -111.9135268) 

 LatLim = c(SW[1],NW[1])
 LongLim = c(NE[2],NW[2])

######################## Subset data to ASU limits
 d <- read.csv(url("https://raw.githubusercontent.com/corinalogan/grackles/refs/heads/master/Files/Preregistrations/gspaceuse_AZgracklePtsAviaryByWeek_new.csv"), 
                  header = T, sep = ",", stringsAsFactors = F)
 d_asu = d[which(d$Latitude>LatLim[1] & d$Latitude<LatLim[2] & d$Longitude<LongLim[1] & d$Longitude>LongLim[2]),]

# Plot the full map with in-sample data highlighted
pdf("AZ_full_map.pdf",height=8,width=8)
 plot(d$Latitude ~ d$Longitude, pch=".", xlab="Longitude", ylab="Latitude")
 points(d_asu$Latitude ~ d_asu$Longitude, col="red", pch=".")

 points(SW[1] ~ SW[2], col="blue", pch=18)
 segments(SW[2],SW[1], NW[2],NW[1], col="blue")

 points(NW[1] ~ NW[2], col="green", pch=18)
 segments(NW[2],NW[1], NE[2],NE[1], col="green")

 points(SE[1] ~ SE[2], col="purple", pch=18)
 segments(SE[2],SE[1], SW[2],SW[1], col="purple")

 points(NE[1] ~ NE[2], col="orange", pch=18)
 segments(NE[2],NE[1], SE[2],SE[1], col="orange")
 
 dev.off()


####################### Now, use 2D binning to count GPS points per bird in each grid-cell
# First prepare variables
 nbins = 71
 # (71^2)/(2.4*1.6)
 # 1312.76 gridcells per kmsq

 birds = c("Adobo", "Burrito", "Chalupa","Chilaquile", "Chile", "Diablo","Fideo", "Habanero", "Marisco", "Mofongo", 
           "Mole", "Pizza", "Pollito", "Queso", "Taco","Tapa", "Taquito", "Tomatillo", "Yuca")

 nbirds = length(birds)
 d_birds = d_asu[which(d_asu$Bird.Name %in% birds),]

 ndays = length(unique(d_birds$bird.week))
 days = unique(d_birds$bird.week)

 results = array(0,c(nbins^2, ndays, nbirds))

 d_birds_asu = d_birds[which(d_birds$Latitude>LatLim[1] & d_birds$Latitude<LatLim[2] & d_birds$Longitude<LongLim[1] & d_birds$Longitude>LongLim[2]),]

# Now fill in data, bird by bird
for(n in 1:nbirds){
 d_focal = d_birds_asu[which(d_birds_asu$Bird.Name==birds[n]),]

 tracks = vector("list", ndays)

 for(i in 1:ndays){
    tracks[[i]] = data.frame(X=d_focal$Latitude[which(d_focal$bird.week==days[i])],
                             Y=d_focal$Longitude[which(d_focal$bird.week==days[i])]
                             )
                    }

 results[,,n] = t(gracklebinner(tracks, nbin = c(nbins, nbins), ab_override= matrix(rbind(LatLim,LongLim),nrow=2,ncol=2))) # gracklebinner function code in Helper_Functions.R
}

# Now plot the zoomed in AZ map, and the density estimates, to ensure that 2D binning worked correctly
pdf("AZ_sub_map.pdf",height=8,width=8)
plot(d_asu$Latitude , d_asu$Longitude, pch=".",xlab="Longitude", ylab="Latitude")
points(d_birds_asu$Latitude, d_birds_asu$Longitude, col="red", pch=".")
dev.off()

pdf("AZ_density_map.pdf",height=8,width=8)
imageF(log(1+matrix(apply(results, 1, sum, na.rm=TRUE), nrow=nbins, ncol=nbins))) # Overall
dev.off()

