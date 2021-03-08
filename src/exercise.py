def main():
    #write your code below this line

    inheritance = int(input("Inheritance:"))
    YearsSinceDeath = int(input("Years since death:"))
    inheritanceDifference = (inheritance-325000)

    if(inheritance<325000 or YearsSinceDeath>=7):
      print("Tax: 0")
    elif(YearsSinceDeath>=6):
      print("Tax:" + str(inheritanceDifference*0.08))
    elif(YearsSinceDeath>=5):
      print("Tax:" + str(inheritanceDifference*0.16))
    elif(YearsSinceDeath>=4):
      print("Tax:" + str(inheritanceDifference*0.24))
    elif(YearsSinceDeath>=3):
      print("Tax:" + str(inheritanceDifference*0.32))
    elif(YearsSinceDeath<3):
      print("Tax:" + str(inheritanceDifference*0.40))
    else:
      print("Please enter a valid response.")
     



if __name__ == '__main__':
    main()
