########################################## Load functions 
# Load a little helper to flip image plots 
imageF = function(m){
    m = m[,nrow(m):1]
    image(m, xlab="Longitude", ylab="Latitude")
    }

# Load a little helper to standardize variable, 
# and impute missings using the mean value
normalize = function(x){
    x2 = as.numeric(as.character(x))
    x2[is.na(x2)] = mean(x2, na.rm=TRUE)
    y = (x2-mean(x2))/sd(x2)
    return(y)
 }

# Make results from lm objects
 make_res = function(a,b,x){
    return(c(a,b,x$coef[2], confint(x)[2,1], confint(x)[2,2]))
 }

# Get foraging velocity from AZ data set
get_foraging_velocity = function(d, BN, DD){
 d_scrap = d[which(d$Bird.Name==BN & d$Date==DD), ]
  if(length(d_scrap$Time)>1){
   d_scrap$dx = NA
   d_scrap$dt = NA
   d_scrap$fv = NA
   
   for(i in 2:length(d_scrap$Date)){
    d_scrap$dx[i] = distm(rev(d_scrap[i,5:6]), rev(d_scrap[i-1,5:6]), fun = distHaversine)
    d_scrap$dt[i] = difftime(
                 parse_date_time(paste(d_scrap$Time[i]), c('%H:%M:%S','%H:%M')),
                 parse_date_time(paste(d_scrap$Time[i-1]), c('%H:%M:%S','%H:%M')),
                 units = "mins")
    d_scrap$fv[i] = d_scrap$dx[i]/d_scrap$dt[i]
     }

   if(length(d_scrap$fv[which(d_scrap$dt>0)])>0){
    FV = data.frame(Bird=BN, Date = DD, FV = d_scrap$fv[which(d_scrap$dt>0)], DX = d_scrap$dx[which(d_scrap$dt>0)], DT = d_scrap$dt[which(d_scrap$dt>0)])
   return(FV)
     }
     }
}

# Get foraging velocity from CA data set
get_foraging_velocity_ca = function(d, BN, DD){
 d_scrap = d[which(d$Bird.Name==BN & d$Date==DD), ]
  if(length(d_scrap$Time)>1){
   d_scrap$dx = NA
   d_scrap$dt = NA
   d_scrap$fv = NA

   for(i in 2:length(d_scrap$Date)){
    d_scrap$dx[i] = distm(rev(d_scrap[i,6:7]), rev(d_scrap[i-1,6:7]), fun = distHaversine)
    d_scrap$dt[i] = difftime(
                 parse_date_time(paste(d_scrap$Time[i]), '%H:%M:%S'),
                 parse_date_time(paste(d_scrap$Time[i-1]), '%H:%M:%S'),
                 units = "mins")
      d_scrap$fv[i] = d_scrap$dx[i]/d_scrap$dt[i]
        }

   if(length(d_scrap$fv[which(d_scrap$dt>0)])>0){
    FV = data.frame(Bird=BN, Date = DD, FV = d_scrap$fv[which(d_scrap$dt>0)], DX = d_scrap$dx[which(d_scrap$dt>0)], DT = d_scrap$dt[which(d_scrap$dt>0)])
    return(FV)
    }
   }
}

### For space use analysis
library(ash)
gracklebinner = function (tracks, nbin = c(15, 15), ab_override = NULL) 
{
  Trips <- length(tracks)
  
  GrackBins <- matrix(NA, nrow = Trips, ncol = nbin[1] * nbin[2])
  
  bins <- bin2(as.matrix(do.call(rbind,tracks)), nbin = nbin)
  
  
  
  if (length(dim(ab_override)) == 0) {
    for (i in 1:Trips) {
      if(length(tracks[[i]]$X)>0){
        GrackBins[i, ] <- c(bin2(cbind(tracks[[i]]$X, tracks[[i]]$Y), 
                                 nbin = nbin, ab = bins$ab)$nc)
      }
    }
  } else {
    for (i in 1:Trips) {
      if(length(tracks[[i]]$X)>0){
        GrackBins[i, ] <- c(bin2(cbind(tracks[[i]]$X, tracks[[i]]$Y), 
                                 nbin = nbin, ab = ab_override)$nc)
      }
    }
  }
  
  return(GrackBins)
}
