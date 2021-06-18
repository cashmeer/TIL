# Title     : How to handel data with R
# Objective : Learn R
# Created by: jongsulee
# Created on: 2021/06/18

# Plan watch quick 30 min R video
# Learn with Datacamp

# install R on pycharm
# https://www.jetbrains.com/help/pycharm/r-plugin-support.html#ui
# Download and install the R language.
# # get R https://cran.r-project.org/bin/macosx/
# Install the R plugin for PyCharm.
# Configure an R interpreter.

x <- 42
x
y <- 37
x + y
int <- x + y
int

text <- "sting"
bool <- FALSE
float <- 3.2

class(int) # numeric
class(text) # character
class(bool) # logical
class(float) # numeric

#create vector
boolean_vector <- c(TRUE, FALSE, TRUE)
class(boolean_vector) # "logical"

mixed_vector <- c(1, "TRUE", FALSE)
class(mixed_vector) # character

mixed_vector2 <- c("TRUE", FALSE, 1)
class(mixed_vector) # character

# id  h    w
# "A" 150  40
# "B" 160  50
# "C" 170  60

h <- c(150, 160, 170)
w <- c(40, 50, 60)
id <- c("A", "B", "C")
names(h) <- c("A", "B", "C")
names(w) <- id

vector_sum <- h + w
vector_sum






