What are the costs and constraints of behavioral flexibility in great-tailed grackles?
================
[Dr. Corina Logan](http://CorinaLogan.com) (Max Planck Institute for Evolutionary Anthropology, <corina_logan@eva.mpg.de>), Carolyn Rowney (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), Luisa Bergeron (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), Dr. Kelsey McCune (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), [Dr. Benjamin Trumble](https://sols.asu.edu/people/benjamin-trumble) (Arizona State University), [Dr. Aaron Blackwell](http://www.anth.ucsb.edu/faculty/blackwell/) (University of California, Santa Barbara), [Dr. Ananias Escalante](http://igem.temple.edu/people/person/c0ca56d9e60be58ca9380514ed8ac51d) (Temple University), [Dr. Maria Pacheco](http://igem.temple.edu/people/person/6417596d4976b9cbfa2a5ba8062ed7b9) (Temple University), [Dr. Dieter Lukas](http://dieterlukas.strikingly.com) (Max Planck Institute for Evolutionary Anthropology), [Dr. Claudia Wascher](https://www.claudiawascher.com) (Anglia Ruskin University)
2018-10-29

``` r
#Make code wrap text so it doesn't go off the page when Knitting to PDF
library(knitr)
opts_chunk$set(tidy.opts=list(width.cutoff=60),tidy=TRUE)
```

### A. STATE OF THE DATA

This preregistration was written prior to collecting any data (note the behavioral data are covered by separate preregistrations: [flexibility](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md), [causal cognition](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_causal.md), and [foraging](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexforaging.md)). Hypotheses H7 and H8 were added along with a new collaborator (Dieter Lukas) and intestinal parasites were added to H5 along with a new collaborator (Claudia Wascher) after 18 blood samples had been collected.

### B. PARTITIONING THE RESULTS

We may publish the results from each hypothesis separately.

### C. HYPOTHESES

The way we define flexibility (individuals change behavior according to changing circumstances using learning from previous experiences) assumes that being flexible will always be associated with the higher fitness payoff (e.g., higher quality food rewards). Therefore, the reasons individuals might not be flexible are 1) there are indirect costs to flexibility (e.g., exploration, risks involved in uncertain choices), 2) individuals live in environments that rarely change or change randomly, or 3) individuals have internal constraints (e.g., not enough energy). Points [1](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_exploration.md) and [2](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_expansion.md) are being tested in different preregistrations. Here we test point 3.

#### H1: Behavioral flexibility and cognitive performance on other tests negatively correlates with mounting a stress response (in response to being captured) because all three variables are energetically costly.

**Prediction 1:** Individuals with higher serum glucocorticoid concentrations at the time of capture will perform more poorly in causal inference experiments (see [causal cognition preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_causal.md)), solve fewer loci and switch between loci slower on the multi-access box, and require more trials to reverse preferences (see [flexibility preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md)).

**P1 alternative 1:** If flexibility positively correlates with serum glucocorticoid concentrations at the time of capture, this could be due to 1) the more dominant individuals incurring higher stress levels to maintain dominance, if the more dominant individuals are also more flexible; or 2) the more flexible individuals access higher quality resources and thus have more energy to mount a stress response.

**P1 alternative 2:** If flexibility and cognitive performance do not correlate with serum glucocorticoid concentrations at the time of capture, this indicates these traits are independent from each other or that they are related to another variable that was not measured.

#### H2: Behavioral flexibility and cognitive performance on other tests positively correlates with testosterone levels, as is found in other species (humans: Janowsky, Oviatt, and Orwoll (1994), Trumble et al. (2015); birds: C. K. Thompson and Brenowitz (2010)).

**P2:** Individuals with higher circulating testosterone will perform better in causal inference experiments (see [causal cognition preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_causal.md)), solve more loci and switch between loci faster on the multi-access box, and require fewer trials to reverse preferences (see [flexibility preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md)) because testosterone might have a neuroprotective effect (e.g., C. K. Thompson and Brenowitz (2010)), and higher levels of testosterone indicate better energetic condition.

**P2 alternative 1a:** If flexibility and cognitive performance are negatively correlated with testosterone, this might indicate a potential indirect link with immune function, which negatively correlates with testosterone levels (Janowsky, Oviatt, and Orwoll (1994), C. K. Thompson and Brenowitz (2010), Trumble et al. (2015)). If testosterone negatively correlates with immune function and immune function positively correlates with flexibility/cognition, then testosterone will negatively correlate with flexibility/cognition.

**P2 alternative 1b:** If flexibility negatively correlates with testosterone, but not other measures of condition, this might indicate that birds with higher testosterone are more invested in mating/competing, at a cost to flexibility and innovation. It may be that the less dominant birds have a greater need for flexibility due to their poorer ability to compete behaviorally with conspecifics.

**P2 alternative 2:** If flexibility and cognitive performance are not correlated with testosterone, this indicates these traits are independent from each other or that they are related to another variable that was not measured.

#### H3.1: There will be a negative correlation between behavioral flexibility and immune activation as a marker of poor condition.

**P3:** Individuals that are faster to reverse preferences (reversal learning) and switch to solving new options (multi-access box) (see [flexibility preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md)) will have lower total heterophil counts and lower levels of gene expression for inflammatory cytokines, due to their lower investment in actively fighting infections, leaving greater energy for cognitive resources such as flexibility.

