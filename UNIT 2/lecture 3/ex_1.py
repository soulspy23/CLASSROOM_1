#13th July 2022

#input a text from user. Accept roll number as text. Identify whether this roll number belongs to S K Somaiya or not. -> cascading

str = input("Enter roll call :")
if(str.strip().startswith("31")):
    print(str,"belongs to SKSC domain !")
else:
    print(str,"does not belongs to SKSC domain !")
