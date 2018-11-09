How and why does behavioral flexibility vary across the range of a rapidly expanding species?
================
[Dr. Corina Logan](http://CorinaLogan.com) (Max Planck Institute for Evolutionary Anthropology, <corina_logan@eva.mpg.de>), Carolyn Rowney (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), Luisa Bergeron (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), Dr. Kelsey McCune (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), [Dr. Benjamin Trumble](https://sols.asu.edu/people/benjamin-trumble) (Arizona State University), [Dr. Aaron Blackwell](http://www.anth.ucsb.edu/faculty/blackwell/) (University of California, Santa Barbara), [Dr. Ananias Escalante](http://igem.temple.edu/people/person/c0ca56d9e60be58ca9380514ed8ac51d) (Temple University), [Dr. Maria Pacheco](http://igem.temple.edu/people/person/6417596d4976b9cbfa2a5ba8062ed7b9) (Temple University), [Dr. Dieter Lukas](http://dieterlukas.strikingly.com) (Max Planck Institute for Evolutionary Anthropology)
2018-10-29

``` r
#Make code wrap text so it doesn't go off the page when Knitting to PDF
library(knitr)
opts_chunk$set(tidy.opts=list(width.cutoff=60),tidy=TRUE)
```

### A. STATE OF THE DATA

This preregistration was written prior to collecting any data.

### B. PARTITIONING THE RESULTS

We may publish the results from each hypothesis separately.

### C. HYPOTHESES

The way we define flexibility (individuals change behavior according to changing circumstances using learning from previous experiences) assumes that being flexible will always be associated with the higher fitness payoff (e.g., higher quality food rewards). Therefore, the reasons individuals might not be flexible are 1) there are indirect costs to flexibility (e.g., exploration, risks involved in uncertain choices), 2) individuals live in environments that rarely change or change randomly, or 3) individuals have internal constraints (e.g., not enough energy). Points [1](./g_exploration.Rmd) and [3](./g_withinpop.Rmd) are being tested in different preregistrations. Here we test point 2.

For the purposes of these predictions, the site that is in the middle of their original geographic range (Central America) is the Honduras site. “Edge” is defined based on distance from Central America (i.e., grackles expanded northward into Arizona in the 1960s and Nebraska in the 2000s (the northern edge) (Figure 1).

![Figure 1. The geographic range of the great-tailed grackle with the three field sites marked by (\*). The arrow represents the northward direction of their range expansion. Purple squares represent the percentage of eBird.org birding checklists that report this species (see legend). Map credit: eBird.org.](g_expansionFig1.png)

#### H1: Individuals are more [behaviorally flexible](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md) (measured by reversal learning and switching between options on a multi-access box) near the edge of their geographic range (in the US relative to Honduras) if flexibility is required for range expansion.

**Prediction 1:** There will be a positive association between flexibility (individuals that are faster to reverse preferences on a reversal learning task and who also have lower latencies to switch to solving new loci after previously solved loci become unavailable) a population's proximity to the edge of the geographic range. If this is supported, other variables should also be involved in how such flexibility is achieved. These other variables will be investigated in the hypotheses below.

**P1 alternative 1:** If there no difference in flexibility between the edge and non-edge populations, this could indicate that most individuals are already highly flexible (ceiling effect).

**P1 alternative 2:** If there is a negative correlation or no difference in flexibility between the edge and non-edge populations, this suggests that other variables might play a larger role than flexibility in how this species is able to rapidly expand its geographic range (see hypotheses below).

#### H2: Grackles in populations in the US will subsist more on human foods and less on wild foods than those in Honduras.

**P2:** The grackle's geographic expansion may be facilitated by human expansion and the ability to supplement or replace wild foraged foods with human food waste and other products (Wehtje (2003)).

**P2 alternative 1:** There is no difference between sites in reliance on human foods, due either to a preference for human foods that exists across all sites, or an ability of grackles to flexibly forage at all sites.

#### H3: Populations closer to the range edge will have lower testosterone.

**P3:** Grackles living on the range edge will experience reduced food security, harsh physiological conditions (e.g., cold temperatures and snow) and will likely have poorer energetic condition, which will result in lower levels of testosterone (maintaining a high testosterone phenotype is difficult under energetic duress). Males in good condition with high testosterone are likely better able to control territories within the central range of the grackle habitat, pushing low testosterone males in poorer condition to the periphery of the grackle range.

**P3 alternative 1:** Alternatively, testosterone has been associated with novel sensation seeking and risk taking in humans (e.g., Campbell et al 2010), so males with higher testosterone may seek novel stimuli, moving to the periphery of grackle ranges.

**P3 alternative 2:** Alternatively, testosterone may be higher in the US populations due to a higher reliance on high calorie human foods and reduced parasite loads, paralleling differences seen in human populations.

#### H4: Populations closer to the range edge will have higher levels of serum glucocorticoids

**P4:** Grackles living on the range edge will experience reduced food security, harsh physiological conditions (e.g., cold temperatures and snow) and likely have poorer energetic condition, which will result in higher circulating glucocorticoids as these factors all represent physiological and mental stressors.

**P4 Alternative 1:** Constant physiological and mental stressors can result in chronically low levels of cortisol in humans (Yehuda 2002), and low cortisol responsivity to stresses (e.g. Yehuda and Seckl 2011). If this is a phylogenetically constrained phenomenon, then constantly stressed grackles may have low baseline glucocorticoids and a low stress response. Because samples are taken following the grackles being captured, they will likely be experiencing a stressor and have higher than baseline levels of corticosterone: if chronically stressed grackles on the margins of their territory do not espouse a strong stress response, they may appear to have low baseline cortisol when in actuality we are comparing non-reactive cortisol in marginal populations to a strong stress response in central populations.

#### H5: Populations closer to the range edge will have poorer body condition.

**P5:** The longer the distance from the center of the original range, the more likely they are to have poor body condition (shorter tarsus length) because of the difficulty of moving to new environments that are physiologically more stressful (e.g., cold temperatures and snow) than their original tropical environment.

**P5 alternative 1a:** If there is a positive correlation between distance from the center of the original range and body condition (longer tarsus length), this could indicate that the better quality individuals are the ones that are better able to disperse and adapt to new environments.

**P5 alternative 1b:** A positive correlation between body size and edge distance could also result if grackles in Arizona and Nebraska subsist more on high calorie human foods. However, we would expect this to be associated with poorer condition on other measures such as testosterone and hematocrit and/or red blood cell counts.

**P5 alternative 2:** If there is no correlation, this could indicate these variables are independent from each other or that they are related to another variable that was not measured

**P5 alternative 3:** Grackles expanding into colder areas (Nebraska) may have a larger body size, which is beneficial in a colder environment. If this is the case, then we predict that grackles will be smaller in Arizona and Honduras.

#### H6: Grackles in populations closer to the range edge will have higher variation in haemosporidian parasite loads.

**P6:** Populations closer to the range edge will have a higher individual variance in parasite loads (the total number of parasite individuals and the total number of parasite species), harbor more novel parasite species, and more parasite species that are not common near the range edge because 1) grackles that are nearer the range edge might be in poorer energetic condition and more susceptible to acquiring parasites, and 2) the younger age of these grackle populations exposes them to new parasite species due to encountering new geographic regions.