**P3 alternative 1:** If no correlation is found, it is possible that this trade off is masked by a positive correlation between flexibility and testosterone (see H2; as in Janowsky, Oviatt, and Orwoll (1994), C. K. Thompson and Brenowitz (2010), Trumble et al. (2015)).

**P3 alternative 2:** If a positive correlation is found, this indicates that 1) there could be a threshold level of health (immune function) above which flexibility is promoted, or 2) flexibility is positively correlated with encountering more parasites, which increase the immune response.

#### H3.2: Individuals that are less [neophilic](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_exploration.md) will have higher immune activation and more immunosuppression.

**P4:** Individuals with elevated heterophils and inflammatory gene expression (immune activation) will avoid novel stimuli, due to the potential cost of exposure to novel parasites/pathogens. Similarly, individuals with low lymphocytes and low total leukocytes (which may indicate immunosuppression) may avoid novel pathogens.

**P4 alternative 1:** Alternatively, elevated heterophils and inflammatory cytokines may be protective against novel infections, rather than representing current infection. In this case they might be positively associated with neophilia.

**P4 alternative 2:** It is possible that neophilia increases exposure and thus leads to elevated heterophils and inflammation, thus the behavioral trait might cause the immune status. If this is supported, we expect other markers of infection to also positively associate with neophilia.

#### H3.3: There will be a positive correlation between flexibility and markers of basal immunity.

**P5:** We expect elevated lymphocytes, anti-inflammatory, and Th2 related gene expression (markers of basal immunity) to correlate with an increased ability to resist infection, and thus a greater capacity to invest in cognitively demanding tasks such as behavioral flexibility.

**P5 alternative 1:** Markers of basal immunity may be costly to maintain, and so may trade-off against costly cognitive abilities. However, such trade-offs may only be detectable after controlling for general markers of condition (see H4).

**P5 alternative 2:** There may be no correlation between immunity and flexibility at the individual level. They may simply be separate traits that assort independently.

#### H3.4: There will be a positive correlation between neophilia and markers of basal immunity

**P6:** We expect elevated lymphocytes, anti-inflammatory, and Th2 related gene expression (markers of basal immunity) to correlate with an increased ability to resist infection, and thus lower the cost of neophilia, resulting in greater neophilia.

**P6 alternative 1:** Markers of basal immunity may be costly to maintain and may indicate that an individual already has more available resources, thus lowering the need to seek new resources by investigating novel stimuli. If this is supported, we expect these individuals to already be in good condition (see H4).

**P6 alternative 2:** There may be no correlation between immunity and neophilia at the individual level. They may simply be separate traits that assort independently.

#### H4: Individuals that are more behaviorally flexible are in better condition (an indicator of available energy).

**P7:** A larger body size (heavier with longer tarsi, tails, and wings, higher hematocrit, higher red blood cell counts, and higher testosterone) will indicate better condition, and these individuals will be more flexible because they are less energetically constrained.

**P7 alternative 1:** If body size and flexibility negatively correlate, flexibility might relate less with condition and be used more as a strategy for competing with dominant conspecifics (thus investing more energy in competing rather than in flexibility).

**P7 alternative 2:** If body size and flexibility are not correlated, this indicates these traits are independent from each other or that they are related to another variable that was not measured.

#### H5: Individuals that are more behaviorally flexible have lower endoparasite loads (and thus a stronger immune system and more available energy).

**P8:** The more flexible individuals (on the multi-access box and in reversal learning) will have fewer haemosporidian parasite counts, lower haemosporidian parasite species diversity, and fewer fecal egg counts (an estimate of intestinal parasite load). We expect an individual’s physiological stress response (H1), immune system (H3), and condition (H3 and H4) to influence each other. Given that we do not yet know how these systems interact in great-tailed grackles, we expect that the flexible individuals will be less stressed and therefore ultimately in better condition. Regarding intestinal parasites, we expect individuals to be infected with a variety of nematode, coccidian and cestode species, most of which are directly transmitted via the fecal-oral route or via an intermediate host (e.g., earthworms, slugs). All individuals in a population are expected to be exposed to parasites in a similar way, but the more flexible individuals are expected be better able to cope with sources of stress (e.g., social stress) and therefore have a stronger immune system.

**P8 alternative 1:** If there is a positive relationship between flexibility and parasite loads (haemosporidian and/or intestinal), this could be because the more flexible individuals 1) eat a wider range of foods (see [foraging preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexforaging.md)) and roam a larger geographic area and are thus exposed to more parasites, and/or 2) might be in poorer energetic condition and more susceptible to hosting more species.

**P8 alternative 2:** If there is no correlation between flexibility and parasite loads, this could indicate that these variables are independent from each other or that they are related to another variable that was not measured.

#### H6: Individuals that are more behaviorally flexible have microbiomes with higher species diversity, which could facilitate the digestion of diverse foods and the adaptation to new parasites/bacteria (Alberdi et al. (2016)).

**P9:** The more flexible individuals will have a larger number of species in their microbiome, which could facilitate the digestion of novel foods and the adaptation to new parasites/bacteria.

**P9 alternative 1:** There is no difference in the number of species in the grackle microbiome in relation to flexibility, potentially because 1) there is little between individual variation in the number of microbiome species each grackle hosts which could be due to their exploiting similar food sources, and/or 2) these variables are independent from each other or are related to another variable that was not measured.

