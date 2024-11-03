class Goalkeeping_peromance:
    def __init__(self, GA='N/A', GA90='N/A', SoTA='N/A', Saves='N/A', Save_percent='N/A', 
                 W='N/A', D='N/A', L='N/A', CS='N/A', CS_percent='N/A'):
        self.__GA = GA
        self.__GA90 = GA90
        self.__SoTA = SoTA
        self.__Saves = Saves
        self.__Save_percent = Save_percent
        self.__W = W
        self.__D = D
        self.__L = L
        self.__CS = CS
        self.__CS_percent = CS_percent

    def get_GA(self):
        return self.__GA

    def get_GA90(self):
        return self.__GA90

    def get_SoTA(self):
        return self.__SoTA

    def get_Saves(self):
        return self.__Saves

    def get_Save_percent(self):
        return self.__Save_percent

    def get_W(self):
        return self.__W

    def get_D(self):
        return self.__D

    def get_L(self):
        return self.__L

    def get_CS(self):
        return self.__CS

    def get_CS_percent(self):
        return self.__CS_percent

    def set_GA(self, GA):
        self.__GA = GA

    def set_GA90(self, GA90):
        self.__GA90 = GA90

    def set_SoTA(self, SoTA):
        self.__SoTA = SoTA

    def set_Saves(self, Saves):
        self.__Saves = Saves

    def set_Save_percent(self, Save_percent):
        self.__Save_percent = Save_percent

    def set_W(self, W):
        self.__W = W

    def set_D(self, D):
        self.__D = D

    def set_L(self, L):
        self.__L = L

    def set_CS(self, CS):
        self.__CS = CS

    def set_CS_percent(self, CS_percent):
        self.__CS_percent = CS_percent

    def __str__(self):
        return (f"Goalkeeping Performance:\n"
                f"Goals Against (GA): {self.__GA}\n"
                f"Goals Against per 90 (GA90): {self.__GA90}\n"
                f"Shots on Target Against (SoTA): {self.__SoTA}\n"
                f"Saves: {self.__Saves}\n"
                f"Save Percentage (Save%): {self.__Save_percent}\n"
                f"Wins (W): {self.__W}\n"
                f"Draws (D): {self.__D}\n"
                f"Losses (L): {self.__L}\n"
                f"Clean Sheets (CS): {self.__CS}\n"
                f"Clean Sheet Percentage (CS%): {self.__CS_percent}")