**P6 alternative 1:** Populations closer to the range edge will have lower haemosporidian parasite loads because there will be less contact with suitable vectors due to their recent establishment.

**P6 alternative 2:** Populations closer to the range edge will have haemosporidian parasite loads that are not different from other populations because these parasites were carried by grackles throughout their range expansion, which could indicate that flexibility and haemosporidian parasite loads are independent from each other or that they are related to another variable that was not measured.

#### H7: Grackles in populations closer to the range edge will have elevated immune markers indicative of active infection.

**P7:** Given the variation in exposure to novel parasites and poorer energetic condition (H6), we expect grackles closer to the range edge to have higher indicators of active infection, including elevated total leukocytes, elevated heterophils, and a greater number of immature red blood cells, indicating increased turn-over in red blood cells.

**P7 alternative 1** If P6 alternative 1 is supported, and grackles closer to the range edge are exposed to fewer parasites and have lower disease transmission, then we expect lower measures of immune activation.

#### H8: Populations closer to the range edge will have lower indicators or baseline cellular immunity when not actively fighting infection.

**P8:** Individuals in poor energetic condition from reduced food availability, increased physical activity to get scarce food resources, or physiologically stressful conditions (e.g., cold temperatures and snow) will lower lymphocyte counts, and lower lymphocyte/heterophil ratios.

**P8 alternative 1:** Alternatively, high lymphocyte counts may facilitate range expansion by improving resistance to novel pathogens, and individuals with high counts may be more likely to be found in edge populations.

**P8 alternative 2:** If individuals in edge populations are not in poorer condition, they might still have lower baseline immunity if they are less regularly challenged by parasites and pathogens.

#### H9: Populations closer to the range edge will have higher microbiome species diversity.

**P9:** Populations closer to the range edge will have higher microbiome species diversity because 1) grackles that are nearer the range edge might be in poorer energetic condition and more susceptible to hosting more species, and/or 2) the younger age of these grackle populations exposes them to new microbiome species due to consuming new foods (Alberdi et al. (2016)). The higher transient diversity of microbiome species in the edge population could stabilize over time.

**P9 alternative 1:** Populations closer to the range edge will have lower microbiome species diversity because these individuals exploit similar food sources and/or because they are a more recently established population that has not yet become a suitable host for particular microbiome species.

**P9 alternative 2:** Populations closer to the range edge will have microbiome species diversity that is not different from other populations, which could indicate that flexibility and microbiome species diversity are independent from each other or that they are related to another variable that was not measured.

#### H10: Populations closer to the range edge will have stronger selection for flexibility (a stronger association between fitness and flexibility) and lower heritability of flexibility (based on the pedigree)

**P10:** More flexible individuals are more likely to have fitness benefits in edge (novel) environments, whereas in non-edge populations previous experiences (either during development (plasticity) or during a "sensitive period" (initial learning about what/where/when resources are available, when to breed, etc.) or previous generations (selection)) may have shaped responses to the environment. Accordingly, in edge populations the fitness benefits of flexibility will outweigh any potential fitness costs, and there will be a stronger correlation between fitness and flexibility. In edge environments, when there is stronger selection for flexibility there will be less variation because everyone has to be flexible (e.g., Jones and DiRienzo (2018)), therefore knowing which lineage individuals come from is not informative about how flexible they will be. In contrast, in non-edge populations where there is weaker selection for or against flexibility, variation in flexibility might exist and be inherited. Selection will be measured as the correlation between the number of offspring an individual has (determined using paternity and maternity from ddRADseq) and [flexibility](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md), and the heritability of flexibility will be measured in a separate [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexgenes.md).

**P10 alternative:** We will not detect selection for flexibility in individuals living in edge populations potentially because 1) the dispersing individuals are subordinate are forced to leave their natal areas and therefore the trait under selection would be dominance rank (investigated in a future preregistration), and/or 2) there are high costs associated with flexibility in novel environments (e.g., parasite exposure, a different climate, unfamiliar breeding sites, see previous hypotheses), and/or 3) non-edge populations also have a high degree of immigration and mixing such that individuals constantly experience new environments (measured using ddRADseq, see P12 alternative 2), and therefore we will not be able to detect a signal between fitness and flexibility.

#### H11: Populations at the range edge will be more likely to have unique traits (traits not found in other populations)

**P11:** Edge populations will be more divergent for some traits if bottlenecks occurred during their geographic range expansion (repeated linear expansion - like hopping from one island to the next). Rare variants can increase in frequency because migration into new areas usually starts from a random small subset of individuals, who by chance might have certain traits that are usually not found in most individuals.

**P11 alternative:** Edge populations will not be more divergent for some traits if migration into new areas is sourced from multiple places along the edge.

#### H12: Populations closer to the edge will have reduced genetic diversity, though genetic differences among pairs of individuals can be high

**P12:** Edge populations will have lower levels of genetic variation because expansion occurs through stepwise repeated migration of a small number of individuals who only carry a subset of the genetic variation found in the source population. Pairs of individuals might be different from each other if individuals immigrated from multiple distinct source populations, whereas in non-edge populations most individuals are likely to have been hatched in the same population.

**P12 alternative 1:** Edge populations will not show reduced variation if the expansion occurs gradually and where multiple individuals slowly move into new areas while remaining in contact with the source population. Pairs of individuals will not show higher genetic differences because they all originated from the same source population.

**P12 alternative 2:** Edge populations will not show reduced variation if individuals frequently move long distances to breed so that edge populations as well as more central populations contain very divergent individuals.

