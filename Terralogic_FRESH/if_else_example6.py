# Example for if elif else
# To check student grade
percentage = 30

if percentage >= 90 :
    print ("He/she is OUTSTANDING --O")
elif percentage >= 80 and   percentage < 90:
    print ("He/she is EXCELLENT --A")
elif percentage >= 70 and percentage < 80:
    print ("He/She is GOOD --B")
elif percentage >= 60 and percentage < 70:
    print ("He/She is FAIR --C")
elif percentage >= 50 and percentage < 60:
    print ("He/She is SATISFACTORY --D")
elif percentage >= 40 and percentage < 50:
    print ("He/She is AVERAGE ---E")
else:
    print ("You are not eligible")

print ("Good bye!!!!!!")