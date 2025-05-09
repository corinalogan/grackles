**NOTE! This .md file has been replaced with an easier-to-read html version. Please read the html version instead by [clicking here](http://corinalogan.com/Preregistrations/g_flexgenes.html)**

The genetics of behavioral flexibility across the range of a rapidly expanding species
================
[Dr. Corina Logan](http://CorinaLogan.com) (Max Planck Institute for Evolutionary Anthropology, <corina_logan@eva.mpg.de>), Carolyn Rowney (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), Luisa Bergeron (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), Dr. Kelsey McCune (University of California Santa Barbara / Max Planck Institute for Evolutionary Anthropology), Dr. Angela Bond (Arizona State University), [Dr. Aaron Blackwell](http://www.anth.ucsb.edu/faculty/blackwell/) (University of California, Santa Barbara), [Dr. Dieter Lukas](http://dieterlukas.strikingly.com) (Max Planck Institute for Evolutionary Anthropology)
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

### C. RESEARCH QUESTIONS

#### R1 heritability: To what extent is variation in behavioral flexibility explained by genetic similarity?

Based on [flexibility testing in aviaries](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md), we will develop a flexibility test for individuals in the wild to increase our sample size. Genetic relationships among individuals will be determined using ddRADseq to then investigate this question using the Animal Model. If flexibility is not heritable, this is potentially because behavior is not usually very heritable, and/or we might fail to detect heritability because the A) sample size might not be large enough, and/or B) individuals may not vary enough in flexibility. If we find that flexibility is heritable, this could indicate that there is a stable polymorphism where some individuals have high and others low flexibility, which could give different benefits in a given environment.

#### R2 genetic architecture: Is variation in behavioral flexibility explained by variation in specific genetic loci (e.g., DRD4) or their expression?

Based on [flexibility testing in aviaries](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md), we will develop a flexibility test for individuals in the wild to increase our sample size. Genetic variation of individuals will be determined using ddRADseq and gene expression will be determined using RNA sequencing.

**R2.1 individual** Do the more flexible individuals carry or express genetic variants at specific loci that differ from the less flexible individuals? Genetic variants will be identified using genome wide association studies (GWAS).

**R2.2 candidate loci** Is one variant of the genetic locus DRD4 (associated with exploratory behavior) primarily present in the more flexible individuals, while the other variant is primarily present in the less flexible individuals?

#### R3: When did the populations in our sample originate and what was the likely geographic spread of great-tailed grackles across North America?

Genetic variation of individuals will be determined using ddRADseq, and coalescence simulations will be used with the ddRADseq data to determine the common ancestors and timing of divergence of the populations we sample.

### D. METHODS

#### **Randomization and counterbalancing**

No randomization or counterbalancing is involved in this study.

#### **Blinding of conditions during analysis**

No blinding is involved in this study.

#### **Dependent variables**

#### *R1 & R2*

1.  Flexibility 1: **Number of trials to reverse** a preference in the last reversal an individual experienced (reversal learning; an individual is considered to have a preference if it chose the rewarded option at least 17 out of the most recent 20 trials, with a minimum of 8 or 9 correct choices out of 10 on the two most recent sets of 10 trials). See behavioral flexibility [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md).

2.  Flexibility 2: The **ratio of correct divided by incorrect trials** for the first 40 trials in their final reversal after the individual has seen the newly rewarded option once. These 40 trials include trials where individuals were offered the test and chose not to participate (i.e., make a choice). This accounts for flexibility that can occur when some individuals inhibit their previously rewarded preference (thus exhibiting flexibility because they changed their behavior when circumstances changed), but are not as exploratory as those who have fewer 'no choice' trials. 'No choice' data is data that is otherwise excluded from standard reversal learning analyses. Including 'no choice' trials, controls for individual differences in exploration because those that refuse to choose are not exploring new options, which would allow them to learn the new food location.