### D. METHODS

#### **Randomization and counterbalancing**

No randomization or counterbalancing is involved in this study.

#### **Blinding of conditions during analysis**

No blinding is involved in this study.

#### **Dependent variables**

#### *P1: edge & flexibility*

1.  Flexibility 1: **Number of trials to reverse** a preference in the last reversal an individual experienced (reversal learning; an individual is considered to have a preference if it chose the rewarded option at least 17 out of the most recent 20 trials, with a minimum of 8 or 9 correct choices out of 10 on the two most recent sets of 10 trials). See behavioral flexibility [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md).

2.  Flexibility 2: The **ratio of correct divided by incorrect trials** for the first 40 trials in their final reversal after the individual has seen the newly rewarded option once. These 40 trials include trials where individuals were offered the test and chose not to participate (i.e., make a choice). This accounts for flexibility that can occur when some individuals inhibit their previously rewarded preference (thus exhibiting flexibility because they changed their behavior when circumstances changed), but are not as exploratory as those who have fewer 'no choice' trials. 'No choice' data is data that is otherwise excluded from standard reversal learning analyses. Including 'no choice' trials, controls for individual differences in exploration because those that refuse to choose are not exploring new options, which would allow them to learn the new food location.

3.  Flexibility 3: If the number of trials to reverse a preference does not positively correlate with the latency to attempt or solve new loci on the multi-access box (an additional measure of behavioral flexibility), then the **average latency to solve** and the **average latency to attempt** a new option on the multi-access box will be additional dependent variables. See behavioral flexibility [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md).

One model will be run per dependent variable.

#### *P2: edge & foraging variation*

Number of human food types consumed in the first X minutes (X=the sum of the total observation time per individual, using the individual who had the lowest sum to equalize observation time across individuals) from focal follow observations on wild, individually-marked grackles

#### *P3: edge & testosterone*

Testosterone concentration at capture

#### *P4: edge & glucocorticoids*

Serum glucocorticoid concentration

#### *P5: edge & body condition*

1.  Tarsus length (average of left and right legs)

2.  Hematocrit

3.  Number of red blood cells

#### *P6: edge & haemosporidian parasites*

1.  Number of parasite individuals

2.  Number of parasite species

3.  Number of novel (to grackles) parasite species

4.  Number of uncommon parasite species in this geographic area

One model will be run per dependent variable.

#### *P7: edge & immune activation*

1.  Number of white blood cells

2.  Number of heterophils

3.  Number of immature red blood cells

#### *P8: edge & baseline immunity*

1.  Number of lymphocytes

2.  Lymphocyte/heterophil ratio

#### *P9: edge & microbiome*

1.  Number of species

#### *P10: selection on flexibility*

1.  Slope of the correlation between flexibility and the number of offspring per individual (controlled for age and sex)

#### *P11: unique genes at edge*

1.  Number of genetic variants that only exist in a single population

#### *P12: reduced genetic diversity at edge*

1.  Number of different genetic variants per locus

2.  Heterozygosity: average proportion of the genome at which individuals carry two different genetic variants on the two different chromosomes

#### **Independent variables**

#### *P1-P12*

1.  Population: center (Central America), middle of the northern expansion front (Arizona), edge of the northern expansion front (Nebraska)

### E. ANALYSIS PLAN

We do not plan to **exclude** any data. When **missing data** occur, the existing data for that individual will be included in the analyses for the tests they completed. Analyses will be conducted in R (current version 3.3.3; R Core Team (2017)). We will analyze data for females and males separately because each sex has a distinct natural history (Johnson and Peer (2001)).

#### *Data checking*

The data will be visually checked to determine whether they are normally distributed via two methods: 1) normality is indicated when the histograms of actual data match those with simulated data (Figure 2), and 2) normality is indicated when the residuals closely fit the dotted line in the Normal Q-Q plot (Figure 3) (Zuur, Ieno, and Saveliev 2009).

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# Check the dependent variables for normality: Histograms
# females
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
# This is what the distribution of actual data looks like
hist(fem$TrialsToReverseLast, xlab = "Flexibility: Trials to reverse", 
    main = "Actual Data")
hist(fem$FlexRatio, xlab = "Flexibility: Ratio correct", main = "Actual Data")
hist(fem$NumberHumanFoodsEaten, xlab = "% human foods eaten", 
    main = "Actual Data")
hist(fem$AvgTarsusLength, xlab = "Condition: Avg tarsus length", 
    main = "Actual Data")
hist(fem$Hematocrit, xlab = "Condition: Avg tarsus length", main = "Actual Data")
hist(fem$AvgTarsusLength, xlab = "Condition: Avg tarsus length", 
    main = "Actual Data")
hist(fem$NumberRedBloodCells, xlab = "Condition: number RBCs", 
    main = "Actual Data")
hist(fem$NumberLeucocytes, xlab = "Immune activation: number WBCs", 
    main = "Actual Data")
hist(fem$NumberHeterophils, xlab = "Immune activation: number heterophils", 
    main = "Actual Data")
hist(fem$NumberImmatureRedBloodCells, xlab = "Immune activation: number immature RBCs", 
    main = "Actual Data")
hist(fem$NumberLymphocytes, xlab = "Baseline immunity: number lymphocytes", 
    main = "Actual Data")
hist(fem$LymphocyteHeterophilRatio, xlab = "Baseline immunity: lymphocyte/heterophil ratio", 
    main = "Actual Data")
hist(fem$NumberParasiteSpecies, xlab = "Parasites: number of species", 
    main = "Actual Data")
hist(fem$NumberNovelParasiteSpecies, xlab = "Parasites: number novel species", 
    main = "Actual Data")
hist(fem$NumberUncommonParasiteSpecies, xlab = "Parasites: number uncommon species", 
    main = "Actual Data")
hist(fem$NumberMicrobiomeSpecies, xlab = "Microbiome: number of species", 
    main = "Actual Data")


# Given the actual data, this is what a normal distribution
# would look like
X2 <- rnorm(1281, mean = mean(fem$TrialsToReverseLast), sd = sd(fem$TrialsToReverseLast))
hist(X2, xlab = "Flexibility: Trials to reverse", main = "Simulated Data")

Y2 <- rnorm(1281, mean = mean(fem$FlexRatio), sd = sd(fem$FlexRatio))
hist(Y2, xlab = "Flexibility: Ratio correct", main = "Simulated Data")

