
# Function to return the minimum cost 
def minCost(price, n): 

	# Sort the price array 
	price = sorted(price) 
	totalCost = 0

	# Calcualte minimum price 
	# of n-2 most costly person 
	for i in range(n - 1, 1, -2): 
		if (i == 2): 
			totalCost += price[2] + price[0] 

		else: 
			price_first = price[i] + price[0] + 2 * price[1] 
			price_second = price[i] + price[i - 1] + 2 * price[0] 
			totalCost += min(price_first, price_second) 

	# Calculate the minimum price 
	# of the two cheapest person 
	if (n == 1): 
		totalCost += price[0] 

	else: 
		totalCost += price[1] 

	return totalCost 

no_of_test_cases = int(input("Enter no of test cases: "))
inputArr = []
inputPerson =[]
while no_of_test_cases > 0 :
	no_of_persons = int(input("Enter no of person: "))
	inputPerson=[]
	inputArr.append(no_of_persons)
	while no_of_persons > 0:
		cost_per_person = int(input("Enter costs : "))
		inputPerson.append(cost_per_person)
		no_of_persons = no_of_persons - 1
	inputArr.append(inputPerson)
	no_of_test_cases = no_of_test_cases - 1

print()
print("======================OUTPUT===========================")  
print()                    
for i,j in enumerate(inputArr):
	if i %2 != 0:
		price = j
		person = len(j)
		print(minCost(price, person))
