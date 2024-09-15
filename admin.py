
class Admin:

    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username
    def getId(self):
        return self.username
    def getPassword(self):
        return self.username

    def setUsername(self,username):
        self.username = username
    def setId(self,id):
        self.id = id
    def setPassword(self,password):
        self.password = password

    def ajouterAdmin(self):
        query = "INSERT INTO admins VALUES(%s, %s, %s)"
        return query
    def checkAdmin(self):
        return self.username,self.password