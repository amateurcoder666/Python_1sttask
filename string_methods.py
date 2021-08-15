str1 = "kaustav Das"
print(str1.capitalize())
str2 = ",THIS IS MY NAME"
print(str2.casefold())
str3 = "This is a centered text"
print(str3.center(110,"T"))
str4 = "This is my project for My captain. My captain is a learning platform and my captain is very cool"
print(str4)
print("This is how many times I have said captain in the previous sentence:", str(str4.count("captain")))
str5 = "Deku is my hero."
print(str5.encode())
print(str5.endswith("my hero."))
print(str5.endswith("my father."))
str6 = "Hab\tit"
print("My fav song is",str6.expandtabs(9))
print(str4.find("captain"))
print ("Its over {plevel}!!!".format(plevel = 9000))
print(str5.index("my"))
str7 = " Area51 "
print(str7.isalnum())
print(str7.isalpha())
print(str7.isascii())
print(str7.isdecimal())
print(str7.isprintable())
str8 = "22\u00B222"
print(str8.isdigit())
print(str7.isidentifier())
print(str1[0:6].islower())
print(str2[1:len(str2)].isupper())
print(str8.isnumeric())
str9 = "alpha male"
str9 = str9.title()
print(str9.istitle())
str10 = "   "
print(str10.isspace())
str11 = "This is a right justified text"
str12 = "This is a left justified text"
print(str11.rjust(100))
print(str12.ljust(100))
mytuple = ("Me","Love","Anime")
print("*".join(mytuple))
print(str2[1:len(str2)].lower())
print(str1[0:7].upper())
print(str7.strip())
print(str7.lstrip())
print(str7.rstrip())
q = {114:110}
str13 = "He is a queer"
print(str13.translate(q))
x = "hero"
y = "evil"
z = "my"
mytable = str5.maketrans(x,y,z)
print(str5.translate(mytable))
print(str4.partition("captain"))
print(str4.rpartition("captain"))
print(str2[1:len(str2)].replace("NAME","CODE"))
print(str5.split())
print(str4.rsplit(".",1))
print(str5.startswith("Deku"))
str14 = "I know two languages Java and C.\n Now I am learning python"
print(str14.splitlines(False))
print(str1.swapcase())
print(str8.zfill(10))
