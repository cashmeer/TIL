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

total_h <- sum(h)
total_w <- sum(w)

total_h
total_w

total_h > total_w
total_h < total_w

slice <- id[c(2,3)]
slice
slice2 <- id[2:3]
slice2

# who is abover 165
over_height <- h > 165

name_over_height <- id[over_height]
over_height
name_over_height

# create matrix

# DC data
new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)


matrix(1:9, byrow = TRUE, nrow = 3)

mtx <- c(h,w,id)
mtx
