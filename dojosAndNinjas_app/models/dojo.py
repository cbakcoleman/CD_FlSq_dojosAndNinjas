from dojosAndNinjas_app.config.mysqlconnection import connectToMySQL
from dojosAndNinjas_app.models import ninja

class Dojo:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojosAndNinjas_schema").query_db( query )
        dojos_all = []
        for row in results:
            dojos_all.append( cls(row) )
        return dojos_all

    @classmethod
    def add_dojo( cls, data ):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        new_dojo = connectToMySQL("dojosAndNinjas_schema").query_db( query, data )
        return new_dojo

    @classmethod
    def dojo_ind( cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s ;"
        results = connectToMySQL("dojosAndNinjas_schema").query_db( query, data )

        dojo = cls(results[0])

        for row in results:
            data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(data))
        return dojo