G2 <- rnorm(1281, mean = mean(fem$NumberHumanFoodsEaten), sd = sd(fem$NumberHumanFoodsEaten))
hist(G2, xlab = "% human foods eaten", main = "Simulated Data")

H2 <- rnorm(1281, mean = mean(fem$Hematocrit), sd = sd(fem$Hematocrit))
hist(H2, xlab = "Condition: hematocrit", main = "Simulated Data")

Z2 <- rnorm(1281, mean = mean(fem$AvgTarsusLength), sd = sd(fem$AvgTarsusLength))
hist(Z2, xlab = "Condition: Avg tarsus length", main = "Simulated Data")

I2 <- rnorm(1281, mean = mean(fem$NumberRedBloodCells), sd = sd(fem$NumberRedBloodCells))
hist(I2, xlab = "Condition: number RBCs", main = "Simulated Data")

J2 <- rnorm(1281, mean = mean(fem$NumberLeucocytes), sd = sd(fem$NumberLeucocytes))
hist(J2, xlab = "Immune activation: number WBCs", main = "Simulated Data")

K2 <- rnorm(1281, mean = mean(fem$NumberHeterophils), sd = sd(fem$NumberHeterophils))
hist(K2, xlab = "Immune activation: number heterophils", main = "Simulated Data")

L2 <- rnorm(1281, mean = mean(fem$NumberImmatureRedBloodCells), 
    sd = sd(fem$NumberImmatureRedBloodCells))
hist(L2, xlab = "Immune activation: number immature RBCs", main = "Simulated Data")

M2 <- rnorm(1281, mean = mean(fem$NumberLymphocytes), sd = sd(fem$NumberLymphocytes))
hist(M2, xlab = "Baseline immunity: number lymphocytes", main = "Simulated Data")

N2 <- rnorm(1281, mean = mean(fem$LymphocyteHeterophilRatio), 
    sd = sd(fem$LymphocyteHeterophilRatio))
hist(N2, xlab = "Baseline immunity: lymphocyte/heterophil ratio", 
    main = "Simulated Data")

A2 <- rnorm(1281, mean = mean(fem$NumberParasites), sd = sd(fem$NumberParasites))
hist(A2, xlab = "Parasites: number parasite inds", main = "Simulated Data")

B2 <- rnorm(1281, mean = mean(fem$NumberParasiteSpecies), sd = sd(fem$NumberParasiteSpecies))
hist(B2, xlab = "Parasites: number spp", main = "Simulated Data")

D2 <- rnorm(1281, mean = mean(fem$NumberNovelParasiteSpecies), 
    sd = sd(fem$NumberNovelParasiteSpecies))
hist(D2, xlab = "Parasites: novel spp", main = "Simulated Data")

E2 <- rnorm(1281, mean = mean(fem$NumberUncommonParasiteSpecies), 
    sd = sd(fem$NumberUncommonParasiteSpecies))
hist(E2, xlab = "Parasites: uncommon spp", main = "Simulated Data")

F2 <- rnorm(1281, mean = mean(fem$NumberMicrobiomeSpecies), sd = sd(fem$NumberMicrobiomeSpecies))
hist(F2, xlab = "Microbiome: number species", main = "Simulated Data")


# males
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
# This is what the distribution of actual data looks like
hist(mal$TrialsToReverseLast, xlab = "Flexibility: Trials to reverse", 
    main = "Actual Data")
hist(mal$FlexRatio, xlab = "Flexibility: Ratio correct", main = "Actual Data")
hist(mal$NumberHumanFoodsEaten, xlab = "% human foods eaten", 
    main = "Actual Data")
hist(mal$AvgTarsusLength, xlab = "Condition: Avg tarsus length", 
    main = "Actual Data")
hist(mal$Hematocrit, xlab = "Condition: Avg tarsus length", main = "Actual Data")
hist(mal$AvgTarsusLength, xlab = "Condition: Avg tarsus length", 
    main = "Actual Data")
hist(mal$NumberRedBloodCells, xlab = "Condition: number RBCs", 
    main = "Actual Data")
hist(mal$NumberLeucocytes, xlab = "Immune activation: number WBCs", 
    main = "Actual Data")
hist(mal$NumberHeterophils, xlab = "Immune activation: number heterophils", 
    main = "Actual Data")
hist(mal$NumberImmatureRedBloodCells, xlab = "Immune activation: number immature RBCs", 
    main = "Actual Data")
hist(mal$NumberLymphocytes, xlab = "Baseline immunity: number lymphocytes", 
    main = "Actual Data")
hist(mal$LymphocyteHeterophilRatio, xlab = "Baseline immunity: lymphocyte/heterophil ratio", 
    main = "Actual Data")
hist(mal$NumberParasiteSpecies, xlab = "Parasites: number of species", 
    main = "Actual Data")
hist(mal$NumberNovelParasiteSpecies, xlab = "Parasites: number novel species", 
    main = "Actual Data")
hist(mal$NumberUncommonParasiteSpecies, xlab = "Parasites: number uncommon species", 
    main = "Actual Data")
hist(mal$NumberMicrobiomeSpecies, xlab = "Microbiome: number of species", 
    main = "Actual Data")


# Given the actual data, this is what a normal distribution
# would look like
x2 <- rnorm(1281, mean = mean(mal$TrialsToReverseLast), sd = sd(mal$TrialsToReverseLast))
hist(x2, xlab = "Flexibility: Trials to reverse", main = "Simulated Data")

y2 <- rnorm(1281, mean = mean(mal$FlexRatio), sd = sd(mal$FlexRatio))
hist(y2, xlab = "Flexibility: Ratio correct", main = "Simulated Data")

g2 <- rnorm(1281, mean = mean(mal$NumberHumanFoodsEaten), sd = sd(mal$NumberHumanFoodsEaten))
hist(g2, xlab = "% human foods eaten", main = "Simulated Data")

h2 <- rnorm(1281, mean = mean(mal$Hematocrit), sd = sd(mal$Hematocrit))
hist(h2, xlab = "Condition: hematocrit", main = "Simulated Data")

z2 <- rnorm(1281, mean = mean(mal$AvgTarsusLength), sd = sd(mal$AvgTarsusLength))
hist(z2, xlab = "Condition: Avg tarsus length", main = "Simulated Data")

