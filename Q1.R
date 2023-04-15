library(readxl)
library(tidyverse)

setwd("D:/UK/assignment/DSA8023")


#load datasets
temp1 <- read_excel("./WB1_Energia_Challenge_March_2023_Data.xlsx", sheet = 2)
temp2 <- read_excel("./WB2_Energia_Challenge_March_2023_Data.xlsx", sheet= 2)

#combine datasets
raw_data = rbind(temp1, temp2)

head(raw_data)

