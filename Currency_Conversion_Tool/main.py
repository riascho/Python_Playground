import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
window.title("EUR <-> USD Conversion")


def runEUR():
  try:
    eur = float(userInputEUR.get("1.0", "end"))
    resultEUR = eur * 0.9224  #check source for current rate
    resultEUR = round(resultEUR, 2)
    labelEUR["text"] = f"{resultEUR} €"
    userInputEUR.delete("1.0", "end")
  except:
    labelEUR["text"] = 'only enter numbers and "." '
    userInputEUR.delete("1.0", "end")


def runUSD():
  try:
    usd = float(userInputUSD.get("1.0", "end"))
    resultUSD = usd * 1.08413000  #check source for current rate
    resultUSD = round(resultUSD, 2)
    labelUSD["text"] = f"{resultUSD} $"
    userInputUSD.delete("1.0", "end")
  except:
    labelUSD["text"] = 'only enter numbers and "." '
    userInputUSD.delete("1.0", "end")


label = tk.Label(window,
                 text="Enter Your Conversion Amount",
                 font=('Arial', 14))
label.pack(padx=20, pady=20)

## EUR Conversion ##

userInputEUR = tk.Text(window, height=1, font=('Arial', 18))
userInputEUR.pack(padx=10)

buttonEUR = tk.Button(window,
                      text="convert to EUR",
                      font=("Calibri", 18),
                      command=runEUR)
buttonEUR.pack()

labelEUR = tk.Label(window, text=" ", font=('Arial', 18))
labelEUR.pack(padx=20, pady=20)

## USD Conversion ##

userInputUSD = tk.Text(window, height=1, font=('Arial', 18))
userInputUSD.pack(padx=10)

buttonUSD = tk.Button(window,
                      text="convert to USD",
                      font=("Calibri", 18),
                      command=runUSD)
buttonUSD.pack()

labelUSD = tk.Label(window, text=" ", font=('Arial', 18))
labelUSD.pack(padx=20, pady=20)

####

tag = tk.Label(window, text="© 2023 made by Maria 'Surfineer' Scholz", font=('Arial', 8))
tag.pack(side=tk.BOTTOM)

window.mainloop()