i2 <- rnorm(1281, mean = mean(mal$NumberRedBloodCells), sd = sd(mal$NumberRedBloodCells))
hist(i2, xlab = "Condition: number RBCs", main = "Simulated Data")

j2 <- rnorm(1281, mean = mean(mal$NumberLeucocytes), sd = sd(mal$NumberLeucocytes))
hist(j2, xlab = "Immune activation: number WBCs", main = "Simulated Data")

k2 <- rnorm(1281, mean = mean(mal$NumberHeterophils), sd = sd(mal$NumberHeterophils))
hist(k2, xlab = "Immune activation: number heterophils", main = "Simulated Data")

l2 <- rnorm(1281, mean = mean(mal$NumberImmatureRedBloodCells), 
    sd = sd(mal$NumberImmatureRedBloodCells))
hist(l2, xlab = "Immune activation: number immature RBCs", main = "Simulated Data")

m2 <- rnorm(1281, mean = mean(mal$NumberLymphocytes), sd = sd(mal$NumberLymphocytes))
hist(m2, xlab = "Baseline immunity: number lymphocytes", main = "Simulated Data")

n2 <- rnorm(1281, mean = mean(mal$LymphocyteHeterophilRatio), 
    sd = sd(mal$LymphocyteHeterophilRatio))
hist(n2, xlab = "Baseline immunity: lymphocyte/heterophil ratio", 
    main = "Simulated Data")

a2 <- rnorm(1281, mean = mean(mal$NumberParasites), sd = sd(mal$NumberParasites))
hist(a2, xlab = "Parasites: number parasite inds", main = "Simulated Data")

b2 <- rnorm(1281, mean = mean(mal$NumberParasiteSpecies), sd = sd(mal$NumberParasiteSpecies))
hist(b2, xlab = "Parasites: number spp", main = "Simulated Data")

d2 <- rnorm(1281, mean = mean(mal$NumberNovelParasiteSpecies), 
    sd = sd(mal$NumberNovelParasiteSpecies))
hist(d2, xlab = "Parasites: novel spp", main = "Simulated Data")

e2 <- rnorm(1281, mean = mean(mal$NumberUncommonParasiteSpecies), 
    sd = sd(mal$NumberUncommonParasiteSpecies))
hist(e2, xlab = "Parasites: uncommon spp", main = "Simulated Data")

f2 <- rnorm(1281, mean = mean(mal$NumberMicrobiomeSpecies), sd = sd(mal$NumberMicrobiomeSpecies))
hist(f2, xlab = "Microbiome: number species", main = "Simulated Data")


# Check the dependent variables for normality: Q-Q plots
# females
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(glm(fem$TrialsToReverseLast ~ fem$Population))
plot(glm(fem$AvgTarsusLength ~ fem$Population))
plot(glm(fem$NumberHumanFoodsEaten ~ fem$Population))
plot(glm(fem$Hematocrit ~ fem$Population))

op <- par(mfrow = c(5, 4), mar = c(4, 4, 2, 0.2))
plot(glm(fem$NumberRedBloodCells ~ fem$Population))
plot(glm(fem$NumberLeucocytes ~ fem$Population))
plot(glm(fem$NumberImmatureRedBloodCells ~ fem$Population))
plot(glm(fem$NumberLymphocytes ~ fem$Population))
plot(glm(fem$LymphocyteHeterophilRatio ~ fem$Population))

op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(glm(fem$NumberParasiteSpecies ~ fem$Population))
plot(glm(fem$NumberNovelParasiteSpecies ~ fem$Population))
plot(glm(fem$NumberUncommonParasiteSpecies ~ fem$Population))
plot(glm(fem$NumberMicrobiomeSpecies ~ fem$Population))

# males
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(glm(mal$TrialsToReverseLast ~ mal$Population))
plot(glm(mal$AvgTarsusLength ~ mal$Population))
plot(glm(mal$NumberHumanFoodsEaten ~ mal$Population))
plot(glm(mal$Hematocrit ~ mal$Population))

op <- par(mfrow = c(5, 4), mar = c(4, 4, 2, 0.2))
plot(glm(mal$NumberRedBloodCells ~ mal$Population))
plot(glm(mal$NumberLeucocytes ~ mal$Population))
plot(glm(mal$NumberImmatureRedBloodCells ~ mal$Population))
plot(glm(mal$NumberLymphocytes ~ mal$Population))
plot(glm(mal$LymphocyteHeterophilRatio ~ mal$Population))

op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(glm(mal$NumberParasiteSpecies ~ mal$Population))
plot(glm(mal$NumberNovelParasiteSpecies ~ mal$Population))
plot(glm(mal$NumberUncommonParasiteSpecies ~ mal$Population))
plot(glm(mal$NumberMicrobiomeSpecies ~ mal$Population))
```

If the data do not appear normally distributed, visually check the residuals. If they are patternless, then assume a normal distribution (Figure 4) (Zuur, Ieno, and Saveliev 2009).

``` r
# Check the dependent variables for normality: Residuals
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# Figure 3. Visual check of the residuals females
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(residuals(glm(fem$TrialsToReverseLast ~ fem$Population)), 
    ylab = "Residuals (flexibility): Trials to reverse ~ Population")
plot(residuals(glm(fem$NumberHumanFoodsEaten ~ fem$Population)), 
    ylab = "Residuals: % human foods ~ Population")
plot(residuals(glm(fem$AvgTarsusLength ~ fem$Population)), ylab = "Residuals (condition): Tarsus length ~ Population")
plot(residuals(glm(fem$Hematocrit ~ fem$Population)), ylab = "Residuals (condition): hematocrit ~ Population")
plot(residuals(glm(fem$NumberRedBloodCells ~ fem$Population)), 
    ylab = "Residuals (condition): RBCs ~ Population")
plot(residuals(glm(fem$NumberParasites ~ fem$Population)), ylab = "Residuals (parasites): number inds ~ Population")
plot(residuals(glm(fem$NumberParasiteSpecies ~ fem$Population)), 
    ylab = "Residuals (parasites): number spp ~ Population")
plot(residuals(glm(fem$NumberNovelParasiteSpecies ~ fem$Population)), 
    ylab = "Residuals (parasites): number novel ~ Population")
plot(residuals(glm(fem$NumberUncommonParasiteSpecies ~ fem$Population)), 
    ylab = "Residuals (parasites): number uncommon ~ Population")
