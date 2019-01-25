

D="2 - Limcee ||,1 - Calcirol ||,2 - Instafol ||,2 - Paternia xt ||,1 - Ultraq 300 ||,1 - Folxt  ||"

prdt_list=D.split("||,")
prdt_list=[item.replace("|", "") for item in prdt_list]
Product_list=""
count=1
for k in prdt_list:
		#k.replace("|","")
        Product_list += str(count)+") "+ k +"\n"
        #print(Product_list)
        count = count+1
Product_list.replace("|",".")
print(Product_list)
print(type(Product_list))