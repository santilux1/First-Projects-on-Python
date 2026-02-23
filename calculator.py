
Ahorros = int(input("How much money do you want to save for this year?"))
print(Ahorros)
if Ahorros < 100:
		print("Get more money")
else: 
		for i in range(5):
			Ahorros = int(Ahorros * 5)
		print("In 5 years you will have: " + str(Ahorros) + ",Keep Saving,Fellow")