plot(residuals(glm(fem$NumberLeucocytes ~ fem$Population)), ylab = "Residuals (immune): WBCs ~ Population")
plot(residuals(glm(fem$NumberHeterophil ~ fem$Population)), ylab = "Residuals (immune): heterophils ~ Population")
plot(residuals(glm(fem$NumberLymphocytes ~ fem$Population)), 
    ylab = "Residuals (immunity): lymphocytes ~ Population")
plot(residuals(glm(fem$LymphocyteHeterophilRatio ~ fem$Population)), 
    ylab = "Residuals (immunity): Lymph/Hetero ~ Population")
plot(residuals(glm(fem$NumberMicrobiomeSpecies ~ fem$Population)), 
    ylab = "Residuals (microbiome): number spp ~ Population")

# males
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(residuals(glm(mal$TrialsToReverseLast ~ mal$Population)), 
    ylab = "Residuals (flexibility): Trials to reverse ~ Population")
plot(residuals(glm(mal$NumberHumanFoodsEaten ~ mal$Population)), 
    ylab = "Residuals: % human foods ~ Population")
plot(residuals(glm(mal$AvgTarsusLength ~ mal$Population)), ylab = "Residuals (condition): Tarsus length ~ Population")
plot(residuals(glm(mal$Hematocrit ~ mal$Population)), ylab = "Residuals (condition): hematocrit ~ Population")
plot(residuals(glm(mal$NumberRedBloodCells ~ mal$Population)), 
    ylab = "Residuals (condition): RBCs ~ Population")
plot(residuals(glm(mal$NumberParasites ~ mal$Population)), ylab = "Residuals (parasites): number inds ~ Population")
plot(residuals(glm(mal$NumberParasiteSpecies ~ mal$Population)), 
    ylab = "Residuals (parasites): number spp ~ Population")
plot(residuals(glm(mal$NumberNovelParasiteSpecies ~ mal$Population)), 
    ylab = "Residuals (parasites): number novel ~ Population")
plot(residuals(glm(mal$NumberUncommonParasiteSpecies ~ mal$Population)), 
    ylab = "Residuals (parasites): number uncommon ~ Population")
plot(residuals(glm(mal$NumberLeucocytes ~ mal$Population)), ylab = "Residuals (immune): WBCs ~ Population")
plot(residuals(glm(mal$NumberHeterophil ~ mal$Population)), ylab = "Residuals (immune): heterophils ~ Population")
plot(residuals(glm(mal$NumberLymphocytes ~ mal$Population)), 
    ylab = "Residuals (immunity): lymphocytes ~ Population")
plot(residuals(glm(mal$LymphocyteHeterophilRatio ~ mal$Population)), 
    ylab = "Residuals (immunity): Lymph/Hetero ~ Population")
plot(residuals(glm(mal$NumberMicrobiomeSpecies ~ mal$Population)), 
    ylab = "Residuals (microbiome): number spp ~ Population")
```

#### *P1: edge & flexibility*

**Analysis:** Generalized Linear Model (GLM; glm function, stats package) with a Poisson distribution and log link. The contribution of the independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLM: dependent variable = Flexibility 1: number of trials
# to reverse last preference female
flex1 <- glm(TrialsToReverseLast ~ Population, family = "poisson", 
    data = fem)
# summary(flex1)

flexa <- summary(flex1)
library(xtable)
flexa.table <- xtable(flexa)
library(knitr)
kable(flexa.table, caption = "Table 1: Model selection output.", 
    format = "html", digits = 2)

# male
flex2 <- glm(TrialsToReverseLast ~ Population, family = "poisson", 
    data = mal)
# summary(flex2)

flexb <- summary(flex2)
library(xtable)
flexb.table <- xtable(flexb)
library(knitr)
kable(flexb.table, caption = "Table 2: Model selection output.", 
    format = "html", digits = 2)


# GLM: dependent variable = Flexibility 2: ratio of correct
# divided by incorrect trials female
flex3 <- glm(FlexRatio ~ Population, family = "poisson", data = fem)
# summary(flex3)

flexc <- summary(flex3)
library(xtable)
flexc.table <- xtable(flexc)
library(knitr)
kable(flexc.table, caption = "Table 3: Model selection output.", 
    format = "html", digits = 2)

# male
flex4 <- glm(FlexRatio ~ Population, family = "poisson", data = mal)
# summary(flex4)

flexd <- summary(flex4)
library(xtable)
flexd.table <- xtable(flexd)
library(knitr)
kable(flexd.table, caption = "Table 4: Model selection output.", 
    format = "html", digits = 2)
```

*P1 alternative: variance of flexibility across populations*

Determine whether population variances in Flexibility measures 1-3 differ among populations.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_accumulation.csv", 
    header = T, sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# female variance
ctr1 <- fem[fem$Population == "HO", ]  #Honduras
mdl1 <- fem[fem$Population == "AZ", ]  #Arizona
edg1 <- fem[fem$Population == "NE", ]  #Nebraska

A <- var(ctr1$FlexRatio)
D <- var(ctr1$TrialsToReverseLast)

B <- var(mdl1$FlexRatio)
E <- var(mdl1$TrialsToReverseLast)

C <- var(edg1$FlexRatio)
G <- var(edg1$TrialsToReverseLast)

ratio1 <- c(A, B, C)
last1 <- c(D, E, G)

op <- par(mfrow = c(1, 2), mar = c(4, 4, 2, 0.2))
plot(ratio1)
plot(last1)

# male variance
ctr2 <- mal[mal$Population == "HO", ]  #Honduras
mdl2 <- mal[mal$Population == "AZ", ]  #Arizona
edg2 <- mal[mal$Population == "NE", ]  #Nebraska

H <- var(ctr2$FlexRatio)
I <- var(ctr2$TrialsToReverseLast)

J <- var(mdl2$FlexRatio)
K <- var(mdl2$TrialsToReverseLast)

L <- var(edg2$FlexRatio)
M <- var(edg2$TrialsToReverseLast)

ratio2 <- c(H, J, L)
last2 <- c(I, K, M)

