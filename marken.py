#%%


class MichNr:
    def __init__(self, gebiet : str, michnr: int, bild = None):
        self.gebiet = gebiet
        self.michnr = michnr
        self.bild = bild
    def __str__(self):
        return f"{self.gebiet}, MichNr {self.michnr}"

#%%
class Marke(MichNr):
    def __init__(self, gebiet, michnr, entwertung, bild = None,  besitz = 0):
        super().__init__(gebiet, michnr, bild)
        self.entwertung = entwertung
        self.besitz = besitz


#%%
m1 = Marke("re", 1, bild=None, entwertung="gest")





# %%
print(type(m1))

# %%
