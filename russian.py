from googletrans import Translator
from itertools import islice
from colorama import init, Fore, Back, Style

init()

File1 = open("Words.txt", 'r+', encoding = "UTF-8")
File2 = open("WordsDone.txt" , "a", encoding = "UTF-8")
TodayList = []
N = 30

with File1 as f1, File2 as f2:
	TodayList = list(islice(f1, N))
	lines = f1.readlines()
	for word in range(len(TodayList)):
		f2.write(TodayList[word])
	f1.seek(0)
	f1.truncate()
	for line in lines:
		if line not in TodayList:
			f1.write(line)



print(Back.BLUE + Fore.WHITE + "\n" + "BENVENUTO AL CORSO DI RUSSO")
print(Style.RESET_ALL)
for word in range(len(TodayList)):
    translator = Translator()
    translated = translator.translate(str(TodayList[word]), src='ru', dest='it')
    print (Fore.WHITE + str(TodayList[word]).strip() + Fore.RED + " => " + Fore.WHITE + translated.text)
    print(Style.RESET_ALL)
