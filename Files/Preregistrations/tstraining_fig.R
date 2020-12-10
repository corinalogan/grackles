# Touchscreen training article bar plot figure
# Seitz BM, McCune KB, MacPherson M, Bergeron LM, Blaisdell AP, Logan CJ. 2020. Using touchscreen equipped operant chambers to study comparative cognition. Benefits, limitations, and advice. bioRxiv 2020.10.03.324814. https://doi.org/10.1101/2020.10.03.324814
# Corina Logan, corina_logan@eva.mpg.de

#ggplot2 advice https://cedricscherer.netlify.app/2019/08/05/a-ggplot2-tutorial-for-beautiful-plotting-in-r/#toc
library(ggplot2)
d <- read.csv(url("https://raw.githubusercontent.com/corinalogan/grackles/master/Files/Preregistrations/tstraining_data_fig.csv"), header=T, sep=",", stringsAsFactors=F)

d <- data.frame(d)
head(d)

d$Bird <- factor(d$Bird)
d$TrainingType <- factor(d$TrainingType)
d$TrainingType <- ordered(d$TrainingType, levels = c("4trialstartkey", "3whitesquare", "2movingstim", "1hopper"))

ggplot(d, aes(x = Bird, y = Duration, fill=TrainingType)) +
   geom_bar(position="stack", stat="identity") +
   scale_fill_grey() +
   labs(x = "", y = "Number of days") +
   coord_flip() +
   geom_hline(yintercept=13) +
   theme(panel.background = element_rect(fill = "#ffffff", colour = "#ffffff", size = 2, linetype = "solid")) +
   #annotate("text", label=c("Fast","Slow"),x=14.5, y=c(9,17), size=4, colour="black") +
   annotate("text", label="X",x=3, y=1, size=4, colour="black") +
   annotate("text", label="X",x=6, y=1, size=4, colour="black") +
   annotate("text", label="X",x=8, y=1, size=4, colour="black") +
   annotate("text", label="X",x=11, y=11.5, size=4, colour="black") +
   annotate("text", label=c("1.0","1.0","1.0","1.0","1.0","0.0","1.0","0.8","1.0","1.0","1.0","1.0","1.0","1.0","Std"),x=c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,14.5), y=-2, size=3, colour="black") +
   annotate("text", label=c("1.0","1.0","","1.0","1.0","","0.3","","1.0","0.3","","0.3","","1.0","TOC"),x=c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,14.5), y=66, size=3, colour="black") +
   theme(plot.margin = unit(c(2,1,1,1), "lines")) + 
  labs(title = "            Slow     Fast") 