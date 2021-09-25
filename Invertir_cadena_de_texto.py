str = "trabajando con python"
string_reversed=[]
i = len(str)
while i > 0: 
    string_reversed += str[i-1]
    i = i - 1 
print("la forma inversa es:", string_reversed) 