**P9 alternative 2** The more flexible individuals will host fewer microbiome species, potentially because they exploit different food sources than the less flexible individuals.

#### H7: Individuals that are more behaviorally flexible mate with individuals that are more flexible.

**P10:** The more flexible individuals will mate with individuals that are also more flexible, potentially because flexible individuals use different parts of the habitat and are therefore more likely to encounter each other. Flexibility will be measured in a separate [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md) and mate choice will be determined by genetically identifying the parents of offspring using ddRADseq.

**P10 alternative:** Traits other than flexibility determine who individuals mate with, for example, all females (not only the flexible ones) might choose males with longer tail feathers (Johnson et al. 2000), larger body sizes (Johnson et al. 2000), and/or specific territories.

#### H8: Individuals that are more behaviorally flexible have different fitness outcomes than the less flexible individuals. The following predictions are independent of each other and could indicate trade offs (i.e., there might be a positive association between flexibility and one fitness component, and a negative association with a different fitness component).

Flexibility will be measured in a separate [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md), maternity and paternity will be identified using ddRADseq, maternity will also be inferred using behavioral observations during the breeding season.

The fitness components we will measure are: - Females: number of eggs in the nest, number of nestlings, number of fledglings surviving to independence, number of offspring that survive to adulthood (1 year of age), adult survival between years, breeding probability in a given year. - Males: number of juveniles sired, number of offspring that survive to adulthood (1 year of age), adult survival between years, territory holder (yes, no) in a given year, number of females in their territory.

**P11** Roaming males have lower fitness (number of offspring sired) than territory-holding males (Johnson et al. 2000). If this relationship holds for the populations in our investigation, then we will further investigate whether flexibility is related to male territory-holding (P11a,b, P12a,b).

**P11a:** The territory-holding males during the breeding season will be more flexible and have higher paternity rates (Johnson et al. 2000) than roaming males. Territory-holding males might be better at 1) identifying better breeding habitats and/or 2) allying with other males to hold these territories. Territory-holding males will be identified using behavioral observations.

**P11a alternative:** The roaming males during the breeding season will be more flexible and have lower paternity rates (Johnson et al. 2000) than territory-holding males. Roaming males must sneak copulations with females who nest within another male's territory, which could select for an increase in flexible behavior.

**P11b:** The more flexible territory-holding males will have higher paternity rates and number of females nesting in their territories, than the less flexible territory-holding males. The more flexible territory-holding males might be better at 1) identifying better breeding habitats and/or 2) allying with other males to hold these territories.

**P11b alternative:** The more flexible territory-holding males will not have higher paternity rates and number of females nesting in their territories, than the less flexible territory-holding males potentially because body size or other variables might play a larger role (Johnson et al. 2000).

**P12:** The more flexible females will be better at keeping offspring alive either to the fledgling stage or to independence. Offspring survival will be measured through maternity identification of offspring who survived past one year of age.

**P12 alternative:** The more flexible females will not be better at keeping offspring alive, potentially because flexibility might be used for foraging and not in other contexts or, although there is variation in flexibility, the environment is more stable and flexibility does not ultimately offer an advantage.

**P13:** The more flexible individuals have higher survival between years potentially because they are better at coping with environmental change.

**P13 alternative 1:** The more flexible individuals have lower survival between years potentially because they encounter more risks.

**P13 alternative 2:** The more flexible individuals are not different in survival between years potentially because other variables are more strongly related to survival (e.g., immunity, parasite loads, etc.). The link between survival and flexibility is under investigation in H8 P12 above and in the [between population](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_expansion.md) preregistration.

**P14** The more flexible females will have a larger number of eggs and nestlings per breeding attempt, and have a higher breeding probability in a given year, potentially because they are in better condition (see H2, H3, and H5 above condition analyses).

**P14 alternative 1** The more flexible females will have a smaller number of eggs and nestlings per breeding attempt, and have a lower breeding probability in a given year, potentially because they are in worse condition (see H2, H3, and H5 above condition analyses).

**P14 alternative 2** There is no correlation between female flexibility and the number of eggs and nestlings per breeding attempt, and breeding probability in a given year, potentially because flexibility is not associated with condition (see H2, H3, and H5 above condition analyses).

### D. METHODS

#### **Randomization and counterbalancing**

No randomization or counterbalancing is involved in this study.

#### **Blinding of conditions during analysis**

No blinding is involved in this study.

#### **Dependent variables**

#### *P1-P15*

1.  Flexibility 1: **Number of trials to reverse** a preference in the last reversal an individual experienced (reversal learning; an individual is considered to have a preference if it chose the rewarded option at least 17 out of the most recent 20 trials, with a minimum of 8 or 9 correct choices out of 10 on the two most recent sets of 10 trials). See behavioral flexibility [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md).

2.  Flexibility 2: The **ratio of correct divided by incorrect trials** for the first 40 trials in their final reversal after the individual has seen the newly rewarded option once. These 40 trials include trials where individuals were offered the test and chose not to participate (i.e., make a choice). This accounts for flexibility that can occur when some individuals inhibit their previously rewarded preference (thus exhibiting flexibility because they changed their behavior when circumstances changed), but are not as exploratory as those who have fewer 'no choice' trials. 'No choice' data is data that is otherwise excluded from standard reversal learning analyses. Including 'no choice' trials, controls for individual differences in exploration because those that refuse to choose are not exploring new options, which would allow them to learn the new food location.

