# get each branch's sample number
num = c(3, 5, 7, 9, 11) # input
length(num)

for (i in (1:length(num))) {
	set.seed(0610)
	print(sample(x= 1:num[i], size = ceiling(num[i]/10), replace =F))
	# 10% sample, at least one although num < 10, no duplication
}


# test
for (i in (1:length(num))) {
	print(num[i])
}

ceiling(3/10) # rounding up
