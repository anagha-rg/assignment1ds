#Questions 1:
#Given the following jumbled word, OBANWRI guess the correct English word.
#B. RAINBOW

#Questions 2:
#Write a program which prints “LETS UPGRADE”. (Please note that you have to
#print in ALL CAPS as given)
print("LETS UPGRADE")

#Questions 3:
#Write a program that takes cost price and selling price as input and displays whether the transaction is a
#Profit or a Loss or Neither.
cp=eval(input("Enter the Cost price="))
sp=eval(input("Enter the Selling price="))
l=cp-sp   #Loss
p=sp-cp    #Profit
if sp>cp:
    print("Profit=",p)
elif cp==sp:
    print("Neither profit nor loss")
else:
    print("Loss=",l)

#Questions 4:
#Write a program that takes cost price and selling price as input and displays whether the transaction is a
#Profit or a Loss or Neither.
#INPUT FORMAT
#The first line contains the cost price.
#The second line contains the selling price.
#OUTPUT FORMAT
#Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither
#profit nor loss, print "Neither". (You must not have quotes in your output)
#NOTE:
#Please stick to the input and output format. Don't add anything extra like
#'Enter cost price', 'Enter selling price', etc.
cp=eval(input("Enter the cost price="))
sp=eval(input("Enter the selling price="))
p=cp-sp   #profit
if p>0:
    print("Profit")
elif p<0:
    print("Loss")
else:
    print("Neither")
print("Thank you")


#Questions 5:
#Write a program that takes an amount in Indian Rupees as input. You need to find its equivalent
#in Euro and display it. Assume 1 Euro equals Rs. 80.
#Please note that you are expected to stick to the given input and output
#format as in sample test cases. Please don't add any extra lines such as
#'Enter a number', etc.
#Your program should take only one number as input and display the output.
a=eval(input("Amount="))
e=80*a   #e=European converted amount, 80 is conversion rate, and a=Indian currency amount
print("Converted amount=" "Euros", e)

