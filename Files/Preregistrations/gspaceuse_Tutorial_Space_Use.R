# Load library and attach data
library(grackleator)
library(rstan)
library(cmdstanr)
library(PlvsVltra)
library(patchwork)

# Simulate tracks from 1 grackle over 50 trips
z = grackleate(AlphaDist=4.0, AlphaAngle=0, SDDist=1.6, DAngle=1.1, steps = 100, seed = 714, Reps = 5, BetaDist = seq(-2.1, 0, length.out=10), BetaAngle = seq(0.9, 0, length.out=10))

# Bin data on 2D grid
D = 30
grackle_bins = bin_movement_tracks(matrix_to_list(z), ab_override=matrix(c(-3000,-3000,3000,3000), nrow=2, ncol=2),nbin = c(D, D))

X_locs = cbind(z$food_locs_X, z$food_locs_X, z$food_locs_X, z$food_locs_X, z$food_locs_X)
Y_locs = cbind(z$food_locs_Y, z$food_locs_Y, z$food_locs_Y, z$food_locs_Y, z$food_locs_Y)
z_food = list(X=X_locs, Y=Y_locs)

food_bins = bin_movement_tracks(matrix_to_list(z_food), ab_override=matrix(c(-3000,-3000,3000,3000), nrow=2, ncol=2),nbin = c(D, D))

# Plot environmental hotspots
image(matrix(colSums(food_bins), nrow=D, ncol=D)) # Overall
image(matrix(grackle_bins[1,], nrow=D, ncol=D)) # Day 1
image(matrix(grackle_bins[2,], nrow=D, ncol=D)) # Day 2
image(matrix(grackle_bins[3,], nrow=D, ncol=D)) # Day 3

mask = matrix(0, nrow=D, ncol=D)
mask[1:9, 1:9] = 1                    # Both birds will start using space on day d=1 in this region

# Now create data with temporal correlations
grackle_bins2a = grackle_bins2b = grackle_bins
grackle_bins2a[1,] = grackle_bins2b[1,] = rmultinom(1, 50, colSums(food_bins)*c(mask)) # Create a day d-1 inital state of space use purposefully
A = colSums(food_bins)
A = A/sum(A)
B = 0.1

NN = 50

for(i in 2:5)
grackle_bins2a[i,] = rmultinom(1, NN, A*(1-B) + B*(grackle_bins2a[i-1,]/sum(grackle_bins2a[i-1,])))

########################################################################################## Density map
######################## Build the space-use matrix 
mat_df = melt(matrix(colSums(food_bins), nrow=D, ncol=D), varnames = c("Row", "Col"), value.name = "value")

######################## Plot
tut1a = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(a) Gridded Overall Suitability",
    subtitle = "Cell color reflects base-line space-use rate",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

######################## Plot
tut2a = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(e) Gridded Overall Suitability",
    subtitle = "Cell color reflects base-line space-use rate",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

######################## Build the space-use matrix 
mat_df = melt(matrix(grackle_bins2a[1,], nrow=D, ncol=D), varnames = c("Row", "Col"), value.name = "value")

######################## Plot
tut1b = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(b) Space-use rates in week: w",
    subtitle = "(alpha=0.1)",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

#################### Build the space-use matrix 
mat_df = melt(matrix(grackle_bins2a[2,], nrow=D, ncol=D), varnames = c("Row", "Col"), value.name = "value")

######################## Plot
tut1c = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(c) Space-use rates in week: w+1",
    subtitle = "(alpha=0.1)",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

#################### Build the space-use matrix 
mat_df = melt(matrix(grackle_bins2a[3,], nrow=D, ncol=D), varnames = c("Row", "Col"), value.name = "value")

######################## Plot
tut1d = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(d) Space-use rates in week: w+2",
    subtitle = "(alpha=0.1)",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)


full_grid_1 = tut1a + tut1b + tut1c + tut1d 


# Now create data with temporal correlations
A = colSums(food_bins)
A = A/sum(A)
B = 0.9

for(i in 2:50)
grackle_bins2b[i,] = rmultinom(1, NN, A*(1-B) + B*(grackle_bins2b[i-1,]/sum(grackle_bins2b[i-1,])))

######################## Build the space-use matrix 
mat_df = melt(matrix(grackle_bins2b[1,], nrow=D, ncol=D), varnames = c("Row", "Col"), value.name = "value")

######################## Plot
tut2b = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(f) Space-use rates in week: w",
    subtitle = "(alpha=0.9)",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

#################### Build the space-use matrix 
mat_df = melt(matrix(grackle_bins2b[2,], nrow=D, ncol=D), varnames = c("Row", "Col"), value.name = "value")

######################## Plot
tut2c = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(g) Space-use rates in week: w+1",
    subtitle = "(alpha=0.9)",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

#################### Build the space-use matrix 
mat_df = melt(matrix(grackle_bins2b[3,], nrow=D, ncol=D), varnames = c("Row", "Col"), value.name = "value")

######################## Plot
tut2d = ggplot(mat_df, aes(x = -Col, y = Row, fill = value)) +
  geom_raster() +
  scale_fill_gradientn(
    colors = plvs_vltra("honey_pot",rev=TRUE),
    name = "Log-usage rate"
  )+
  coord_equal() +
  labs(
    title = "(h) Space-use rates in week: w+2",
    subtitle = "(alpha=0.9)",
    x = "Longitude",
    y = "Latitude"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16, margin = margin(b = 4)),
    plot.subtitle = element_text(color = "grey10", size = 14, margin = margin(b = 12)),
    panel.grid = element_blank(),
    axis.text = element_blank(),
    legend.title = element_text(size = 10),
    plot.background = element_rect(fill = "white", color = NA)
  )+ 
  theme(
  plot.title.position = "plot",
  plot.caption.position = "plot"
)

  full_grid_1 = (tut1a + tut1b + tut1c + tut1d) + plot_layout(nrow = 1)
  full_grid_2 = (tut2a + tut2b + tut2c + tut2d) + plot_layout(nrow = 1)

  full_grid = full_grid_1 / full_grid_2

  full_grid 

ggsave("SpaceUse_Explainer.pdf", plot = full_grid, height = 9, width = 18)
