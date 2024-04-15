import mysql.connector
from database.DB_connect import DBConnect
from model.corso import Corso
class CorsoDao:

    @staticmethod       ## è statica perché dentro non ha nessun dato, è un contenitore di metodi, se static NON METTERE SELF
    def get_corsi_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary = True)
            query = """
                    select c.*
                    from corso c
                    where c.pd = %s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_studenti_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct i.matricola
                        from iscrizione i, corso c 
                        where i.codins = c.codins and c.pd = %s"""
            cursor.execute(query, (pd,))
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows

    @staticmethod
    def get_studenti_singolo_corso(codins):
        cnx = DBConnect.get_connection()
        result = set()
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select i.matricola
                        from iscrizione i
                        where i.codins = %s"""
            cursor.execute(query, (codins,))
            for row in cursor:
                result.add(row["matricola"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_all_corsi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select *
                                from corso c """

            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result