3.  Flexibility 3: If the number of trials to reverse a preference does not positively correlate with the latency to attempt or solve new loci on the multi-access box (an additional measure of behavioral flexibility), then the **average latency to solve** and the **average latency to attempt** a new option on the multi-access box will be additional dependent variables. See behavioral flexibility [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md).

One model will be run per dependent variable.

#### *H3.2 and H3.4: neophilia and immunity*

Neophilia: Latency to land on the table next to an object (novel, familiar) (that does not contain food) in a familiar environment (that contains maintenance diet away from the object) - OR - latency to touch an object (novel, familiar) (choose the variable with the most data)

#### *P1 alternative 1: stress and dominance*

Dominance rank

#### *P7 alternative 1: condition and dominance*

Dominance rank

#### *P8 alternative 1: haemosporidian parasites and foods eaten*

Number of different food items eaten

#### *P10: assortative mating*

Flexibility of females (flexibility measures 1, 2, and 3)

#### *P11: territory-holding males higher fitness than roaming*

Number of offspring sired

#### *P11a: territory-holding males more flexible than roaming*

Territory-holding (yes, no)

#### *P11b: territory-holding males more flexible than roaming*

Number of offspring per territory-holder

#### *P12: female flexibility and offspring survival*

Number of fledglings

Number of offspring surviving past 1 year of age

#### *P13: flexibility and adult survival*

Probability of resighting an individual in multiple years

#### *P14: female flexibility and eggs, nestlings, breeding probability*

Number of eggs in the nest

Number of nestlings

Breeding probability in a given year

#### **Independent variables**

#### *P1-P9*

1.  P1 stress: serum glucocorticoid concentration

2.  P2: testosterone concentration (note: also a measure of condition \[P7\])

3.  P3 and P4 immunity: heterophil counts

4.  P3 and P4 immunity: inflammatory gene expression

5.  P5 and P6 immunity: total leucocyte counts

6.  P5 and P6 immunity: total lymphocyte counts

7.  P5 and P6 immunity: anti-inflammatory and Th2 gene expression

8.  P7 condition: hematocrit

9.  P7 condition: red blood cell counts

10. P7 condition: body weight (wild)

11. P7 condition: tarsus length (average left and right legs)

12. P7 condition: tail length (average left and right central retrices)

13. P7 condition: wing length (average left and right wing chords)

14. P8 parasites: number of parasites (haemosporidian and inetestinal) per grackle

15. P8 parasites: number of parasites species per grackle

16. P9 microbiome: number of microbiome species per grackle

17. Population (as a random effect to examine within population variation)

#### *P1 alternative 1: stress and dominance*

1.  Serum glucocorticoid concentration

2.  Flexibility 1: Number of trials to reverse last preference (see above)

3.  Flexibility 2: Flexibility ratio (see above)

4.  Population (as a random effect to examine within population variation)

#### *P7 alternative 1: condition and dominance*

1.  Condition: body weight (wild)

2.  Condition: tarsus length (average left and right legs)

3.  Condition: tail length (average left and right central retrices)

4.  Condition: wing length (average left and right wing chords)

5.  Condition: hematocrit

6.  Condition: red blood cell counts

7.  Condition: testosterone concentration

8.  Flexibility 1: Number of trials to reverse last preference (see above)

9.  Flexibility 2: Flexibility ratio (see above)

10. Population (as a random effect to examine within population variation)

#### *P8 alternative 1: parasites and foods eaten*

1.  Parasites: number of haemosporidian parasites per sample

2.  Parasites: number of haemosporidian parasites species per sample

3.  Parasites: number of intestinal parasite eggs and oocysts per sample

4.  Flexibility 1: Number of trials to reverse last preference (see above)

5.  Flexibility 2: Flexibility ratio (see above)

6.  Population (as a random effect to examine within population variation)

#### *P10: assortative mating*

1.  Flexibility 1 of mate

2.  Flexibility 2 of mate

3.  Flexibility 3 of mate

#### *P11: territory-holding males higher fitness than roaming*

1.  Territory-holding (yes, no)

#### *P11a-P14:*

1.  Flexibility 1

2.  Flexibility 2

3.  Flexibility 3

### E. ANALYSIS PLAN

We do not plan to **exclude** any data. When **missing data** occur, the existing data for that individual will be included in the analyses for the tests they completed. Analyses will be conducted in R (current version 3.3.3; R Core Team (2017)). We will analyze data for females and males separately because each sex has a distinct natural history (Johnson and Peer (2001)).

#### *Data checking*

The data will be visually checked to determine whether they are normally distributed via two methods: 1) normality is indicated when the histograms of actual data match those with simulated data (Figure 2), and 2) normality is indicated when the residuals closely fit the dotted line in the Normal Q-Q plot (Figure 3) (Zuur, Ieno, and Saveliev 2009).

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# Check the dependent variables for normality: Histograms
# females
op <- par(mfrow = c(2, 5), mar = c(4, 4, 2, 0.2))
# This is what the distribution of actual data looks like
hist(fem$TrialsToReverseLast, xlab = "Flexibility: Trials to reverse", 
    main = "Actual Data (females)")
hist(fem$FlexRatio, xlab = "Flexibility: Ratio of correct responses", 
    main = "Actual Data (females)")
