import pyshorteners
from colorama import init, Fore, Back, Style

init()

print(Fore.BLUE, " [+] Url Shortener by wb2c0 [+]\n")

prompt = Fore.RED + "enter the link: "
link = input(prompt)
shortener = pyshorteners.Shortener()


result = shortener.tinyurl.short(link)


print(Fore.YELLOW, f"shortened url: {result}")