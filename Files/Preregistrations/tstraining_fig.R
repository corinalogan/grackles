#Touchscreen training article Figure
d <- read.csv(url("https://raw.githubusercontent.com/corinalogan/grackles/master/Files/Preregistrations/tstraining_data_fig.csv"), header=T, sep=",", stringsAsFactors=F)

d <- data.frame(d)
head(d)

d$Bird <- factor(d$Bird)
d$TrainingType <- factor(d$TrainingType)

barplot(d$Bird,d$TrainingType, main="", horiz=TRUE, xlab="Number of days", ylab="", legend=rownames(d$TrainingType))

d1 <- table(d$TrainingType,d$Bird)

barplot(d1, main="", horiz=TRUE, xlab="Number of days", ylab="", legend=rownames(d$TrainingType))

d$Duration