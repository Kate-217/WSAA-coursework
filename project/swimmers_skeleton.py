import mysql.connector

# Creating class 
class SwimmersDAO:
    host = "localhost"
    user = "root"
    password = "rootroot"
    database = "swimmers"
    connection = ""
    cursor = ""
    
    # get all
    def get_all(self):
        return [{
            "id":1,
            "first_name":"name",
            "last_name":"surname",
            "sex":"F",
            "age_group":12,
            "event":"50 free style",
            "date":"2025-02-01",
            "time":"00:03:46"
        }]
        
        
    # find by id
    def find_by_id(self,id):
        return [{
            "id":1,
            "first_name":"name",
            "last_name":"surname",
            "sex":"F",
            "age_group":12,
            "event":"50 free style",
            "date":"2025-02-01",
            "time":"00:03:46"
        }]
        
    # create    
    def create(self, result):
        result["id"]=2
        return result
        
    # update    
    def update(self, id, result):
        print (f"Swimmer with id {id} updated")
    
    # delete
    def delete(self, id):
        print (f"Swimmer with id {id} deleted")
        
    SwimmersDAO = SwimmersDAO()