hist(fem$DominanceRank, xlab = "Dominance rank", main = "Actual Data (females)")
hist(fem$NumberFoodsEaten, xlab = "Number of foods eaten/individual", 
    main = "Actual Data (females)")
hist(fem$Neophilia, xlab = "Neophilia (latency)", main = "Actual Data (females)")


# Given the actual data, this is what a normal distribution
# would look like
W2 <- rnorm(1281, mean = mean(fem$TrialsToReverseLast), sd = sd(fem$TrialsToReverseLast))
hist(W2, xlab = "Flexibility: Trials to reverse (females)", main = "Simulated Data")

X2 <- rnorm(1281, mean = mean(fem$FlexRatio), sd = sd(fem$FlexRatio))
hist(X2, xlab = "Flexibility: Ratio of correct responses (females)", 
    main = "Simulated Data")

Y2 <- rnorm(1281, mean = mean(fem$DominanceRank), sd = sd(fem$DominanceRank))
hist(Y2, xlab = "Dominance rank (females)", main = "Simulated Data")

Z2 <- rnorm(1281, mean = mean(fem$NumberFoodsEaten), sd = sd(fem$NumberFoodsEaten))
hist(Z2, xlab = "Number of foods eaten/individual (females)", 
    main = "Simulated Data")

V2 <- rnorm(1281, mean = mean(fem$Neophilia), sd = sd(fem$Neophilia))
hist(V2, xlab = "Neophilia latency (females)", main = "Simulated Data")


# Check the dependent variables for normality: Q-Q plots
# (females)
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(glm(fem$TrialsToReverseLast ~ fem$Cort))
plot(glm(fem$DominanceRank ~ fem$Cort))
plot(glm(fem$NumberFoodsEaten ~ fem$NumberParasites))
plot(glm(fem$Neophilia ~ fem$Cort))

# males
op <- par(mfrow = c(2, 5), mar = c(4, 4, 2, 0.2))
# This is what the distribution of actual data looks like
hist(mal$TrialsToReverseLast, xlab = "Flexibility: Trials to reverse", 
    main = "Actual Data (males)")
hist(mal$FlexRatio, xlab = "Flexibility: Ratio of correct responses", 
    main = "Actual Data (males)")
hist(mal$DominanceRank, xlab = "Dominance rank", main = "Actual Data (males)")
hist(mal$NumberFoodsEaten, xlab = "Number of foods eaten/individual", 
    main = "Actual Data (males)")
hist(mal$Neophilia, xlab = "Neophilia (latency)", main = "Actual Data (males)")

# Given the actual data, this is what a normal distribution
# would look like
A2 <- rnorm(1281, mean = mean(mal$TrialsToReverseLast), sd = sd(mal$TrialsToReverseLast))
hist(A2, xlab = "Flexibility: Trials to reverse (males)", main = "Simulated Data")

B2 <- rnorm(1281, mean = mean(mal$FlexRatio), sd = sd(mal$FlexRatio))
hist(B2, xlab = "Flexibility: Ratio of correct responses (males)", 
    main = "Simulated Data")

C2 <- rnorm(1281, mean = mean(mal$DominanceRank), sd = sd(mal$DominanceRank))
hist(C2, xlab = "Dominance rank (males)", main = "Simulated Data")

D2 <- rnorm(1281, mean = mean(mal$NumberFoodsEaten), sd = sd(mal$NumberFoodsEaten))
hist(D2, xlab = "Number of foods eaten/individual (males)", main = "Simulated Data")

E2 <- rnorm(1281, mean = mean(mal$Neophilia), sd = sd(mal$Neophilia))
hist(D2, xlab = "Neophilia latency (males)", main = "Simulated Data")

# Check the dependent variables for normality: Q-Q plots
# (males)
op <- par(mfrow = c(4, 4), mar = c(4, 4, 2, 0.2))
plot(glm(mal$TrialsToReverseLast ~ mal$Cort))
plot(glm(mal$DominanceRank ~ mal$Cort))
plot(glm(mal$NumberFoodsEaten ~ mal$NumberParasites))
plot(glm(mal$Neophilia ~ mal$Cort))
```

If the data do not appear normally distributed, visually check the residuals. If they are patternless, then assume a normal distribution (Figure 4) (Zuur, Ieno, and Saveliev 2009).

``` r
# Check the dependent variables for normality: Residuals
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# Figure 3. Visual check of the residuals females
op <- par(mfrow = c(2, 2), mar = c(4, 4, 2, 0.2))
plot(residuals(glm(fem$TrialsToReverseLast ~ fem$Cort)), ylab = "Flexibility residuals: trials to reverse ~ cort")
plot(residuals(glm(fem$DominanceRank ~ fem$Cort)), ylab = "Residuals: dominance rank ~ cort")
plot(residuals(glm(fem$NumberFoodsEaten ~ fem$NumberParasites)), 
    ylab = "Residuals: foods eaten ~ number of parasites")
plot(residuals(glm(fem$Neophilia ~ fem$Cort)), ylab = "Residuals: neophilia ~ cort")

# males
op <- par(mfrow = c(2, 2), mar = c(4, 4, 2, 0.2))
plot(residuals(glm(mal$TrialsToReverseLast ~ mal$Cort)), ylab = "Flexibility residuals: trials to reverse ~ cort")
plot(residuals(glm(mal$DominanceRank ~ mal$Cort)), ylab = "Residuals: dominance rank ~ cort")
plot(residuals(glm(mal$NumberFoodsEaten ~ mal$NumberParasites)), 
    ylab = "Residuals: foods eaten ~ number of parasites")
