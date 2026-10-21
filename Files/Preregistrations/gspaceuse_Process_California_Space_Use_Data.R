######################## CA GPS Limits
 NW = c(38.46750000, -121.502478)
 NE = c(38.46750000, -121.479000)
 SE = c(38.45000000, -121.479000)
 SW = c(38.45000000, -121.502478)

 LatLim = c(SE[1],NE[1])
 LongLim = c(NE[2],NW[2])

# Subset to region with dense data
 d_ucd = d[which(d$Latitude>LatLim[1] & d$Latitude<LatLim[2] & d$Longitude<LongLim[1] & d$Longitude>LongLim[2]),]

######################## Boundary polygon (for a clean outline instead of 4 separate segments)
boundary = data.frame(
  Longitude = c(NW[2], NE[2], SE[2], SW[2], NW[2]),
  Latitude  = c(NW[1], NE[1], SE[1], SW[1], NW[1])
)

######################## Plot
honey_pal = plvs_vltra("honey_pot", rev=FALSE)

p1ca = ggplot() +
  geom_point(data = d, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = "grey65") +
  geom_point(data = d_ucd, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = honey_pal[1]) +  
  geom_path(data = boundary, aes(x = Longitude, y = Latitude),
            color = "#1d3557", linewidth = 0.7) +
  labs(
    title = "(d) All California GPS Observations",
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

ggsave("CA_full_map.pdf", plot = p1ca, height = 8, width = 8)


####################### Now, use 2D binning to count GPS points per bird in each grid-cell
# First prepare variables
nbins = 66
 # (66^2)/(2.04*1.94)
 # 1100.667 gridcells per kmsq
 

 birds = c("Bacmut", "Bunuelo", "Camote", "Cuervo", "Cutuy", "Dulce", 
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

 results[,,n] = t(bin_movement_tracks(tracks, nbin = c(nbins, nbins), ab_override= matrix(rbind(LatLim,LongLim), nrow=2, ncol=2)))
}

# Now plot the zoomed in CA map, and the density estimates, to ensure that 2D binning worked correctly
p2ca = ggplot() +
  geom_point(data = d_ucd, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = "grey65") +
  geom_point(data = d_birds_ucd, aes(x = Longitude, y = Latitude),
             size = 0.3, alpha = 0.99, color = honey_pal[1]) +  
  geom_path(data = boundary, aes(x = Longitude, y = Latitude),
            color = "#1d3557", linewidth = 0.7) +
  labs(
    title = "(e) In-Sample California GPS Observations",
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

ggsave("CA_sub_map.pdf", plot = p2ca, height = 8, width = 8)

########################################################################################## Density map
######################## Build the space-use matrix 
mat = matrix(log(1 + apply(results, 1, sum, na.rm = TRUE)), nrow = nbins, ncol = nbins)

######################## Reshape to long format for ggplot
mat_df = melt(mat, varnames = c("Row", "Col"), value.name = "Value")

######################## Plot
p3ca = ggplot(mat_df, aes(x = -Col, y = Row, fill = Value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(f) In-Sample California Gridded Densities",
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

ggsave("CA_density_map.pdf", plot = p3ca, height = 8, width = 8)


combined_CA = p1ca + p2ca + p3ca
ggsave("CA_combined_maps.pdf", plot = combined_CA, height = 6, width = 18)



