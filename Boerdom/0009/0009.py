import sys # type: ignore
from pyfiglet import Figlet # type: ignore
import random # type: ignore

figlet = Figlet()
fonts = figlet.getFonts()

args = sys.argv
args.pop(0)

if len(args) == 0:
    randfont = random.choice(fonts)
    figlet.setFont(font = randfont)
    print(figlet.renderText(input("Input: ")))
elif len(args) == 2:
    if args[0] == "-f" or args[0] == "--font":
        figlet.setFont(font = args[1])
        print(figlet.renderText(input("Input: ").strip()))
    else:
        sys.exit(1)
else:
    sys.exit(1)