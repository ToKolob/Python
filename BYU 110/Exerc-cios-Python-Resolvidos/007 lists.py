pip install numpy
import numpy


num = 1
nums = []
while num != 0:
	num = float(input("num? "))
	if num != 0:
		nums.append(num)

print (nums)

nums = numpy.array(nums)

sum_a = numpy.sum(nums)
product_a = numpy.prod(nums)
mean_a = numpy.mean(nums)
max_a = numpy.max(nums)