3.  Flexibility 3: If the number of trials to reverse a preference does not positively correlate with the latency to attempt or solve new loci on the multi-access box (an additional measure of behavioral flexibility), then the **average latency to solve** and the **average latency to attempt** a new option on the multi-access box will be additional dependent variables. See behavioral flexibility [preregistration](https://github.com/corinalogan/grackles/blob/master/EasyToReadFiles/g_flexmanip.md).

One model will be run per dependent variable.

#### *R3: pop age and spread*

Model parameters: absolute and change in population size, time, frequency of exchange of individuals/genes between populations. We will then run a simulation and find the combination of values for the parameters that produce the closest fit to the actual data.

#### **Independent variables**

#### *R1: heritability of flexibility*

1.  Age: adult, juvenile

2.  Body size: tarsus length

3.  Body condition: hematocrit (percentage of red blood cells in the blood)

4.  Number of parasite species hosted

5.  Population: Central America, Arizona, Nebraska

6.  Birth year (random effect)

7.  Pedigree (random effect)

#### *R2.1: Do the more flexible individuals carry or express genetic variants at specific loci that differ from the less flexible individuals?*

1.  Each genetic variant (allele)

#### *R2.2: Is one variant of the genetic locus DRD4 (associated with exploratory behavior) primarily present in the more flexible individuals*

1.  Each genetic variant (allele)

### E. ANALYSIS PLAN

We do not plan to **exclude** any data. When **missing data** occur, the existing data for that individual will be included in the analyses for the tests they completed. Analyses will be conducted in R (current version 3.3.3; R Core Team (2017)). We will analyze data for females and males separately because each sex has a distinct natural history (Johnson and Peer (2001)).

*NOTE: the analysis plan is still being drafted*

#### *Data checking*

#### *R1*

#### *R2.1*

#### *R2.2*

#### *R3: population origin time and spread*

### F. PLANNED SAMPLE

Great-tailed grackles (n &gt; 200) will be caught in the wild at three field sites across their geographic range: the center of their original range (Central America), the middle of the northward expanding edge (Tempe, Arizona USA), and on the northern expanding edge (to be determined). Individuals will be identified using colored leg bands in unique combinations, their data collected (blood, feathers, and biometrics), and then they will be released back to the wild. Some individuals (40-100) will be brought temporarily into aviaries for behavioral testing, and then they will be released back to the wild.

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

### H. AUTHOR CONTRIBUTIONS

**Logan:** Hypothesis development, study design, materials, data collection, data analysis and interpretation, write up, funding.

**Rowney:** Data collection, sample processing, data analysis and interpretation, editing/revising.

**Bergeron:** Data collection, sample processing, data analysis and interpretation, editing/revising.

**McCune:** Data collection, sample processing, data analysis and interpretation, editing/revising.

**Blackwell:** Hypothesis development, study design, data analysis and interpretation, write up.

**Lukas:** Hypothesis development, study design, data analysis and interpretation, write up.

### I. FUNDING

This research is funded by the Department of Human Behavior, Ecology and Culture at the Max Planck Institute for Evolutionary Anthropology.

### J. ACKNOWLEDGEMENTS

We thank Ben Trumble for hosting the grackle project at Arizona State University (providing office and lab space); Melissa Wilson Sayres for sponsoring our affiliations at Arizona State University and lending lab equipment; Kristine Johnson for technical advice on great-tailed grackles; Jay Taylor for grackle scouting; Arizona State University School of Life Sciences Department Animal Care and Technologies for providing space for our aviaries and for their excellent support of our daily activities; and Cornell University (Irby Lovette and Bronwyn Butcher) for letting us use their lab to process the DNA and for teaching us how.

### K. REFERENCES

Johnson, Kristine, and Brian D Peer. 2001. *Great-Tailed Grackle: Quiscalus Mexicanus*. Birds of North America, Incorporated.

R Core Team. 2017. *R: A Language and Environment for Statistical Computing*. Vienna, Austria: R Foundation for Statistical Computing. <https://www.R-project.org>.
