from dojosAndNinjas_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

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