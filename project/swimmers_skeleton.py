import mysql.connector
from db_config import db_config

# Creating class 
class SwimmersDAO:
    def __init__(self):
        self.host = db_config["host"],
        self.user = db_config["user"],
        self.password = db_config["password"],
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
    def get_all(self):
        cursor = self.getCursor()
        sql = "select * from results"
        cursor.execute(sql)
        result = cursor.fetchall()
        swimmers_list = []
        for row in result:
            swimmers_list.append(self.convertToDict(row))
        self.closeAll()
        return swimmers_list
    
    
    # find by id
    def find_by_id(self,id):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchall()
        self.closeAll()
        return self.convertToDict(result)
    
        # find by age group
    def find_by_id(self,age_group):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE age_group = %s"
        values = (age_group,)
        cursor.execute(sql,values)
        result = cursor.fetchall()
        self.closeAll()
        return self.convertToDict(result)
    
    
        # only Girls
    def find_by_id(self, sex):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE sex = %s"
        values = ("F",)
        cursor.execute(sql,values)
        result = cursor.fetchall()
        self.closeAll()
        return self.convertToDict(result)
    
            # only Boys
    def find_by_id(self, sex):
        cursor = self.getCursor()
        sql = "SELECT * FROM results WHERE sex = %s"
        values = ("M",)
        cursor.execute(sql,values)
        result = cursor.fetchall()
        self.closeAll()
        return self.convertToDict(result)
        
        
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
            swimmer.get("time"),
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return {"message": "Swimmer's record updated"}
                
    # update swimmer record   
    def update(self, id, swimmer):
        cursor = self.getCursor()
        sql = """
        update results SET first_name=%s, last_name=%s, sex=%s, age_group=%s, event=%s, date=%s, time=%s)
        where id =%s
        values (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            swimmer.get("first_name")
            swimmer.get("last_name")
            swimmer.get("sex")
            swimmer.get("age_group")
            swimmer.get("event")
            swimmer.get("date")
            swimmer.get("time"),
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return {"message": "Swimmer added successfully"}
        
    
    
    
    
    
    # delete
    def delete(self, id):
        print (f"Swimmer with id {id} deleted")
        
    SwimmersDAO = SwimmersDAO()