import random as r
import os
from datetime import datetime

def main():
    psw = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "()[]{}!?'@#-_,;.:+-*/ "
    len = inputLen()
    for i in range(len):
        psw += r.choice(lower + upper + numbers + symbols)
    if createFile(psw):
        os.system("cls")
        os.system("color a")
        print("La tua nuova password è stata creata con successo, controlla nel Desktop nel file di testo appena creato")
    else:
        os.system("cls")
        os.system("color 4")
        print("Si è verificato un errore nella creazione del file di testo contenente la tua password.")


def inputLen() -> int:
    n = 0
    while n <= 15:
        try:
            n = int(input("Inserire la lunghezza della password (min: 16 caratteri): "))
        except:
            print("L'input inserito non è un numero o un carattere valido.")
            n = 0
            pass
    return n

def createFile(psw : str) -> bool:
    """
    Function in order to create a text file in the desktop
    """
    home = os.path.expanduser( '~' )
    path = os.path.join(home, "Desktop")
    file_name = inputFileName() + ".txt"
    os.chdir(path)
    try:
        file = open(file_name, "w")
        file.write(psw)
        file.close()
        log(string="Password generated successfully", type=0, fileName=file_name)
        return True
    except Exception as error:
        log(string=error.__str__(), type=1, fileName=file_name)
        return False
    

def inputFileName() -> str:
    return input("\nInserisci il nome del file dove vuoi salvare la password: ")
    
def log(string : str, type : int, fileName : str):
    """
    Save in a log file all the processes/error of the program

    Type:
        0 - Password generated successfully
        1 - Error. Could not open the file

    return void
    """
    
    s = datetime.now().__str__() + "\n"
    if type == 0:
        s += "LOG: " + string + "\n"
    else:
        s += "ERROR: " + string + "\n"
    s += "File Name: " + fileName + "\nLocation: Desktop\n\n"
    path = "C:\\lavori\\psw_log\\"
    os.chdir(path)
    file = open("log.log", "a")
    file.write(s)
    file.close()


main()