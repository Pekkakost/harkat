# tee ratkaisu tänne
def lue_hedelmat():
    with open("hedelmat.csv")as tiedosto:
        sanakirja = {}
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(";")
            nimi = osat[0]
            arvo = float(osat[1])
            sanakirja[nimi] = arvo
        return sanakirja


if __name__ == "__main__":

    print(lue_hedelmat())

Opettaja:


def lue_hedelmat():
    with open("hedelmat.csv") as tiedosto:
        hedelmat = {}
        for rivi in tiedosto:
            # puretaan kahdeksi palaksi
            tiedot = rivi.split(";")
            # nimi on eka, hinta toka
            hedelmat[tiedot[0]] = float(tiedot[1])
    return hedelmat
