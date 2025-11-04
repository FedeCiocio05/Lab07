from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def get_musei(self):
        cnx = ConnessioneDB.get_connection()
        lst_musei = []
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            # Query parametrizzata, richiamata ogni volta che l'utente cambia il numero di stelle nella casella dropdown
            query = """SELECT * FROM musei"""
            cursor.execute(query)
            for row in cursor:
                lst_musei.append(Museo(**row))

            cursor.close()
            cnx.close()
            return lst_musei


    def get_epoche(self):
        cnx = ConnessioneDB.get_connection()
        lst_epoche = []
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            # Query parametrizzata, richiamata ogni volta che l'utente cambia il numero di stelle nella casella dropdown
            query = """SELECT DISTINCT(epoca) FROM artefatti"""
            cursor.execute(query)
            for row in cursor:
                lst_epoche.append(Museo(**row))

            cursor.close()
            cnx.close()
            return lst_epoche

        #poi passo a model, poi controller e infine creo nel controller il metodo che popola il dropdown nel NB
    # TODO
