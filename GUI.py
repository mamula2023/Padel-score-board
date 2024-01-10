import tkinter as tk
import Score
import Team
class gameDisplay:
    def __init__(self, team1: Team, team2: Team, score:Score):
        self.mainDisplay=tk.Tk()
        self.score = score    

        screenWidth = str(self.mainDisplay.winfo_screenwidth())
        screenHeight= str(self.mainDisplay.winfo_screenheight())
        self.mainDisplay.wm_geometry(screenWidth+"x"+screenHeight)
        self.mainDisplay.title("Display")


        self.frame=tk.Frame(self.mainDisplay, highlightbackground="blue", highlightthickness=2)
        self.frame.pack(padx=100, pady=100)
        self.frame.rowconfigure(0, weight = 1)
        self.frame.rowconfigure(1, weight = 1)

        for i in range(score.__nSets__+1):
            self.frame.columnconfigure(i+1, weight=1)

        firstTeam=tk.Label(self.frame, text=team1.getDisplay(), font = ("arial", 25), padx=20, pady=20)
        secondTeam=tk.Label(self.frame, text=team2.getDisplay(), font = ("arial", 25), padx = 20, pady = 20)

        self.firstTeamWon = tk.Button(self.mainDisplay, text="team one", font=("arial", 25), padx=2, pady=2, command=lambda:self.scored(1))
        self.firstTeamWon.pack()
        self.secondTeamWon = tk.Button(self.mainDisplay, text="team two", font=("arial", 25), padx=2, pady=2, command=lambda:self.scored(2))
        self.secondTeamWon.pack()
         
        self.labels = []
        self.labels.append([firstTeam])
        self.labels.append([secondTeam])
        for i in range(self.score.__nSets__+1):
            tempLabel1=tk.Label(self.frame, text=0, font = ("arial", 25), padx = 20, pady = 20)
            tempLabel2=tk.Label(self.frame, text=0, font = ("arial", 25), padx = 20, pady = 20)
            self.labels[0].append(tempLabel1)
            self.labels[1].append(tempLabel2)
        
        self.updateScore()


        self.mainDisplay['background']="#3366BB"
        self.mainDisplay.mainloop()
    
    def updateScore(self):
        print("called")
        self.labels[0][0].grid(row = 0, column = 0)
        self.labels[1][0].grid(row = 1, column = 0)

        for i in range(len(self.score.__sets__)):
            self.labels[0][i+1].grid(row=0, column = i+1)
            self.labels[0][i+1].config(text = self.score.__sets__[i][0])
            self.labels[1][i+1].grid(row = 1, column = i+1)
            self.labels[1][i+1].config(text = self.score.__sets__[i][1])
        
        self.labels[0][-1].grid(row = 0, column = len(self.labels[0])-1)
        self.labels[0][-1].config(text = self.score.getCurrGame(1))
        self.labels[1][-1].grid(row = 1, column = len(self.labels[1])-1)
        self.labels[1][-1].config(text = self.score.getCurrGame(2))    

    def scored(self, team):
        print(team)
        self.mainDisplay.wait_variable = team

        result = self.score.newPoint(team)
        self.updateScore()
        if result:
            print("finished")
            return
        
        
           


