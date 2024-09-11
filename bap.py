money = int(input()) 
if (money%100<10 or money%100>19 ):
    if (money%10 == 1):
        print(f"{money} доллар")
if (money%10 <= 4 and money %10>= 2):
   print(f"{money} доллара")
if ((money%10 > 4 or money%10 == 0) or (money%100>10 and money%100<20)):
    print(f"{money} долларов")
