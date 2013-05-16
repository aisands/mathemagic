#Name: airbnb.r
#Author: Adrienne Sands (2013)
#Purpose: reads in listings/ bookings data, creates a filtered frequency table, and runs an OLS regression

airbnb  <- function(){
  listings  <- read.csv("C:\\Users\\FrootyLoops\\Desktop\\listings.csv",header=TRUE,as.is=TRUE)
  bookings  <- read.csv("C:\\Users\\FrootyLoops\\Desktop\\bookings.csv",header=TRUE,as.is=TRUE)
  mergedbnb  <-   merge(listings,bookings,by="prop_id")
  
  #creates frequency table of the neighborhoods
  subsetN  <- table(mergedbnb$neighborhood)
  subsetNDF  <- as.data.frame(subsetN)
  subsetNDF  <- subset(subsetNDF,subsetNDF$Freq>=10)
  final  <- subset(mergedbnb,mergedbnb$neighborhood %in% subsetNDF$Var1)
  
  #adds frequency value to merged table
  subsetP  <- table(final$prop_id)
  subsetPDF  <- as.data.frame(subsetP)
  final <- merge(final,subsetPDF,by.x="prop_id",by.y="Var1")
  
  #runs regression OLS linear regression of price, person_capacity, and description_length as independent variables 
  #against total bookings per listing
  reg1  <- lm(Freq ~ price + person_capacity + description_length, data=final)
  reg1  <- summary(reg1)
  
  #Run an OLS linear regression of every characteristic (except prop_id) in listings.csv 
  #against total bookings per listing
  reg2  <- lm(Freq ~ prop_type + neighborhood + price + person_capacity + picture_count + description_length + tenure_months,data=final)
  summary(reg2)
  reg2  <- summary(reg2)
  print(reg1)
  print(reg2)
}
