# Importing the libraries
import yt_dlp
import os
import pyfiglet
from colorama import Fore, Style, init
init(autoreset=True)

# Creating the logo
def show_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    ascii_banner = pyfiglet.figlet_format("PyMedia", font="slant")
    print(Fore.CYAN + Style.BRIGHT + ascii_banner)
    print(Fore.CYAN + "═" * 50)
    print(Fore.WHITE + Style.BRIGHT + "      Simple & Fast Media Downloader Tool")
    print(Fore.CYAN + "═" * 50)
    print(Fore.GREEN + f" [►] Developer: {Fore.WHITE}anonDev")
    print(Fore.CYAN + "═" * 50)
    print(Fore.CYAN + f" Warning: {Fore.RED} Please Don't Use The Tool For Haram Videos ")
    print(Fore.CYAN + "═" * 50 + "\n")

show_logo()

# Asking for URL
url = input(Fore.YELLOW + Style.BRIGHT + " $ Paste Link Here" + Fore.WHITE + " > " + Style.RESET_ALL)

# the options for the downloader
# not to show warnings and notifications
ydl_opts = {
    'quiet': True,          
    'no_warnings': True,    
    'nocheckcertificate': True, 
}

print(Fore.CYAN + "\n $ Fetching media info...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    infos = ydl.extract_info(url, download=False)
    title = infos.get('title', 'Unknown')
    formats = infos.get('formats', None)

print(Fore.CYAN + "─" * 30)
print(Fore.WHITE + f"Title: {Fore.MAGENTA}{title}")
print(Fore.CYAN + "─" * 30)

asking = input(Fore.YELLOW + " $ Choose Type (" + Fore.WHITE + "v" + Fore.YELLOW + " for Video /" + Fore.WHITE + "a" + Fore.YELLOW + " for Audio): ").lower()

print(f"\n{Fore.CYAN} {'ID':<10} | {'EXT':<6} | {'QUALITY/ABR':<12}")
print(Fore.CYAN + " " + "─" * 35)

# Asking for the type
if asking == "v":
    for f in formats:
        if f.get('vcodec') != 'none' and f.get("acodec") != 'none':
            print(f" {Fore.GREEN}{f['format_id']:<10} {Fore.WHITE}| {f['ext']:<6} | {Fore.YELLOW}{f.get('height')}p")
elif asking == "a":
    for f in formats:
        if f.get('vcodec') == 'none' and f.get('acodec') != 'none':
            print(f" {Fore.GREEN}{f['format_id']:<10} {Fore.WHITE}| {f['ext']:<6} | {Fore.YELLOW}{f.get('abr')}kbps")
else:
    print(Fore.RED + " Invalid selection.")
    exit()

print(Fore.CYAN + " " + "─" * 35)
choice = input(Fore.YELLOW + "\n $ Enter Format ID " + Fore.WHITE + "> ")

# Choosing the folder to save
current_path = os.getcwd()
ask_path = input(Fore.YELLOW + f" $ Use current path? ({Fore.WHITE}{current_path}{Fore.YELLOW}) y/n " + Fore.WHITE + "> ").lower()

target_path = current_path
if ask_path == 'n':
    user_input_path = input(Fore.YELLOW + " $ Enter Destination Path " + Fore.WHITE + "> ")
    if os.path.exists(user_input_path):
        target_path = user_input_path
    else:
        print(Fore.RED + "Path not found! Reverting to current directory.")

ydl_opts_down = {
    'format': choice,
    'outtmpl': os.path.join(target_path, '%(title)s.%(ext)s'),
    'quiet': False,          
    'no_warnings': True,    
    'nocheckcertificate': True, 
}

print(f"\n{Fore.RED}{Style.BRIGHT} DOWNLOADING....")
try:
    with yt_dlp.YoutubeDL(ydl_opts_down) as ydl:
        ydl.download([url])
    print(Fore.GREEN + Style.BRIGHT + f"\n Done! Saved at: {Fore.WHITE}{target_path}")
except Exception as error:
    print(Fore.RED + f" Error: {error}")
