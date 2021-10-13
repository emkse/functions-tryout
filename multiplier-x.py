from typing import NoReturn


Getal = int(input("Van welk getal wilt u in de tafel zien?? 1 tot en met 10"))
def tafelX(noemer: int):
    for teller in range(1,11):
        print(teller,"x", noemer, "=", teller * noemer)
tafelX(Getal)