op <- par(mfrow = c(1, 2), mar = c(4, 4, 2, 0.2))
plot(ratio2)
plot(last2)
```

#### *P2: edge & foraging variation*

**Analysis:** Generalized Linear Model (GLM; glm function, stats package) with a Poisson distribution and log link. The contribution of the independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLM female
t1 <- glm(NumberHumanFoodsEaten ~ Population, family = "poisson", 
    data = fem)
# summary(t1)

ta <- summary(t1)
library(xtable)
ta.table <- xtable(ta)
library(knitr)
kable(ta.table, caption = "Table 5: Model selection output.", 
    format = "html", digits = 2)

# male
t2 <- glm(NumberHumanFoodsEaten ~ Population, family = "poisson", 
    data = mal)
# summary(t2)

tb <- summary(t2)
library(xtable)
tb.table <- xtable(tb)
library(knitr)
kable(tb.table, caption = "Table 6: Model selection output.", 
    format = "html", digits = 2)
```

#### *P3: edge & testosterone*

**Analysis:** Generalized Linear Model (GLM; glm function, stats package) with a Poisson distribution and log link. The contribution of the independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLM female
t1 <- glm(Testosterone ~ Population, family = "poisson", data = fem)
# summary(t1)

ta <- summary(t1)
library(xtable)
ta.table <- xtable(ta)
library(knitr)
kable(ta.table, caption = "Table 7: Model selection output.", 
    format = "html", digits = 2)

# male
t2 <- glm(Testosterone ~ Population, family = "poisson", data = mal)
# summary(t2)

tb <- summary(t2)
library(xtable)
tb.table <- xtable(tb)
library(knitr)
kable(tb.table, caption = "Table 8: Model selection output.", 
    format = "html", digits = 2)
```

#### *P4: edge & glucocorticoids*

**Analysis:** To be able to detect trade offs, we need to control for condition, therefore we chose the average tarsus length as the representative measure of condition (a random effect). We will conduct a Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0)), G = list(G1 = list(V = 1, 
    nu = 0)))

# females
f1 <- MCMCglmm(Cort ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(Cort ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?
```

#### *P5: edge & body condition*

**Analysis:** Generalized Linear Model (GLM; glm function, stats package) with a Poisson distribution and log link. The contribution of the independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLM female
t1 <- glm(AvgTarsusLength ~ Population, family = "poisson", data = fem)
# summary(t1)

ta <- summary(t1)
library(xtable)
ta.table <- xtable(ta)
library(knitr)
kable(ta.table, caption = "Table 9: Model selection output.", 
    format = "html", digits = 2)

# male
t2 <- glm(AvgTarsusLength ~ Population, family = "poisson", data = mal)
# summary(t2)

tb <- summary(t2)
library(xtable)
tb.table <- xtable(tb)
library(knitr)
kable(tb.table, caption = "Table 10: Model selection output.", 
    format = "html", digits = 2)
```

#### *P6: edge & haemosporidian parasites*

**Analysis:** To be able to detect trade offs, we need to control for condition, therefore we chose the average tarsus length as the representative measure of condition (a random effect). We will conduct a Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLMM: response variable = number of parasite individuals
# per bird
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0)), G = list(G1 = list(V = 1, 
    nu = 0)))

# females
f1 <- MCMCglmm(NumberParasites ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(NumberParasites ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?

# GLMM: response variable = number of parasite species per
# bird females
f2 <- MCMCglmm(NumberParasiteSpecies ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f2)
# autocorr(f2$Sol) #Did fixed effects converge?
# autocorr(f2$VCV) #Did random effects converge?

# males
m2 <- MCMCglmm(NumberParasiteSpecies ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m2)
# autocorr(m2$Sol) #Did fixed effects converge?
# autocorr(m2$VCV) #Did random effects converge?


# GLMM: response variable = number of NOVEL parasite species
# per bird females
f4 <- MCMCglmm(NumberNovelParasiteSpecies ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f4)
# autocorr(f4$Sol) #Did fixed effects converge?
# autocorr(f4$VCV) #Did random effects converge?

# males
m4 <- MCMCglmm(NumberNovelParasiteSpecies ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m4)
# autocorr(m4$Sol) #Did fixed effects converge?
# autocorr(m4$VCV) #Did random effects converge?


# GLMM: response variable = number of UNCOMMON parasite
# species per bird females
f5 <- MCMCglmm(NumberUncommonParasiteSpecies ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f5)
# autocorr(f5$Sol) #Did fixed effects converge?
# autocorr(f5$VCV) #Did random effects converge?

# males
m5 <- MCMCglmm(NumberUncommonParasiteSpecies ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m5)
# autocorr(m5$Sol) #Did fixed effects converge?
# autocorr(m5$VCV) #Did random effects converge?
```

#### *P7: edge & immune activation*

**Analysis:** To be able to detect trade offs, we need to control for condition, therefore we chose the average tarsus length as the representative measure of condition (a random effect). We will conduct a Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0)), G = list(G1 = list(V = 1, 
    nu = 0)))

