######################## CA GPS Limits
 NW = c(38.466708134, -121.502478)
 NE = c(38.466708134, -121.480686)
 SE = c(38.4547828, -121.480686)
 SW = c(38.4547828, -121.502478)

 LatLim = c(SE[1],NE[1])
 LongLim = c(NE[2],NW[2])

 d <- read.csv(url("https://raw.githubusercontent.com/corinalogan/grackles/refs/heads/master/Files/Preregistrations/gspaceuse_CAgracklePtsAviaryByWeek_new.csv"), 
                  header = T, sep = ",", stringsAsFactors = F)
 
# Subset to region with dense data
 d_ucd = d[which(d$Latitude>LatLim[1] & d$Latitude<LatLim[2] & d$Longitude<LongLim[1] & d$Longitude>LongLim[2]),]

# Plot the full map with in-sample data highlighted
pdf("CA_full_map.pdf",height=8,width=8)
 plot(d$Latitude ~ d$Longitude, pch=".", xlab="Longitude", ylab="Latitude") #, ylim=c(38.43,38.48))
 points(d_ucd$Latitude ~ d_ucd$Longitude, col="red", pch=".")

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
nbins = 58
 # (58^2)/(1.3*1.9)
 # 1361.943 gridcells per kmsq
 
# 24 Bird IDs with all data from step length analysis:
# "Akxi"       "Bacmut"     "Bunuelo"    "Camote"     "Churro"     "Cuervo"     "Cutuy"      "Dulce"      "Galandra"   "Helado"    
# "Kau"        "Kel"        "Pina"       "Polvorones" "Quiscalus"  "Sopapilla"  "Talingo"    "Tembleque"  "Tzanatl"    "Urraca"    
# "Wachil"     "Xango"      "Xunub"      "Zapote"   

# but cannot include Akxi because he was in Woodland - outside the GPS region with dense data
 birds = c("Bacmut", "Bunuelo", "Camote", "Churro", "Cuervo", "Cutuy", "Dulce", 
            "Galandra", "Helado", "Kau", "Kel", "Pina", "Polvorones", "Quiscalus", 
            "Sopapilla", "Talingo", "Tembleque", "Tzanatl", "Urraca", "Wachil", 
            "Xango", "Xunub", "Zapote")
 nbirds = length(birds)
 d_birds_ucd = d_ucd[which(d_ucd$Bird.Name %in% birds),]

 ndays = length(unique(d_birds_ucd$bird.week))
 days = unique(d_birds_ucd$bird.week)

 results = array(0,c(nbins^2, ndays, nbirds))

####################### Parameters and results array
for(n in 1:nbirds){
 d_focal = d_birds_ucd[which(d_birds_ucd$Bird.Name==birds[n]),]

 tracks = vector("list", ndays)

 for(i in 1:ndays){
    tracks[[i]] = data.frame(X=d_focal$Latitude[which(d_focal$bird.week==days[i])],
                             Y=d_focal$Longitude[which(d_focal$bird.week==days[i])]
                             )
                    }

 results[,,n] = t(gracklebinner(tracks, nbin = c(nbins, nbins), ab_override= matrix(rbind(LatLim,LongLim),nrow=2,ncol=2)))
}

# Now plot the zoomed in CA map, and the density estimates, to ensure that 2D binning worked correctly
pdf("CA_sub_map.pdf",height=8,width=8)
plot(d_ucd$Latitude , d_ucd$Longitude,pch=".", xlab="Longitude", ylab="Latitude")
points(d_birds_ucd$Latitude, d_birds_ucd$Longitude, col="red", pch=".")
dev.off()

pdf("CA_density_map.pdf",height=8,width=8)
imageF(log(1+matrix(apply(results, 1, sum, na.rm=TRUE), nrow=nbins, ncol=nbins))) # Overall
dev.off()


