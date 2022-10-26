exp="(x-1)
pila= 
for i in exp;
	if i == "(":
		pila.append(i)
	elif i==")":
		if len(pila)>0:
			pila.pop()
		else :
			print("Expresion Incorrecta")
			break
else:
	if len(pila)==0:
		print("Expresion correcta")
	else:
		print("Expresion incorrecta")

