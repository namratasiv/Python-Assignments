# Namrata Sivakumar
# nxs8168


sec = int(input("Enter the number of seconds: "))
min = 0
hour =0
day = 0
if sec>=60 and sec<3600:
    min = sec//60
    sec = sec%60
    print("{} minutes and {} seconds".format(min, sec))

elif sec>=3600 and sec<86400:
    hour = sec//(60*60)
    diff = sec - hour*60*60
    min = diff//60
    sec = sec%60
    print("{} hours, {} minutes and {} seconds".format(hour, min, sec))

elif sec>=86400:
    day = sec //(60*60*24)
    diff = sec - (day * (60*60*24))
    hour = diff // (60 * 60)
    min = diff // 60
    sec = sec % 60
    print("{} days, {} hours, {} minutes and {} seconds".format(day, hour, min, sec))

else:
    print("Try again!")