plot(residuals(glm(mal$Neophilia ~ mal$Cort)), ylab = "Residuals: neophilia ~ cort")
```

#### *P1, P3, P5, P8: flexibility trade offs*

**Analysis:** Because the independent variables could influence each other, we will analyze them in a single model: Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

To be able to detect trade offs, we need to control for condition, therefore we chose the average tarsus length as the representative measure of condition (a random effect).

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0), R2 = list(V = 1, 
    nu = 0), R3 = list(V = 1, nu = 0), R4 = list(V = 1, nu = 0), 
    R5 = list(V = 1, nu = 0), R6 = list(V = 1, nu = 0), R7 = list(V = 1, 
        nu = 0), R8 = list(V = 1, nu = 0), R9 = list(V = 1, nu = 0)), 
    G = list(G1 = list(V = 1, nu = 0), G2 = list(V = 1, nu = 0)))

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# GLMM with response variable = trials to reverse the last
# preference females
f1 <- MCMCglmm(TrialsToReverseLast ~ Cort + NumberHeterophil + 
    NumberLymphocytes + InflammatoryGene + NumberLeucocytes + 
    AntiInflammatoryGene + Th2Gene + NumberParasites + NumberParasiteSpecies, 
    random = ~Population + AvgTarsusLength, family = "poisson", 
    data = fem, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(TrialsToReverseLast ~ Cort + NumberHeterophil + 
    NumberLymphocytes + InflammatoryGene + NumberLeucocytes + 
    AntiInflammatoryGene + Th2Gene + NumberParasites + NumberParasiteSpecies, 
    random = ~Population + AvgTarsusLength, family = "poisson", 
    data = mal, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?


# GLMM with response variable = flexibility ratio females
f2 <- MCMCglmm(TrialsToReverseLast ~ Cort + NumberHeterophil + 
    NumberLymphocytes + InflammatoryGene + NumberLeucocytes + 
    AntiInflammatoryGene + Th2Gene + NumberParasites + NumberParasiteSpecies, 
    random = ~Population + AvgTarsusLength, family = "poisson", 
    data = fem, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(f2)
# autocorr(f2$Sol) #Did fixed effects converge?
# autocorr(f2$VCV) #Did random effects converge?

# males
m2 <- MCMCglmm(TrialsToReverseLast ~ Cort + NumberHeterophil + 
    NumberLymphocytes + InflammatoryGene + NumberLeucocytes + 
    AntiInflammatoryGene + Th2Gene + NumberParasites + NumberParasiteSpecies, 
    random = ~Population + AvgTarsusLength, family = "poisson", 
    data = mal, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(m2)
# autocorr(m2$Sol) #Did fixed effects converge?
# autocorr(m2$VCV) #Did random effects converge?
```

#### *P4 and P6: neophilia and immunity*

**Analysis:** Because the independent variables could influence each other, we will analyze them in a single model: Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

