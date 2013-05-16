#Name: polyreg.r
#Author: Adrienne Sands (2013)
#Purpose: Fits polynomials up to a maxdeg


#polyfit(x,maxdeg) fits all polynomials up to degree maxdeg; y is 
#vector for response variable, x for predictor; creates an object of
#class "polyreg", consisting of outputs from the various regression
#models, plus the original data

polyfit  <- function(y,x,maxdeg){
  pwers  <- powers(x,maxdeg) 
  lmout  <- list() #start to build class
  class(lmout)  <- "polyreg" #create new class
  for (i in 1:maxdeg){
    lmo  <- lm(y ~ pwrs[,1:i])
    #extend the lm class here, with the cross-validated predictions
    lmo$fitted.xvvalues  <- lvoneout(y,pwrs[,1:i,drop=F])
    lmout[[i]]  <- lmo
  }
  lmout$x  <- x
  lmout$y  <- y
  return(lmout)
}

#generic print() for an object of class "polyreg": print
#cross validated mean-squared prediction errors
print.polyreg  <- function(fits){
  maxdeg  <- length(fits) #count lm() outputs only, not $x, $y
  n  <- length(fits$y)
  tbl  <- matrix(nrow=maxdeg, ncol=1)
  cat("mean squared prediction errors, by degree\n")
  colnames(tbl)  <- "MSPE"
  for (i in 1:maxdeg){
    fi  <- fits[[i]]
    errs  <- fits$y - fi$fitted.xvvalues
    spe  <- sum(errs^2)
    tbl[1,i]  <- spe/n
  }
  print(tbl)
}

#generic plot(); plots fits against raw data
plot.ployreg  <- function(fits){
  plot(fits$x, fits$y, xlab="X",ylab="Y") #plot data points as backgorund
  maxdg  <- length(fits) -2
  cols  <- c("red","green","blue")
  dg  <- curvecount  <- 1 #initialize both variables at 1
  while (dg < maxdg){
    prompt  <- paste("RETURN for XV fit for degree",dg, "or type degree","or q for quit")
    rl  <- readline(prompt)
    dg  <- if (rl=="") dg else if (rl !="q") as.integer(rl) else break
    lines (fits$x,fits[[dg]]$fitted.values,col=cols[curvecount%%3 + 1])
    dg  <- dg+1
    curvecount  <- curvecount +1
  }
}

#forms matrix of pwoers of the vector x, through degree dg
powers  <- function(x,dg){
  pw  <- matrix(x,nrow=length(x))
  prod  <- x
  for (i in 2:dg){
    prod  <- prod*x
    pw  <- cbind(pw,prod)
  }
  return(pw)
}

#finds cross-validated predicted values; could be made much faster via #matrix-update methods
lvoneout  <- function(y,xmat){
  n  <- length(y)
  predy  <- vector(length=n)
  for (i in 1:n){
    #regress, leaving out ith observation
    lmo  <- lm(y[-i] ~xmat[-i,])
    betahat  <- as.vector(lmo$coef)
    #the 1 accomodates the constant term
    pred[i]  <- betahat %*% c(1,xmat[i,])
  }
  return(predy)
}

#polynomial function of x, coefficients cfs
poly  <- function(x,cfs){
  val  <- cfs[1]
  prod  <- 1
  dg  <- length(cfs)-1
  for (i in 1:dg){
    prod  <- prod * x
    val  <- val + cfs[i+1] *prod
  }
}