"""
Name: Aaryan Sharma
Program-2 : Chicago Lobbyist Database App
CS - 341 (Spring 2024)
Professor: Ellen Kidane
"""


import datatier


class Lobbyist:                                                                                                         # Definition for class "Lobbyist".
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone


class LobbyistDetails:                                                                                                  # Definition for class "LobbyistDetails".
   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
      self._Lobbyist_ID = Lobbyist_ID
      self._Salutation = Salutation
      self._First_Name = First_Name
      self._Middle_Initial = Middle_Initial
      self._Last_Name = Last_Name
      self._Suffix = Suffix
      self._Address_1 = Address_1
      self._Address_2 = Address_2
      self._City = City
      self._State_Initial = State_Initial
      self._Zip_Code = Zip_Code
      self._Country = Country
      self._Email = Email
      self._Phone = Phone
      self._Fax = Fax
      self._Years_Registered = Years_Registered
      self._Employers = Employers
      self._Total_Compensation = Total_Compensation

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Initial

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone

   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered

   @property
   def Employers(self):
      return self._Employers

   @property
   def Total_Compensation(self):
      return self._Total_Compensation


class LobbyistClients:                                                                                                  # Definition for class "LobbyistClients".
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

   @property
   def Clients(self):
      return self._Clients


def CheckTuple(tuple, x = 1):                                                                                           # This is a helper function, which is employed in the functions below.

   if (x == 1):
      if ((tuple == ()) or (tuple is None)):
         return False

   elif (x == 2):
      if (tuple is None):
         return False

   return True


def num_lobbyists(dbConn):                                                                                              # This function returns the number of lobbyists in the database, and if an error occurs, the function returns -1.
   query = "SELECT COUNT(*) FROM lobbyistinfo"
   result = datatier.select_one_row(dbConn, query)

   if (not CheckTuple(result)):
      return -1

   return result[0]


def num_employers(dbConn):                                                                                              # This function returns the number of employers in the database, and if an error occurs, the function returns -1
   query = "SELECT COUNT(*) FROM employerinfo"
   result = datatier.select_one_row(dbConn, query)

   if (not CheckTuple(result)):
      return -1

   return result[0]


def num_clients(dbConn):                                                                                                # This function returns the number of clients in the database, and if an error occurs, the function returns -1
   query = "SELECT COUNT(*) FROM clientinfo"
   result = datatier.select_one_row(dbConn, query)

   if (not CheckTuple(result)):
      return -1

   return result[0]


def get_lobbyists(dbConn, pattern):                                                                                     # This function returns the list of lobbyists in ascending order by ID, and incorporates error handling.
   query = "SELECT lobbyist_id, first_name, last_name, phone FROM LobbyistInfo WHERE first_name LIKE ? OR last_name LIKE ? ORDER BY lobbyist_id"
   result = datatier.select_n_rows(dbConn, query, [pattern, pattern])
   data = []

   if (not CheckTuple(result, 2)):
      return data

   for row in result:
      data.append(Lobbyist(*row))

   return data


def get_lobbyist_details(dbConn, lobbyist_id):                                                                          # This function returns a LobbyistDetails object, if the search is successful.
   queryLobbyist = "SELECT * FROM lobbyistinfo WHERE lobbyist_id = ?"
   queryYears = "SELECT year FROM lobbyistyears WHERE lobbyist_id = ?"
   queryEmployers = """ SELECT DISTINCT employer_name
                        FROM employerinfo ei
                        JOIN lobbyistandemployer lae ON ei.employer_id = lae.employer_id
                        WHERE lobbyist_id = ?
                        ORDER BY employer_name"""
   queryComp = "SELECT SUM(compensation_amount) FROM compensation WHERE lobbyist_id = ?;"
   years = []
   employers = []
   total = 0

   result = datatier.select_one_row(dbConn, queryLobbyist, [lobbyist_id])

   if (not CheckTuple(result  )):                                                                                       # Checking whether the Lobbyist with "lobbyist_id" exists in the database.
      return None

   resultYears = datatier.select_n_rows(dbConn, queryYears, [lobbyist_id])
   resultEmployers = datatier.select_n_rows(dbConn, queryEmployers, [lobbyist_id])
   resultComp = datatier.select_one_row(dbConn, queryComp, [lobbyist_id])

   for row in resultYears:                                                                                              # Looping over the tuples to convert them into lists.
      years.append(row[0])

   for row in resultEmployers:
      employers.append(row[0])

   if (resultComp is not None) and (resultComp[0] is not None):
      total = resultComp[0]

   return LobbyistDetails( result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7],
      result[8], result[9], result[10], result[11], result[12], result[13], result[14], years, employers, total)



def get_top_N_lobbyists(dbConn, N, year):                                                                               # This function returns a list of 0 or more LobbyistClients objects.
   queryLobbyist = """SELECT li.lobbyist_id, li.first_name, li.last_name, li.phone, SUM(c.compensation_amount)
                      FROM lobbyistinfo li
                      JOIN compensation c ON c.lobbyist_id = li.lobbyist_id
                      WHERE strftime('%Y', c.period_end) = ?
                      GROUP BY c.lobbyist_id
                      ORDER BY SUM(c.compensation_amount) DESC
                      LIMIT ?;"""
   queryClient = """SELECT DISTINCT ci.client_id, ci.client_name
                    FROM clientinfo ci
                    JOIN compensation c ON c.client_id = ci.client_id
                    WHERE strftime('%Y', c.period_end) = ? AND c.lobbyist_id = ?
                    ORDER BY ci.client_name ASC;"""
   lobbyists = []
   result = datatier.select_n_rows(dbConn, queryLobbyist, [year, N])

   if not CheckTuple(result, 2):
      return None

   for row in result:
      resultClient = datatier.select_n_rows(dbConn, queryClient, [year, row[0]])
      clients = []

      for rows in resultClient:
         clients.append(rows[1])

      lobbyists.append(LobbyistClients(row[0], row[1], row[2], row[3], row[4], clients))                                # Adding all of the "LobbyistClient" objects to the "lobbyists" list.

   return lobbyists


def add_lobbyist_year(dbConn, lobbyist_id, year):                                                                       # This function inserts the given year into the database for the given lobbyist.
   query = "SELECT COUNT(*) FROM lobbyistinfo WHERE lobbyist_id = ?"
   result = datatier.select_one_row(dbConn, query, [lobbyist_id])

   if (result[0] <= 0):
      return 0

   queryYear = "INSERT INTO lobbyistyears (lobbyist_id, year) VALUES (?, ?)"
   datatier.perform_action(dbConn, queryYear, [lobbyist_id, year])
   return 1


def set_salutation(dbConn, lobbyist_id, salutation):                                                                    # This function sets the salutation for the given lobbyist.
   query = "SELECT COUNT(*) FROM lobbyistinfo WHERE lobbyist_id = ?"
   result = datatier.select_one_row(dbConn, query, [lobbyist_id])

   if (result[0] <= 0):
      return 0

   querySalutation = "UPDATE lobbyistinfo SET salutation = ? WHERE lobbyist_id = ?"
   datatier.perform_action(dbConn, querySalutation, [salutation, lobbyist_id])
   return 1