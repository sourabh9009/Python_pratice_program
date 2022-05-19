class Contact:
    def _init_ (self,Contact_Name,Contact_Number):
        self.Contact_Name= Contact_Name
        self.Contact_Number=Contact_Number
    def Get_data(self):
        data = open("Data.txt","r")
        Contact_Data = data.read()
        data.close()
        return Contact_Data
    def Put_data(self,Contact_name,Contact_Number):

        data = open("Data.txt","a")
        data.write("Contact Name Is :" +Contact_name +"\n")
        data.write("Contact Number  Is :" +Contact_Number)
        data.close()
Contact_Name=input("Enter Your Contact Name :")
Contact_Number=input("Enter Your Contact Number :")

CN1=Contact(Contact_Name,Contact_Number)
CN1.Put_data(Contact_Name,Contact_Number)
print(CN1.Get_data())