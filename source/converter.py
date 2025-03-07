tips = '''
Another tip is only use either "" or '' dont switch between them

Also use f"" to print strings with variables in them simply put every variable in a bracket
EXAMPLE: print(f"Hello i am {name}")

When naming variables use names that descripe the value of the variable not random letters
EXAMPLE: windows_path = 'C:/Windows'
'''
import ctypes
import os, sys
import time
import requests
from pytube import YouTube

banner = '''

███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ 
████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
██╔████╔██║██║   ██║██║     ██║   ██║██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
██║╚██╔╝██║██║   ██║██║     ██║   ██║██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

                        * Open Sorce Multi Downloader by CraftModzZ aka. WeepingAngel *
                Discord: _WeepingAngel_ VI#6666 | GitHub: https://www.github.com/crafttino21


'''


class colors:
  '''
  This is a class containing variables of similar values
  To use this class call the class name then the variable 
  '''
  blue = os.system("color b")
  red = os.system("color C")
  green = os.system("color a")
  pink = os.system("color D")


class functions:

  # Create a windows message box
  def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

  # Clears the console
  def clearConsole():
    clr = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

  # Main menu loop function
  def menu():
    '''
		                            _____CHANGES_____
  	  * Used while True instead of while option != 0 to simplify the loop.
		  * Used input() instead of int(input()) to handle non-integer input gracefully.
		  * Used option.lower() to convert the input option to lowercase and simplify the if statements.
		  * Removed the exit() calls in the try-except blocks and used continue instead to keep the loop running.
	    * Added better exit() mechanic with sys.exit() which passing a 1 means an error occured.
		  * Added a prompt for the destination directory in option 3.
		  * Moved the menu() call outside the function to prevent an infinite recursion loop.
    '''

    option_text = "Choose your Converter > "

    functions.clearConsole()
    print(banner)
    colors.pink

    # Use '\n' to create a new line
    print("[1] YouTube to MP4 \n")
    print("[2] Image Downloader \n")
    print("[3] YouTube to MP3 (New!) \n\n")

    while True:
      option = input(option_text)

      if option == "1":
        try:
          link = input("Enter your YouTube Link (mp4): ")
          yt = YouTube(link)
          y = yt.title.title()
          print(f"Video Title: {y}")
          z = yt.author.title()
          print(f"Uploader: {z}")
          ys = yt.streams.get_highest_resolution()
          ys.download()
          functions.Mbox('MultiDownloader by WeepingAngel',
               'Download Successfully and Finished!', 1)
        except:
          print("[ERROR] Can't Download the Video or invalid link!")
          time.sleep(5)
          continue

        et = input("Do you want to Download another video? (Y/N) > ")
        if et.lower() == "y":
          functions.clearConsole()
          continue
        else:
          functions.Mbox('MultiDownloader by WeepingAngel',
               'Thanks for Using This Tool :)', 1)
          sys.exit(0)

      elif option == "2":
        try:
          web = input("Paste your Image: ")
          r = requests.get(web)
          print(r.content)
          with open("output.png", "wb") as f:
            f.write(r.content)
          functions.Mbox('MultiDownloader', 'Download Complete!', 1)
          print(f"{colors.green}Download Complete!")
        except:
          print("[ERROR] Can't Convert!")
          continue

      elif option == "3":
        print("YouTube to MP3 (Beta)")
        try:
          yt = YouTube(
            str(input("Enter the URL of the video you want to download: \n>> ")))
          video = yt.streams.filter(only_audio=True).first()
          destination = input(
            "Enter the destination (leave blank for current directory)\n>> ") or '.'
          out_file = video.download(output_path=destination)
          base, ext = os.path.splitext(out_file)
          new_file = f'{base}.mp3'
          os.rename(out_file, new_file)
          print(f"{yt.title} has been successfully downloaded.")
          functions.Mbox('MultiDownloader', 'Download Successfully!', 1)
        except:
          print("[ERROR] Can't Download the Audio or Invalid URL!")
          time.sleep(5)
          continue

      elif option == "0":
        functions.Mbox('MultiDownloader by WeepingAngel',
             'Thanks for Using This Tool :)', 1)
        sys.exit(0)

      else:
        print("Invalid option!")
        continue


# This is the first block of code ran
try:
  functions.Mbox('MultiDownloader',
       'OS MultiDownloader by WeepingAngel | Version: 1.2.1 (Patched)', 1)
  functions.menu()
except Exception as e:
  # If we cannot do the above block print the error and exit with error code `1`
  print(f"An unkown runtime error occured \n{e}\n")
  sys.exit(1)