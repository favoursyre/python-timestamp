#I want to create a generic datetime module for recording the timestamp of any python related tutorial that I undertake

#Useful libraries that I would be working with -->
try:
    import datetime
    from colored import fg, attr
    from pyfiglet import Figlet, FigletFont
    import pyfiglet
    import pyfiglet.fonts
    import traceback
except Exception as e:
    print(f"An error occurred in imported libraries due to [{e}]")



#Declaring the code timestamp class
class codeTimestamp():
    def __init__(self, author, projectName, framework, year, month, day, hour, minute, seconds):
        self.author = author
        self.projectName = projectName.title()
        self.framework = framework.title()
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.seconds = seconds
        if self.projectName[0] in ["A", "E", "I", "O", "U"]:
            self.letter = "an"
        else:
            self.letter = "a"

        self.CurrentDate = datetime.datetime.now()
        #format(year, month, day, hour, minute, second)
        self.StartDate = datetime.datetime(year, month, day, hour, minute, seconds)
        self.NewDate = self.CurrentDate - self.StartDate 

    def display(self, show = True):
        if show:
            print(f"I want to create {self.letter} {self.projectName} using {self.framework} framework")
            print(f"I began this {self.framework} {self.projectName} Project {self.NewDate.days} days ago")
            print(self.CurrentDate.strftime("""And you're viewing this live at %H:%M:%S %p. %d %B, %Y\n
            Have Fun!!\n"""))

            try:
                res = pyfiglet.figlet_format(f"{self.projectName}", font = "larry3d")
                print(f"{fg(3)}     (                                             (                 {attr(0)}") 
                print(f"{fg(3)}    )\ )                            )            )\ )                {attr(0)}")
                print(f"{fg(3)}   (()/(       )   )     )       ( /(   (   (   (()/(  (   (         {attr(0)}") 
                print(f"{res}")
                print(f"{fg(9)}  )()/(_)) (  (   )    (          )\()) ))\  )(   /(_)) )\  )(   (   {attr(0)}")
                print(f"{fg(1)} ((_))_ ))\  _ (  _  ` _) __(  (_))/ /((_)(()\ (_))_|((_)(()\ ))\ )  {attr(0)}")
                print()
                print(f"{'~' * 50} \nAuthor: {self.author} \n{'~' * 50}")
                print()
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Happy Hacking!! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
            except:
                print(f"An error occurred in code timestamp due to {traceback.print_exc()}")
                print(f"{'~' * 50} \nAuthor: {self.author} \n{'~' * 50}")
        else:
            pass


#Just testing the code 
if __name__ == "__main__":
    #Commencing the code --> 
    codeTimestamp("Syre Musk", "Code Timestamp", "python", 2021, 12, 11, 13, 52, 10).display()








