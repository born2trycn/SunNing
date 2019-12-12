import time

now = time.gmtime()
print('now')

month = now.tm_mon
day = now.tm_mday

print(month)
print(day)

if (month==9 and day == 10):
    print('猪你生日快乐！')

if (month==4 and day==24):
    print('今天是妈妈的生日呀')

if (month == 12 and day == 9):
    print('今天是爸爸的生日呀')

if (month == 6 and day == 21):
    print('今天父亲节 嗷~~')

if (month == 5 and day == 10):
    print('今天母亲节 嗷~~')