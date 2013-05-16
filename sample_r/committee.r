#Name: committee.r
#Author: Adrienne Sands (2013)
#Purpose: a combinatorial simulation with committee/ representative members

#comsim function from 8.6.3: A combinatorial simulation
#create a function. Input: number of representatives.
sim  <- function(nreps){
  commdata  <- list() #create a new list to hold info on the 3 communities
  #initialize this new variable for our loop
  commdata$countabsamecomm  <- 0
  for (rep in 1:nreps) {
    commdata$whosleft  <- 1:nreps #who's left to choose from. changed from hard coded 20
    commdata$numabchosen  <-0 #initialize variable for number among a,b chosen so far
    #choose committe 1, check for A,B serving together
    commdata  <- choosecomm(commdata,5) #change the value of commdata after running com;
    #if A or B already chosen, no need to look at the other comms.
    if (commdata$numabchosen > 0) next
    #choose committee 2 and check
    commdata  <- choosecomm(commdata,4)
    if (commdata$numabchosen > 0) next
    #choose committee 3 and check 
    commdata  <- choosecomm(commdata,3)
    if (commdata$numabchosen > 0) next
  }
print(commdata$countabsamecomm/nreps) #print probability of a,b on commitee together
}
#com helper function
choosecomm  <- function(comdat,comsize){
  #choose committee
  committee  <- sample(comdat$whosleft,comsize)
  #count how many of A and B were chosen
  comdat$numabchosen  <- length(intersect(1:2,committee))
  if (comdat$numabchosen ==2)
      comdat$countabsamecomm  <- comdat$countabsamecomm + 1 #adds to our count of event occurrences
  #delete chosen committee from the set of people we now have to choose from
  comdat$whosleft  <- setdiff(comdat$whosleft,committee)
  return(comdat)
}