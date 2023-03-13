import requests

class Produit():
    """gère
    """
    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:8000"



    def produit(self) :
        req = requests.get(f"{self.__HOST}/")
        return req.json()
        
if __name__ == "__main__":
    prod = Produit()
    json = prod.produit()
    print(json)