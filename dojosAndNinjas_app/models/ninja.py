from dojosAndNinjas_app.config.mysqlconnection import connectToMySQL
from dojosAndNinjas_app.models.dojo import Dojo

class Ninja:
    def __init__( self, data ):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age= data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]
        self.dojo = None

    @classmethod
    def add_ninja( cls, data ):
        query = "INSERT INTO ninjas ( dojo_id, first_name, last_name, age ) VALUES ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s );"
        new_ninja = connectToMySQL("dojosAndNinjas_schema").query_db( query, data )
        return new_ninja