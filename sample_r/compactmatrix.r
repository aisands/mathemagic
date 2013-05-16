#Name: compactmatrix.r
#Author: Adrienne Sands (2013)
#Purpose: compactly stores upper-triangular matrices

#class "ut", compact storage of upper-triangular matrices

#utility function, returns 1+...+i
sum1toi  <- function(i) return(i*(i+1)/2)

#create an object of class "ut" from the full matrix inmat
ut  <- function(inmat){
  n  <- nrow(inmat)
  outmat  <- list()
  class(outmat)  <- "ut"
  outmat$mat  <- vector(length=sum1toi(n))
  outmat$ix  <- sum1toi(0:(n-1)) +1
  for (i in 1:n){
    #store column i
    ixi  <- outmat$ix[i]
    outmat$mat[ixi:(ixi+i-1)]  <- inmat[1:i,i]
  }
  return(outmat)
}

#uncompress utmat to a full matrix
expandut  <- function(utmat){
  n  <- length(utmat$ix) #numbers of rows and cols of matrix
  fullmat  <- matrix(nrow=n,ncol=n) #start building the full matrix with n rows, cols
  for (j in 1:n){
    #fill jth column
    start  <- utmat$ix[j] 
    fin  <- start + j -1 
    abovediagj  <- utmat$mat[start:fin] #above-diag part of col j
    fullmat[,j]  <- c(abovediagj,rep(0,n-j)) #fill with zeros
  }
  return(fullmat)
}

#print matrix
print.ut  <- function(utmat)
    print(expandut(utmat))

#multiply one ut matrix by another, returning another ut instance;
#implement as a binary operation
"%mut%"  <- function(utmat1,utmat2){
  n  <- length(utmat1$ix) #num rows and cols of matrix (must be same size)
  utprod  <- ut(matrix(0,nrow=n, ncol=n))
  
  for(i in 1:n){
    startbi  <- utmat2$ix[i] #find starting element of column i of matrix 2
    prodcoli  <- rep(0,i) #create a vector that will hold the product

    for (j in 1:n) {  
      startaj  <- utmat1$ix[j] #find starting element of column j of matrix 1
      bielement  <- utmat2$mat[startbi+j-1] #find the jth row element of b column i
      prodcoli[1:j]  <- prodcoli[1:j] + bielement *utmat1$mat[startaj:(startaj+j-1)]
    }
  # now need to tack on the lower 0s
  startprodcoli  <- sum1toi(i-1)+1
  utprod$mat[startbi:(startbi+i-1)]  <- startprodcoli
  }
  return(utprod)
}

test  <- function() {
  utm1  <- ut(rbind(1:2,c(0,2)))
  utm2  <- ut(rbind(3:2,c(0,1)))
  utp  <- utm1 %mut% utm2
  
  print(utm1)
  print(utm2)
  print(utp)
  
  utm1  <- ut(rbind(1:3,0:2,c(0,0,5)))
  utm2  <- ut(rbind(4:2,0:2,c(0,0,1)))
  utp <- utm1 %mut% utm2
  
  print(utm1)
  print(utm2)
  print(utp)
  
}
                            