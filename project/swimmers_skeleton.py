import mysql.connector
from db_config import db_config

# Creating class 
class SwimmersDAO:
    def __init__(self):
        self.host = db_config["host"]
        self.user = db_config["user"]
        self.password = db_config["password"]
        self.database = db_config["database"]
    
    
    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database      
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    
    # get all swimmers
# code MySQL fixed with AI: 
# Using TIME_FORMAT to convert MySQL TIME field into a string.
# This prevents Python from returning a 'timedelta' object, which cannot be serialized to JSON.
# The formatted string ('HH:MM:SS') is safe to use in templates and API responses.

    def get_all(self, limit=10, offset=0):
        cursor = self.getCursor()
        try:
            sql = """
                SELECT id, first_name, last_name, sex, age_group, event, date,
                TIME_FORMAT(time, '%H:%i:%s') AS time
                FROM results
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            swimmers_list = []
            for row in result:
                swimmers_list.append(self.convertToDict(row))
            return swimmers_list
        finally:
            self.closeAll()
        self.closeAll()
        return swimmers_list
    
    
    # find by id
    def find_by_id(self,id):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)
    
    # find by age group
    def find_by_age_group(self,age_group):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE age_group = %s"
        values = (age_group,)
        cursor.execute(sql,values)
        result = cursor.fetchall()
        swimmers_list = []
        for row in result:
            swimmers_list.append(self.convertToDict(row))
        self.closeAll()
        return swimmers_list
    
    
    # only Girls
    def find_girls(self, sex):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE sex = %s"
        values = ("F",)
        cursor.execute(sql,values)
        result = cursor.fetchall()
        swimmers_list = []
        for row in result:
            swimmers_list.append(self.convertToDict(row))
        self.closeAll()
        return swimmers_list
    
    # only Boys
    def find_boys(self, sex):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE sex = %s"
        values = ("M",)
        cursor.execute(sql,values)
        result = cursor.fetchall()
        swimmers_list = []
        for row in result:
            swimmers_list.append(self.convertToDict(row))
        self.closeAll()
        return swimmers_list
        
        
    # create a new gala result    
    def create(self, swimmer):
        cursor = self.getCursor()
        sql = """
        insert into results (first_name, last_name, sex, age_group, event, date, time)
        values (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            swimmer.get("first_name"),
            swimmer.get("last_name"),
            swimmer.get("sex"),
            swimmer.get("age_group"),
            swimmer.get("event"),
            swimmer.get("date"),
            swimmer.get("time")
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return {"message": "Swimmer's record created"}
                
    # update swimmer record   
    def update(self, id, swimmer):
        cursor = self.getCursor()
        sql = """
        update results SET first_name=%s, last_name=%s, sex=%s, age_group=%s, event=%s, date=%s, time=%s
        where id = %s
        """
        values = (
            swimmer.get("first_name"),
            swimmer.get("last_name"),
            swimmer.get("sex"),
            swimmer.get("age_group"),
            swimmer.get("event"),
            swimmer.get("date"),
            swimmer.get("time"),
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return {"message": "Swimmer's record updated successfully"}
            
    # delete by ID
    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from results where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return {"message": "Swimmer's record deleted"}
    
    # Make a dict from keys and values
    # https://stackoverflow.com/questions/209840/make-a-dictionary-dict-from-separate-lists-of-keys-and-values
    
    # 
    def convertToDict(self,resultline):
        keys = ["id", "first_name", "last_name", "sex", "age_group", "event", "date", "time"]
        dictionary = dict(zip(keys,resultline))
        return dictionary
        
        
swimDAO = SwimmersDAO()    