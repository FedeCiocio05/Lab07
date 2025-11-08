from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    def get_artefatti_filtrati(self, museo: str | None, epoca: str | None):
        cnx = ConnessioneDB.get_connection()
        artefatti = []

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = (
            """
            SELECT a.id, a.nome, a.tipologia, a.epoca, a.id_museo
            FROM artefatto AS a
            JOIN museo AS m ON a.id_museo = m.id
            WHERE (%s IS NULL OR m.nome = %s)
              AND (%s IS NULL OR a.epoca = %s)
            ORDER BY a.nome
            """
        )

        params = (museo, museo, epoca, epoca)
        cursor.execute(query, params)

        for row in cursor:
            artefatti.append(Artefatto(
                id=row["id"],
                nome=row["nome"],
                tipologia=row["tipologia"],
                epoca=row["epoca"],
                id_museo=row["id_museo"]
            ))

        cursor.close()
        cnx.close()

        return artefatti
    # TODO