product=['A','B','C']
price=[20,40,50]
quantity=[]
pack=[]
amount=[]
totalamount=0.0
temp=0.0
discount_msg="No discount applicable"
discount_amt=0
shp_amt=0
for i in range(0,3):
 quantity.append(int(input("Enter the quantity of product{}: ".format(product[i]))))
 amount.append(price[i]*quantity[i])
 ch=input("Do you want to wrap as gift (Y|N): ")
 if(ch=='y' or ch=='Y'):
  pack.append(1)
 elif(ch=='n' or ch=='N'):
  pack.append(0)
 else:
  print("invalid input !!");
totalamount=sum(amount)
i=0
for i in range(0,3):
 if(quantity[i]>10):
  t=amount[i]
  discount_amt=(amount[i]*5/100)
  amount[i]=amount[i]-(amount[i]*5/100)
  totalamount=sum(amount)
  discount_msg="bulk_5_discount"
  amount[i]=t
i=0
for i in range(0,3):
 if(quantity[i]>15):
  if(sum(quantity)>30):
   diff=quantity[i]-15 
   t=amount[i]
   amount[i]=(15*price[i])+(diff*price[i])-((diff*price[i])*50/100)
   temp=sum(amount)
   amount[i]=t
   if(temp<totalamount):
    totalamount=temp
    discount_msg="tiered_50_discount"
    discount_amt=((diff*price[i])*50/100)

if(sum(quantity)>20):
  temp=sum(amount)-(sum(amount)*10/100)
  if(temp<totalamount):
    totalamount=temp
    discount_msg="bulk_10_discount"
    discount_amt=(sum(amount)*10/100)

if(sum(amount)>200):
 temp=sum(amount)-(sum(amount)*10/100)
 if(temp<totalamount):
    discount_msg="flat_10_discount"
    discount_amt=(sum(amount)*10/100)
    totalamount=temp

total_q=sum(quantity)
if((total_q % 10)==0):
  shp_amt=(total_q//10)*5
else:
 shp_amt=((total_q//10)+1)*5

print("\n\t*****BILL DETAILS*****\n")
for j in range(0,3):
 print("Product Name: ",product[j],end="   ");
 print("Quantity: ",quantity[j],end="   ");
 print("Total Amount: ",amount[j]);
print("Sub Total: ",sum(amount))
print("Discount Name: {}  Discount Amount: {}".format(discount_msg,discount_amt))
print("Shipping Fee: {}  Gift Wrap Fee: {}".format(shp_amt,sum(pack)))
print("Total Amount: {}".format(totalamount+shp_amt+(sum(pack))))
  

 


