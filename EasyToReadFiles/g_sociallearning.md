Investigating the use of learning mechanisms in a species that is rapidly expanding its geographic range
================
Dr. Kelsey McCune (University of California Santa Barbara), [Dr. Richard McElreath](http://xcelab.net/rm/) (Max Planck Institute for Evolutionary Anthropology), [Dr. Corina Logan](http://CorinaLogan.com) (Max Planck Institute for Evolutionary Anthropology, <corina_logan@eva.mpg.de>)
2019-05-07

-   [ABSTRACT](#abstract)
-   [A. STATE OF THE DATA](#a.-state-of-the-data)
-   [B. HYPOTHESIS](#b.-hypothesis)
-   [C. METHODS](#c.-methods)
-   [D. ANALYSIS PLAN](#d.-analysis-plan)
-   [E. REFERENCES](#e.-references)

### ABSTRACT

This is one of many studies planned for our long-term research on the role of behavioral flexibility in rapid geographic range expansions. **Project background:** Behavioral flexibility, the ability to change behavior when circumstances change based on learning from previous experience (Mikhalevich, Powell, and Logan (2017)), is thought to play an important role in a species' ability to successfully adapt to new environments and expand its geographic range (e.g., (Lefebvre et al. 1997), (Griffin and Guez 2014), (Chow, Lea, and Leaver 2016), (Sol and Lefebvre 2000), (Sol, Timmermans, and Lefebvre 2002), (Sol et al. 2005)). However, behavioral flexibility is rarely directly tested at the individual level, thus limiting our ability to determine how it relates to other traits, which limits the power of predictions about a species' ability to adapt behavior to new environments. We use great-tailed grackles (a bird species) as a model to investigate this question because they have rapidly expanded their range into North America over the past 140 years ((Wehtje 2003), (Peer 2011)) (see an overview of the [5-year project timeline](https://github.com/corinalogan/grackles/blob/master/README.md)). **This investigation**: In this piece of the long-term project, we aim to determine what learning mechanisms grackles use (i.e., stimulus or local enhancement, imitation/emulation, personal information) when learning to solve novel problems. Results will indicate how social learning might play a role in the geographic range expansion by elucidating how this species solves novel foraging problems in the wild in three populations (core, middle of the expansion, and at the range edge).

### A. STATE OF THE DATA

This preregistration was written (2017) prior to collecting data.

### B. HYPOTHESIS

#### Information about resources is obtained via individual learning and also transmitted socially in the wild.

Prediction 1: Stimulus enhancement will draw attention to WHAT locus on the apparatus to attend to, and then subjects will rely on personal information to learn HOW to solve that locus. This was found for a similar study on New Caledonian crows (C. J. Logan et al. (2016)). We predict that it will be the same for the grackles because grackles likely need to pay attention to what resources others are accessing, but the exact details of how to access these resources may not be as important because it is likely that most resources are not very complicated to access (e.g., open a sandwich bun wrapper to eat the sandwich)

P1 alternative 1: Subjects might rely on local enhancement to attend to a particular area and then rely on personal information to explore the area and learn how to solve a particular locus. Grackles may pay more attention to other grackles and/or individuals of other species (including humans) when determing whether to visit a location to search for food rather than to whatever food might be present in that location.

P1 alternative 2: Subjects copy (in part, emulation, or in whole, imitation) the sequence of actions they observed others using to solve a particular locus. This may be particularly useful mechanism when trying to open complicated packaging (e.g., a plastic ketchup packet). Complicated packaging is likely not as frequently encountered in their natural environment, which is full of easier to access food.

P1 alternative 3: Subjects do not use social information and rely solely on personal information when solving novel apparatus loci. This species does not form strong bonds with each other (relative to, for example, monogamous corvids), therefore perhaps social information is not as important to them when solving new problems.

P2: Dominant individuals will solve faster because they can exclude subordinates from accessing the resource. This might also make it appear that males are faster at solving than females because males are reported as more dominant than females.

P3: Older individuals may be better at outcompeting others potentially because they have more experience at solving problems in general. We will be able to test this prediction when comparing juveniles (&lt;1yr) and adults (&gt;1yr), but we will not know the age of the adults unless they were banded as juveniles and became adults by the time the testing occurred. Therefore we will have a limited ability to test this prediction.

P4: It does not require many observations of others attempting to solve or solving at a particular locus to influence which loci observers attempt first. This was found for a similar study on New Caledonian crows (C. J. Logan et al. (2016)). We predict that it will be the same for the grackles because grackles likely need to attend to fleeting observations of others as they figure out how to find food in their shared environment. Therefore, there is pressure to attend to any available information.

### C. METHODS

**Planned Sample**

Great-tailed grackles will be caught in the wild in Tempe, Arizona USA for individual identification (colored leg bands in unique combinations) until as much of the population is banded as possible (estimated 400 grackles in the area, 56 have been banded as of 6 May 2019). Some individuals (~6-16) will be brought temporarily into aviaries where demonstrators will be trained on a particular locus of the apparatus before being released back to the wild to serve as demonstrators for the experiment, which will occur in the wild (in the same way as C. J. Logan et al. (2016), except in the wild).

**Data collection stopping rule**

Eight sessions of up to 45 minutes per group will be conducted. A group is defined as having the same trained demonstrator in the presence of many of the same conspecifics across the sessions. For control groups (those with no trained demonstrator), a group must have many of the same individuals as in the first session. We will stop this experiment after each group has completed 8 sessions or when we must move to the next field site, whichever comes first.

#### **Randomization and counterbalancing**

We will attempt to counterbalance demonstrators among the groups such that the demonstrator that was trained in a particular solving method will, during testing, only demonstrate to individuals that have not observed other demonstrators who were trained in solving other methods and when no other demonstrators are present.

#### **Blinding of conditions during analysis**

No blinding is involved in this study.

#### **Dependent variables**

1.  Latency to attempt to solve a particular locus or observe another attempt to solve a particular locus

2.  Latency to solve (obtain the food) a particular locus or observe another solve a particular locus

#### **Independent variables**

#### *P1-P4*

1.  Locus on the apparatus (horizontal side, horizontal flap, vertical flap, or vertical rubber)

2.  ID

3.  Group ID

4.  Start and end times for attempting/solving and observations of attempts/solves (minutes:seconds since the beginning of the session)

5.  Whether the observer saw another individual succeed (obtain food) or just attempt (did not obtain food) at the locus the observer is watching

6.  Which apparatus (left or right) was observed or interacted with

7.  Sex

8.  Age

9.  Dominance rank

10. Population (center, middle, edge)

11. Random effect: ID (to allow for multiple events from the same individual)

### D. ANALYSIS PLAN

We do not plan to **exclude** any data. When **missing data** occur, the existing data for that individual will be included in the analyses for the tests they completed. Analyses will be conducted in R (current version 3.5.2; R Core Team (2017)). When there is more than one experimenter collecting data, experimenter will be added as a random effect to account for potential differences between experimenters in conducting the tests.

#### *Data checking*

The data will be checked for overdispersion, underdispersion, zero-inflation, and heteroscedasticity with the DHARMa R package (Hartig 2019) following methods by [Hartig](https://cran.r-project.org/web/packages/DHARMa/vignettes/DHARMa.html). Note: DHARMa doesn't support MCMCglmm, therefore we will use the closest supported model: glmer from the R package lme4 (Bates et al. 2015).

#### *P1-P4: Learning mechanisms*

The analysis will be conducted as in C. J. Logan et al. (2016) with a Cox proportional hazards model that is sensitive to the order and latency of events at each locus. We will model the rate at which individual *i* in group *j* first attempted method *l* at locus *k* as a function of predictor variables (e.g., age, sex, rank). This method accounts for previous attempts by the subject as well as observations of others attempting and solving the loci.

``` r
data1 <- read.csv ("/Users/corina/GTGR/data/data_reverse.csv", header=T, sep=",", stringsAsFactors=F) 

# DATA CHECKING
library(DHARMa)
library(lme4)

#Latency to solve
simulationOutput <- simulateResiduals(fittedModel = glmer(latencysolve ~ Locus + Group ID + StartTime + ObservedAnother + Apparatus + Sex + Age + Rank + Population + (1|ID), family=poisson, data=data1), n=250) #250 simulations, but if want higher precision change n>1000
simulationOutput$scaledResiduals #Expect a flat distribution of the overall residuals, and uniformity in y direction if plotted against any predictor
testDispersion(simulationOutput) #if under- or over-dispersed, then p-value<0.05, but then check the dispersion parameter and try to determine what in the model could be the cause and address it there, also check for zero inflation
testZeroInflation(simulationOutput) #compare expected vs observed zeros, not zero-inflated if p<0.05
testUniformity(simulationOutput) #check for heteroscedasticity ("a systematic dependency of the dispersion / variance on another variable in the model" Hartig, https://cran.r-project.org/web/packages/DHARMa/vignettes/DHARMa.html), which is indicated if dots aren't on the red line and p<0.05. Also...
plot(simulationOutput) #...there should be no pattern in the data points in the right panel
plotResiduals(ReverseNumber, simulationOutput$scaledResiduals) #plot the residuals against other predictors (in cases when there is more than 1 fixed effect) - can't get this code to work yet

#Latency to attempt to solve
simulationOutput <- simulateResiduals(fittedModel = glmer(latencyattempt ~ Locus + Group ID + StartTime + ObservedAnother + Apparatus + Sex + Age + Rank + Population + (1|ID), family=poisson, data=data1), n=250) #250 simulations, but if want higher precision change n>1000
simulationOutput$scaledResiduals #Expect a flat distribution of the overall residuals, and uniformity in y direction if plotted against any predictor
testDispersion(simulationOutput) #if under- or over-dispersed, then p-value<0.05, but then check the dispersion parameter and try to determine what in the model could be the cause and address it there, also check for zero inflation
testZeroInflation(simulationOutput) #compare expected vs observed zeros, not zero-inflated if p<0.05
testUniformity(simulationOutput) #check for heteroscedasticity ("a systematic dependency of the dispersion / variance on another variable in the model" Hartig, https://cran.r-project.org/web/packages/DHARMa/vignettes/DHARMa.html), which is indicated if dots aren't on the red line and p<0.05. Also...
plot(simulationOutput) #...there should be no pattern in the data points in the right panel
plotResiduals(ReverseNumber, simulationOutput$scaledResiduals) #plot the residuals against other predictors (in cases when there is more than 1 fixed effect) - can't get this code to work yet
```

#### *P4: How many observations?*

The analysis will be conducted as in Barrett, McElreath, and Perry (2017) using multilevel experience-weighted attraction models that can determine how individuals accumulate experience and the probability of an option being chosen. We will also use this analysis to investigate P1-P3.

### E. REFERENCES

Barrett, Brendan J, Richard L McElreath, and Susan E Perry. 2017. “Pay-Off-Biased Social Learning Underlies the Diffusion of Novel Extractive Foraging Traditions in a Wild Primate.” In *Proc. R. Soc. B*, 284:20170358. 1856. The Royal Society.

Bates, Douglas, Martin Mächler, Ben Bolker, and Steve Walker. 2015. “Fitting Linear Mixed-Effects Models Using lme4.” *Journal of Statistical Software* 67 (1): 1–48. doi:[10.18637/jss.v067.i01](https://doi.org/10.18637/jss.v067.i01).

Chow, Pizza Ka Yee, Stephen EG Lea, and Lisa A Leaver. 2016. “How Practice Makes Perfect: The Role of Persistence, Flexibility and Learning in Problem-Solving Efficiency.” *Animal Behaviour* 112. Elsevier: 273–83.

Griffin, Andrea S, and David Guez. 2014. “Innovation and Problem Solving: A Review of Common Mechanisms.” *Behavioural Processes* 109. Elsevier: 121–34.

Hartig, Florian. 2019. *DHARMa: Residual Diagnostics for Hierarchical (Multi-Level / Mixed) Regression Models*. <http://florianhartig.github.io/DHARMa/>.

Lefebvre, Louis, Patrick Whittle, Evan Lascaris, and Adam Finkelstein. 1997. “Feeding Innovations and Forebrain Size in Birds.” *Animal Behaviour* 53 (3). Elsevier: 549–60.

Logan, Corina J, Alexis J Breen, Alex H Taylor, Russell D Gray, and William JE Hoppitt. 2016. “How New Caledonian Crows Solve Novel Foraging Problems and What It Means for Cumulative Culture.” *Learning & Behavior* 44 (1). Springer: 18–28.

Mikhalevich, Irina, Russell Powell, and Corina Logan. 2017. “Is Behavioural Flexibility Evidence of Cognitive Complexity? How Evolution Can Inform Comparative Cognition.” *Interface Focus* 7 (3): 20160121. doi:[10.1098/rsfs.2016.0121](https://doi.org/10.1098/rsfs.2016.0121).

Peer, Brian D. 2011. “Invasion of the Emperor’s Grackle.” *Ardeola* 58 (2). BioOne: 405–9.

R Core Team. 2017. *R: A Language and Environment for Statistical Computing*. Vienna, Austria: R Foundation for Statistical Computing. <https://www.R-project.org>.

Sol, Daniel, and Louis Lefebvre. 2000. “Behavioural Flexibility Predicts Invasion Success in Birds Introduced to New Zealand.” *Oikos* 90 (3). Wiley Online Library: 599–605.

Sol, Daniel, Richard P Duncan, Tim M Blackburn, Phillip Cassey, and Louis Lefebvre. 2005. “Big Brains, Enhanced Cognition, and Response of Birds to Novel Environments.” *Proceedings of the National Academy of Sciences of the United States of America* 102 (15). National Acad Sciences: 5460–5.

Sol, Daniel, Sarah Timmermans, and Louis Lefebvre. 2002. “Behavioural Flexibility and Invasion Success in Birds.” *Animal Behaviour* 63 (3). Elsevier: 495–502.

Wehtje, Walter. 2003. “The Range Expansion of the Great-Tailed Grackle (Quiscalus Mexicanus Gmelin) in North America Since 1880.” *Journal of Biogeography* 30 (10). Wiley Online Library: 1593–1607.
