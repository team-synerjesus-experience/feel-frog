import sqlite3

class Database:
  def __init__(self, dbPath):
    self.connection = sqlite3.connect(dbPath)
    self.cursor = self.connection.cursor()
    
  def ensureTable(self, table,schema):
    "Ensures that a table exists creating it with schema if it doesn't"
    re = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='%s'" % table)
    if re.fetchall() == []:
      self.cursor.execute("CREATE TABLE %s %s" % (table, str(schema)))
      self.connection.commit()

  def addUser(self,uname,email,real_name):
    self.userTableSchema = '(uname,email,real_name)'
    self.ensureTable('Users', self.userTableSchema)
    if self.validEmail(email) and self.uniqueName(uname):
      self.cursor.execute("INSERT INTO Users %s VALUES %s" % (str(self.userTableSchema),str((uname,email, real_name))))

  def validEmail(self, email):
    re = self.cursor.execute("SELECT email FROM Users WHERE email='%s'" % email)
    self.ensureTable('Users', self.userTableSchema)
    if re.fetchall() == []:
      return True
    return False

  def uniqueName(self,uname):
    self.ensureTable('Users', self.userTableSchema)
    re = self.cursor.execute("SELECT uname FROM Users WHERE uname='%s'" % uname)
    data = re.fetchall()
    if data == []:
      return True
    return False

  def addActivity(self,uname, atvyCat, startTime,stopTime):
    "Stores activity from category with time and date"
    schema = '(uname,activity,startTime,stopTime)'
    self.ensureTable('Activities',schema)
    if not self.uniqueName(uname):
      self.cursor.execute("INSERT INTO Activities %s VALUES %s" % (schema,str((uname, atvyCat,startTime,stopTime))))
      self.connection.commit()

if __name__ == '__main__':
  db = Database('d.db')
  x = db.addUser("donal","renegadethunder@gmail.com","Donal O'Shea")
  x = db.addActivity("donal","fish",12,16)
 