To be able to detect trade offs, we need to control for condition, therefore we chose the average tarsus length as the representative measure of condition (a random effect).

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0), R2 = list(V = 1, 
    nu = 0), R3 = list(V = 1, nu = 0), R4 = list(V = 1, nu = 0), 
    R5 = list(V = 1, nu = 0), R6 = list(V = 1, nu = 0)), G = list(G1 = list(V = 1, 
    nu = 0), G2 = list(V = 1, nu = 0)))

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# GLMM with response variable = neophilia (latency) females
f1 <- MCMCglmm(Neophilia ~ NumberHeterophil + NumberLymphocytes + 
    InflammatoryGene + NumberLeucocytes + AntiInflammatoryGene + 
    Th2Gene, random = ~Population + AvgTarsusLength, family = "poisson", 
    data = fem, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(Neophilia ~ NumberHeterophil + NumberLymphocytes + 
    InflammatoryGene + NumberLeucocytes + AntiInflammatoryGene + 
    Th2Gene, random = ~Population + AvgTarsusLength, family = "poisson", 
    data = mal, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?
```

#### *P2, P7, P9: flexibility vs testosterone/condition*

**Analysis:** Because the independent variables could influence each other, we will analyze them in a single model: Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0), R2 = list(V = 1, 
    nu = 0), R3 = list(V = 1, nu = 0), R4 = list(V = 1, nu = 0), 
    R5 = list(V = 1, nu = 0), R6 = list(V = 1, nu = 0), R7 = list(V = 1, 
        nu = 0), R8 = list(V = 1, nu = 0)), G = list(G1 = list(V = 1, 
    nu = 0)))

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# GLMM with response variable = trials to reverse the last
# preference females
f1 <- MCMCglmm(TrialsToReverseLast ~ Testosterone + Hematocrit + 
    NumberRedBloodCells + Weight + AvgTarsusLength + AvgTailLength + 
    AvgWingLength + NumberMicrobiomeSpecies, random = ~Population, 
    family = "poisson", data = fem, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(TrialsToReverseLast ~ Testosterone + Hematocrit + 
    NumberRedBloodCells + Weight + AvgTarsusLength + AvgTailLength + 
    AvgWingLength + NumberMicrobiomeSpecies, random = ~Population, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?


# GLMM with response variable = flexibility ratio females
f2 <- MCMCglmm(FlexRatio ~ Testosterone + Hematocrit + NumberRedBloodCells + 
    Weight + AvgTarsusLength + AvgTailLength + AvgWingLength + 
    NumberMicrobiomeSpecies, random = ~Population, family = "poisson", 
    data = fem, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(f2)
# autocorr(f2$Sol) #Did fixed effects converge?
# autocorr(f2$VCV) #Did random effects converge?

# males
m2 <- MCMCglmm(FlexRatio ~ Testosterone + Hematocrit + NumberRedBloodCells + 
    Weight + AvgTarsusLength + AvgTailLength + AvgWingLength + 
    NumberMicrobiomeSpecies, random = ~Population, family = "poisson", 
    data = mal, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(m2)
# autocorr(m2$Sol) #Did fixed effects converge?
# autocorr(m2$VCV) #Did random effects converge?
```

#### *P1 alternative 1: stress and dominance*

**Analysis:** We will conduct the analysis using a Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0), R2 = list(V = 1, 
    nu = 0), R3 = list(V = 1, nu = 0)), G = list(G1 = list(V = 1, 
    nu = 0)))

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# GLMM females
f1 <- MCMCglmm(DominanceRank ~ Cort + TrialsToReverseLast + FlexRatio, 
    random = ~Population, family = "poisson", data = fem, verbose = F, 
    prior = prior, nitt = 130000, thin = 10, burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(TrialsToReverseLast ~ Cort + TrialsToReverseLast + 
    FlexRatio, random = ~Population, family = "poisson", data = mal, 
    verbose = F, prior = prior, nitt = 130000, thin = 10, burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?
```

#### *P7 alternative 1: condition and dominance*

**Analysis:** We will conduct the analysis using a Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0), R2 = list(V = 1, 
    nu = 0), R3 = list(V = 1, nu = 0), R4 = list(V = 1, nu = 0), 
    R5 = list(V = 1, nu = 0), R6 = list(V = 1, nu = 0), R7 = list(V = 1, 
        nu = 0), R8 = list(V = 1, nu = 0), R9 = list(V = 1, nu = 0)), 
    G = list(G1 = list(V = 1, nu = 0)))

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# GLMM females
f1 <- MCMCglmm(DominanceRank ~ Weight + AvgTarsusLength + AvgTailLength + 
    AvgWingLength + Hematocrit + NumberRedBloodCells + Testosterone + 
    TrialsToReverseLast + FlexRatio, random = ~Population, family = "poisson", 
    data = fem, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(DominanceRank ~ Weight + AvgTarsusLength + AvgTailLength + 
    AvgWingLength + TrialsToReverseLast + FlexRatio, random = ~Population, 
    family = "poisson", data = mal, verbose = F, prior = prior, 
    nitt = 130000, thin = 10, burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?
```

#### *P8 alternative 1: haemosporidian parasites and foods eaten*

**Analysis:** We will conduct the analysis using a Generalized Linear Mixed Model (GLMM; MCMCglmm function, MCMCglmm package; (Hadfield 2010)) with a Poisson distribution and log link using 130,000 iterations with a thinning interval of 10, a burnin of 30,000, and minimal priors (V=1, nu=0) (Hadfield 2014). We will ensure the GLMM shows acceptable convergence (lag time autocorrelation values &lt;0.01; (Hadfield 2010)), and adjust parameters if necessary to meet this criterion. The contribution of each independent variable will be evaluated using the Estimate in the full model.

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# GLMM
library(MCMCglmm)
prior = list(R = list(R1 = list(V = 1, nu = 0), R2 = list(V = 1, 
    nu = 0), R3 = list(V = 1, nu = 0), R4 = list(V = 1, nu = 0)), 
    G = list(G1 = list(V = 1, nu = 0)))

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# GLMM females
f1 <- MCMCglmm(NumberFoodsEaten ~ NumberParasites + NumberParasiteSpecies + 
    TrialsToReverseLast + FlexRatio, random = ~Population, family = "poisson", 
    data = fem, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(f1)
# autocorr(f1$Sol) #Did fixed effects converge?
# autocorr(f1$VCV) #Did random effects converge?

# males
m1 <- MCMCglmm(NumberFoodsEaten ~ NumberParasites + NumberParasiteSpecies + 
    TrialsToReverseLast + FlexRatio, random = ~Population, family = "poisson", 
    data = mal, verbose = F, prior = prior, nitt = 130000, thin = 10, 
    burnin = 30000)
summary(m1)
# autocorr(m1$Sol) #Did fixed effects converge?
# autocorr(m1$VCV) #Did random effects converge?
```

#### *P9 alternative 1: individual variation in microbiome species diversity*

We will visually examine individual variation in the number of microbiome species hosted by each grackle using a scatterplot (Figure 5).

``` r
main <- read.csv("/Users/corina/GTGR/data/data_pop.csv", header = T, 
    sep = ",", stringsAsFactors = F)

# Separate the sexes
fem <- main[main$Sex == "f", ]
mal <- main[main$Sex == "m", ]

# Plot
op <- par(mfrow = c(1, 2), mar = c(4, 4, 2, 0.2))
plot(fem$ID, fem$NumberMicrobiomeSpecies, xlab = "Grackle ID (females)", 
    ylab = "Number of species in the microbiome")
plot(mal$ID, mal$NumberMicrobiomeSpecies, xlab = "Grackle ID (males)", 
    ylab = "Number of species in the microbiome")
```

#### *Alternative Analyses*

We will perform network analyses or factor analyses on the gene expression data, however we are still learning about these analyses so we will revise this preregistration to include these new analyses before conducting the analyses above.

We anticipate that we will want to run additional/different analyses after reading McElreath (2016). We will revise this preregistration to include these new analyses before conducting the analyses above.

### F. PLANNED SAMPLE

Great-tailed grackles (n &gt; 200) will be caught in the wild at three field sites across their geographic range: the center of their original range (at a site to be determined in Central America), the middle of the northward expanding edge (Tempe, Arizona USA), and on the northern expanding edge (to be determined). Individuals will be identified using colored leg bands in unique combinations, their data collected (blood, feathers, and biometrics), and then they will be released back to the wild. Some individuals (60-100) will be brought temporarily into aviaries for behavioral testing, and then they will be released back to the wild.

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

**Logan:** Hypothesis development, study design, materials, data collection, data analysis and interpretation, write up, revising/editing, funding.

**Rowney:** Data collection, data interpretation, revising/editing.

**Bergeron:** Data collection, data interpretation, revising/editing.

**McCune:** Data collection, data interpretation, revising/editing.

**Trumble (testosterone and glucocorticoids):** Hypothesis development, materials/lab space, sample processing, data analysis and interpretation, write up, revising/editing.

**Blackwell (immune function):** Hypothesis development, materials/lab space, sample processing, data analysis and interpretation, write up, revising/editing.

**Escalante (haemosporidian parasites and microbiome):** Hypothesis development, data analysis and interpretation, write up, revising/editing.

**Pacheco (haemosporidian parasites and microbiome):** Hypothesis development, materials/lab space, sample processing, data analysis and interpretation, write up, revising/editing.

**Lukas (genetics):** Hypothesis development, data analysis and interpretation, write up, revising/editing.

**Wascher (intestinal parasites):** Hypothesis development, data analysis and interpretation, write up, revising/editing.

### I. FUNDING

This research is funded by the Department of Human Behavior, Ecology and Culture at the Max Planck Institute for Evolutionary Anthropology, and in 2017-2018 by a Leverhulme Early Career Research Fellowship to Logan.

### J. ACKNOWLEDGEMENTS

We thank Ben Trumble for hosting the grackle project at Arizona State University (providing office and lab space); Melissa Wilson Sayres for sponsoring our affiliations at Arizona State University and lending lab equipment; Kristine Johnson for technical advice on great-tailed grackles; Jay Taylor for grackle scouting; and Arizona State University School of Life Sciences Department Animal Care and Technologies for providing space for our aviaries and for their excellent support of our daily activities.

### K. REFERENCES

Alberdi, Antton, Ostaizka Aizpurua, Kristine Bohmann, Marie Lisandra Zepeda-Mendoza, and M Thomas P Gilbert. 2016. “Do Vertebrate Gut Metagenomes Confer Rapid Ecological Adaptation?” *Trends in Ecology & Evolution* 31 (9). Elsevier: 689–99.

Hadfield, JD. 2010. “MCMC Methods for Multi-Response Generalized Linear Mixed Models: The Mcmcglmm R Package.” *Journal of Statistical Software* 33 (2): 1–22.

———. 2014. “MCMCglmm Course Notes.” <http://cran.r-project.org/web/packages/MCMCglmm/vignettes/CourseNotes.pdf>.

Janowsky, Jeri S, Shelia K Oviatt, and Eric S Orwoll. 1994. “Testosterone Influences Spatial Cognition in Older Men.” *Behavioral Neuroscience* 108 (2). American Psychological Association: 325.

Johnson, Kristine, and Brian D Peer. 2001. *Great-Tailed Grackle: Quiscalus Mexicanus*. Birds of North America, Incorporated.

Johnson, Kristine, Emily DuVal, Megan Kielt, and Colin Hughes. 2000. “Male Mating Strategies and the Mating System of Great-Tailed Grackles.” *Behavioral Ecology* 11 (2). Oxford University Press: 132–41.

McElreath, Richard. 2016. *Statistical Rethinking: A Bayesian Course with Examples in R and Stan*. CRC Press. <http://xcelab.net/rm/statistical-rethinking/>.

R Core Team. 2017. *R: A Language and Environment for Statistical Computing*. Vienna, Austria: R Foundation for Statistical Computing. <https://www.R-project.org>.

Thompson, Christopher K, and Eliot A Brenowitz. 2010. “Neuroprotective Effects of Testosterone in a Naturally Occurring Model of Neurodegeneration in the Adult Avian Song Control System.” *Journal of Comparative Neurology* 518 (23). Wiley Online Library: 4760–70.

Trumble, Benjamin C, Jonathan Stieglitz, Melissa Emery Thompson, Eric Fuerstenberg, Hillard Kaplan, and Michael Gurven. 2015. “Testosterone and Male Cognitive Performance in Tsimane Forager-Horticulturalists.” *American Journal of Human Biology* 27 (4). Wiley Online Library: 582–86.

Zuur, Alain F.., Elena N.. Ieno, and Anatoly A Saveliev. 2009. *Mixed Effects Models and Extensions in Ecology with R*. Springer.