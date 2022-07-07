#Load Packages
#library(plyr)
library(Hmisc)
library(lmerTest)
library(LMERConvenienceFunctions)
library(e1071)
library(car)
library(effectsize)
require(MuMIn)

#Reading data
#replace with the team_details file
#data = read.csv("/home/sham/Desktop/846spring2020/project/github/ethanalysis75/vault/data/team_details.csv")

data = read.csv("/home/sham/Desktop/846spring2020/project/github/ethanalysis75/vault/data/team_details_controlvariables1.csv")


################################################################################
# Normality adjustment
################################################################################

# Check the skew and kurtosis of the dependent variable.
# If skewness value lies above +1 or below -1, data is highly skewed. 
# If it lies between +0.5 to -0.5, it is moderately skewed. 
# If the value is 0, then the data is symmetric

skewness(data$median_pr_merged)
kurtosis(data$median_pr_merged)
hist(data$median_pr_merged)

scale.data <- function(data){
  
  scale_variables <- c("proj_size", "proj_age","project_star_count","project_watchers_count","project_forks_count", "noofmembers","noofyears")
  data[scale_variables] <- lapply(data[scale_variables], function(x) c(scale(x, center= min(x), scale=diff(range(x)))))
  
  return(data)
}

data=scale.data(data)

#RQ2
ind_vars_eth = c("noofmembers","noofyears",
                 "eth_blau_index",
                 "gender_blau_index",
                 "proj_size",  
                 "proj_age","project_star_count")

vc_eth <- varclus(~ ., data=data[,ind_vars_eth], trans="abs")
plot(vc_eth)
threshold <- 0.7
abline(h=1-threshold, col = "red", lty = 2)

mixed.lmer<- lmer(log(median_pr_merged)~ 
                    eth_blau_index+
                    gender_blau_index+
                    proj_size+proj_age+
                    noofmembers+
                    noofyears+project_star_count+
                    (1|owner_project),
                  data)

# Remove outlier
print(summary(mixed.lmer))
print(vif(mixed.lmer))
explantory_power = anova(mixed.lmer,test='Chisq')
print(explantory_power)
AIC(mixed.lmer)
BIC(mixed.lmer)
print(r.squaredGLMM(mixed.lmer))

#RQ3
wtest = wilcox.test(median_pr_merged ~ ethblau_st_cat, alt="two.sided", correct=TRUE, paired = FALSE, conf.int = TRUE, data= data)
Zstat<-qnorm(wtest$p.value/2)
boxplot(median_pr_merged ~ ethblau_st_cat, data,xlab = "Teams", ylab ="Team contributions")

print( summary(data$median_pr_merged))
