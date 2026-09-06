################### ASU GPS Limits
 NW = c(33.427868, -111.939172)
 NE = c(33.427868, -111.9135225)
 SW = c(33.411756, -111.939137)
 SE = c(33.411791, -111.9135268) 

 LatLim = c(SW[1],NW[1])
 LongLim = c(NE[2],NW[2])

######################## Subset data to ASU limits
 d_asu = d[which(d$Latitude>LatLim[1] & d$Latitude<LatLim[2] & d$Longitude<LongLim[1] & d$Longitude>LongLim[2]),]

######################## Boundary polygon (for a clean outline instead of 4 separate segments)
boundary = data.frame(
  Longitude = c(NW[2], NE[2], SE[2], SW[2], NW[2]),
  Latitude  = c(NW[1], NE[1], SE[1], SW[1], NW[1])
)

######################## Plot
honey_pal = plvs_vltra("honey_pot", rev=FALSE)

p1az = ggplot() +
  geom_point(data = d, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = "grey65") +
  geom_point(data = d_asu, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = honey_pal[1]) +  
  geom_path(data = boundary, aes(x = Longitude, y = Latitude),
            color = "#1d3557", linewidth = 0.7) +
  labs(
    title = "(a) All Arizona GPS Observations",
    subtitle = "Orange points fall within our sample set",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey40", size = 11, margin = margin(b = 12)),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "grey90", linewidth = 0.3),
    axis.title = element_text(color = "grey30"),
    plot.background = element_rect(fill = "white", color = NA)
  ) +
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
 )

ggsave("AZ_full_map.pdf", plot = p1az, height = 8, width = 8)


####################### Now, use 2D binning to count GPS points per bird in each grid-cell
# First prepare variables
 nbins = 71
 # (71^2)/(2.38*1.79)
 # 1183.278 gridcells per kmsq

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

 results[,,n] = t(bin_movement_tracks(tracks, nbin = c(nbins, nbins), ab_override= matrix(rbind(LatLim,LongLim),nrow=2,ncol=2)))
}

# Now plot the zoomed in AZ map, and the density estimates, to ensure that 2D binning worked correctly
p2az = ggplot() +
  geom_point(data = d_birds, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = "grey65") +
  geom_point(data = d_birds_asu, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = honey_pal[1]) +  
  geom_path(data = boundary, aes(x = Longitude, y = Latitude),
            color = "#1d3557", linewidth = 0.7) +
  labs(
    title = "(b) In-Sample Arizona GPS Observations",
    subtitle = "Zoomed on the bounding box to the left",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey40", size = 11, margin = margin(b = 12)),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "grey90", linewidth = 0.3),
    axis.title = element_text(color = "grey30"),
    plot.background = element_rect(fill = "white", color = NA)
  ) + 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

ggsave("AZ_sub_map.pdf", plot = p2az, height = 8, width = 8)


########################################################################################## Density map
######################## Build the space-use matrix 
mat = matrix(log(1 + apply(results, 1, sum, na.rm = TRUE)), nrow = nbins, ncol = nbins)

######################## Reshape to long format for ggplot
mat_df = melt(mat, varnames = c("Row", "Col"), value.name = "Value")

######################## Plot
p3az = ggplot(mat_df, aes(x = -Col, y = Row, fill = Value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(c) In-Sample Arizona Gridded Densities",
    subtitle = "Cell color reflects space-use rate",
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

ggsave("AZ_density_map.pdf", plot = p3az, height = 8, width = 8)


combined_AZ = p1az + p2az + p3az
ggsave("AZ_combined_maps.pdf", plot = combined_AZ, height = 6, width = 18)