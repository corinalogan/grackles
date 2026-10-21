functions{
  real Entropy(vector X, int N){
    vector[N] Y;

    for(i in 1:N){
      if(X[i] == 0)
      Y[i] = 0;
      else
      Y[i] = X[i]*log(X[i]);
    }

    return(-sum(Y));
  }

  vector to_vector_normalized (array[] int X){
    return to_vector(X)/sum(to_vector(X));
  }
}

data{
    int n_days;
    int n_birds;
    int n_bins;
    int n_estimates;
    array[n_estimates, 2] int estimate_locs;
    array[n_days, n_birds] int data_in_day_star;
    array[n_days, n_birds] int data_in_day_use;
    array[n_bins, n_days, n_birds] int Outcomes;
    vector[n_bins] PriorSuitability;
    array[n_birds, 10] real Covariates;
    vector[10] Z;
}

parameters{
    simplex[n_bins] Suitability;
    array[n_birds] real A;
    real<lower=0> SD_A;
    vector[10] Beta;
}

transformed parameters{
 array[n_birds] vector[2] B;

  for(b in 1:n_birds){
    B[b,2] = inv_logit(A[b]*SD_A + sum(Z .* (Beta .* to_vector(Covariates[b]))));
    B[b,1] = 1 - B[b,2];
    }

}

model{
  vector[n_bins] Predictions;
  real H_scrap;

 //  Priors 
   for(b in 1:n_birds){
    A[b] ~ normal(0, 1);
    }

    Beta ~ normal(0, 2.5);

    SD_A ~ exponential(1);

 // Simplex of average prob of residence over birds and days
   Suitability ~ dirichlet(rep_vector(1,n_bins));

 // Now model Dirichlet mixture
   for(i in 1:n_estimates){
    if(estimate_locs[i,1]>1){ // If not the first week
      if(estimate_locs[i,1] - estimate_locs[i-1,1] == 1){ // If one week after last observation

       Predictions = B[estimate_locs[i,2],1]*Suitability + 
                     B[estimate_locs[i,2],2]*to_vector_normalized(Outcomes[, estimate_locs[i-1,1], estimate_locs[i-1,2]]);

       Outcomes[, estimate_locs[i,1], estimate_locs[i,2]] ~ multinomial(Predictions);
    }
  }

}

}