# females
f1 <- MCMCglmm(NumberLeucocytes ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

f2 <- MCMCglmm(NumberHeterophils ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f2)
# autocorr(f2$Sol) #Did fixed effects converge?
# autocorr(f2$VCV) #Did random effects converge?

f3 <- MCMCglmm(NumberImmatureRedBloodCells ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f3)
# autocorr(f3$Sol) #Did fixed effects converge?
# autocorr(f3$VCV) #Did random effects converge?


# males
m1 <- MCMCglmm(NumberLeucocytes ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?

m2 <- MCMCglmm(NumberHeterophils ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m2)
# autocorr(m2$Sol) #Did fixed effects converge?
# autocorr(m2$VCV) #Did random effects converge?

m3 <- MCMCglmm(NumberImmatureRedBloodCells ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m3)
# autocorr(m3$Sol) #Did fixed effects converge?
# autocorr(m3$VCV) #Did random effects converge?
```

#### *P8: edge & baseline immunity*

**Analysis:** To be able to detect trade offs, we need to control for condition, therefore we chose the average tarsus length as the representative measure of condition (a random effect). We will conduct a Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0)), G = list(G1 = list(V = 1, 
    nu = 0)))

# females
f1 <- MCMCglmm(NumberLymphocytes ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

f2 <- MCMCglmm(LymphocyteHeterophilRatio ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f2)
# autocorr(f2$Sol) #Did fixed effects converge?
# autocorr(f2$VCV) #Did random effects converge?


# males
m1 <- MCMCglmm(NumberLymphocytes ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?

m21 <- MCMCglmm(LymphocyteHeterophilRatio ~ Population, random = ~AvgTarsusLength, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m2)
# autocorr(m2$Sol) #Did fixed effects converge?
# autocorr(m2$VCV) #Did random effects converge?
```

#### *P9: edge & microbiome*

**Analysis:** Generalized Linear Model (GLM; glm function, stats package) with a Poisson distribution and log link. The contribution of the independent variable will be evaluated using the Estimate in the full model.

``` r
edge <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- edge[edge$Sex == "f", ]
mal <- edge[edge$Sex == "m", ]

# GLM female
t1 <- glm(NumberMicrobiomeSpecies ~ Population, family = "poisson", 
    data = fem)
# summary(t1)

ta <- summary(t1)
library(xtable)
ta.table <- xtable(ta)
library(knitr)
kable(ta.table, caption = "Table 11: Model selection output.", 
    format = "html", digits = 2)

# male
t2 <- glm(NumberMicrobiomeSpecies ~ Population, family = "poisson", 
    data = mal)
# summary(t2)

tb <- summary(t2)
library(xtable)
tb.table <- xtable(tb)
library(knitr)
kable(tb.table, caption = "Table 12: Model selection output.", 
    format = "html", digits = 2)
```

#### *Alternative Analyses*

We anticipate that we will want to run additional/different analyses after reading McElreath (2016). We will revise this preregistration to include these new analyses before conducting the analyses above.

### F. PLANNED SAMPLE

Great-tailed grackles (n &gt; 200) will be caught in the wild at three field sites across their geographic range: the center of their original range (Utila, Honduras), the middle of the northward expanding edge (Tempe, Arizona USA), and on the northern expanding edge (to be determined). Individuals will be identified using colored leg bands in unique combinations, their data collected (blood, feathers, and biometrics), and then they will be released back to the wild. Some individuals (40-100) will be brought temporarily into aviaries for behavioral testing, and then they will be released back to the wild.

**Sample size rationale**

We will band as many birds as possible throughout the year, and conduct behavioral tests in aviaries (during the non-breeding seasons approximately September through March) and in the wild (year-round) on as many birds as we can at each field site. The minimum sample size will be 200 banded birds and 60 behavior-tested birds in total, however we expect to be able to sample many more.

**Data collection stopping rule**

We will stop collecting data in April 2023 when the current funding ends, or after data have been collected at all three field sites, whichever date comes first.

### G. ETHICS

This research is carried out in accordance with permits from the:

1.  US Fish and Wildlife Service (scientific collecting permit number MB76700A-0,1,2)
2.  US Geological Survey Bird Banding Laboratory (federal bird banding permit number 23872)
3.  Arizona Game and Fish Department (scientific collecting license number SP594338 \[2017\] and SP606267 \[2018\])
4.  Institutional Animal Care and Use Committee at Arizona State University (protocol number 17-1594R)
5.  University of Cambridge ethical review process (non-regulated use of animals in scientific procedures: zoo4/17)

### H. AUTHOR CONTRIBUTIONS

**Logan:** Hypothesis development, study design, materials, data collection, data analysis and interpretation, write up, funding.

**Rowney:** Data collection, sample processing, data analysis and interpretation, editing/revising.

**Bergeron:** Data collection, sample processing, data analysis and interpretation, editing/revising.

**McCune:** Data collection, sample processing, data analysis and interpretation, editing/revising.

**Trumble (testosterone and glucocorticoids):** Hypothesis development, materials/lab space, sample processing, data analysis and interpretation, write up.

**Blackwell (immunity):** Hypothesis development, materials/lab space, sample processing, data analysis and interpretation, write up.

**Escalante (haemosporidian parasites and microbiome):** Hypothesis development, data analysis and interpretation, write up.

**Pacheco (haemosporidian parasites and microbiome):** Hypothesis development, materials/lab space, sample processing, data analysis and interpretation, write up.

**Lukas (genetics):** Hypothesis development, data analysis and interpretation, write up, revising/editing.

### I. FUNDING

This research is funded by the Department of Human Behavior, Ecology and Culture at the Max Planck Institute for Evolutionary Anthropology, and by a Leverhulme Early Career Research Fellowship to Logan.

### J. ACKNOWLEDGEMENTS

We thank Ben Trumble for hosting the grackle project at Arizona State University (providing office and lab space); Melissa Wilson Sayres for sponsoring our affiliations at Arizona State University and lending lab equipment; Kristine Johnson for technical advice on great-tailed grackles; Jay Taylor for grackle scouting at Arizona State University; and Arizona State University School of Life Sciences Department Animal Care and Technologies for providing space for our aviaries and for their excellent support of our daily activities.

### K. REFERENCES

Alberdi, Antton, Ostaizka Aizpurua, Kristine Bohmann, Marie Lisandra Zepeda-Mendoza, and M Thomas P Gilbert. 2016. “Do Vertebrate Gut Metagenomes Confer Rapid Ecological Adaptation?” *Trends in Ecology & Evolution* 31 (9). Elsevier: 689–99.

Hadfield, JD. 2010. “MCMC Methods for Multi-Response Generalized Linear Mixed Models: The Mcmcglmm R Package.” *Journal of Statistical Software* 33 (2): 1–22.

———. 2014. “MCMCglmm Course Notes.” <http://cran.r-project.org/web/packages/MCMCglmm/vignettes/CourseNotes.pdf>.

Johnson, Kristine, and Brian D Peer. 2001. *Great-Tailed Grackle: Quiscalus Mexicanus*. Birds of North America, Incorporated.

Jones, Cameron, and Nicolas DiRienzo. 2018. “Behavioral Variation Post-Invasion: Resemblance in Some, but Not All, Behavioral Patterns Among Invasive and Native Praying Mantids.” *Behavioural Processes*. Elsevier.

McElreath, Richard. 2016. *Statistical Rethinking: A Bayesian Course with Examples in R and Stan*. CRC Press. <http://xcelab.net/rm/statistical-rethinking/>.

R Core Team. 2017. *R: A Language and Environment for Statistical Computing*. Vienna, Austria: R Foundation for Statistical Computing. <https://www.R-project.org>.

Wehtje, Walter. 2003. “The Range Expansion of the Great-Tailed Grackle (Quiscalus Mexicanus Gmelin) in North America Since 1880.” *Journal of Biogeography* 30 (10). Wiley Online Library: 1593–1607.

Zuur, Alain F.., Elena N.. Ieno, and Anatoly A Saveliev. 2009. *Mixed Effects Models and Extensions in Ecology with R*. Springer.
