
# importing the document object from pyscript module
from pyscript import document
from pyscript import when, display
# Note: the module name is psycopg, not psycopg3
import psycopg
from urllib.parse import urlparse

#from pyodide.ffi.wrappers import add_event_listener

"""

Failed to remove contents in a temporary directory 
'C:\Users\Dell\AppData\Local\Programs\Python\Python314\Lib\site-packages\~sycopg2_binary.libs'.
You can safely remove it manually.

"""



class Customer: 
    def __init__(self, first_name, last_name, email,
      phone_number, address): 
      self.first_name = first_name 
      self.last_name = last_name
      self.email = email 
      self.phone_number = phone_number 
      self.address = address 
    
    
# Sample customer data 
customers = [
    Customer("John", "Doe", "john.doe@example.com", "123-456-7890", "123 Main St"), 
    Customer("Jane", "Smith", "jane.smith@example.com", "098-765-4321", "456 Oak Ave"),
    Customer("Bob", "Johnson", "bob.johnson@example.com", "555-1234", "789Pine Rd"), 
    Customer("Alice", "Williams", "alice.williams@example.com","555-5678", "321 Elm Dr")]  
 


def myfunc():
    
    print("Hello from Python in main.py!")
    for customer in customers:
        print(f"Name: {customer.first_name} {customer.last_name}")
        print(f"Email: {customer.email}")
        print(f"Phone: {customer.phone_number}")
        print(f"Address: {customer.address}")
        print("-" * 20)
      




@when("py-click", "#btnHome")
def say_hello(event):
    document.getElementById("mainhdr").style.display = "block"
    document.getElementById("mainhdr").innerHTML = "<h1>" + event.target.innerText + "</h1>"
    button_id = event.target.id
    display("Hello from Python!")  
    #js.alert("Hello from Python! You clicked the " + button_id + " button.") 

@when("click",  "#btnAbout", "#btnProducts", "#btnContact", "#btnAdmin")
def handler(event):
    
    #input("Button clicked! " + event.target.innerText + " Press Enter to continue...")
    document.getElementById("mainhdr").style.display = "block"
    choice = event.target.innerText
    #display("Button clicked! " + choice)
    match choice:
        case "Home":
            document.getElementById("mainhdr").innerHTML = "<h1>" + choice + "</h1>"
            return choice

        case "Admin":
            document.getElementById("mainhdr").innerHTML = "<h1>" + choice + "</h1>"
            return choice
        
        case "About":
            # connect_to_db()
            document.getElementById("mainhdr").innerHTML = "<h1>" + choice + "</h1>"

            return choice
        
        case "Products":
            document.getElementById("mainhdr").innerHTML = "<h1>" + choice + "</h1>"
            return choice
       
        case "Contact":
            document.getElementById("mainhdr").innerHTML = "<h1>" + choice + "</h1>"
            return choice
       
        case _:
            return "Unsupported user choice. Please select a valid option."
    

#document.getElementById("btnHome").bind("click", handler)
#document.getElementById("btnAbout").bind("click", handler)

#document.getElementById("btnHome").addEventListener("py-click", say_hello)
#document.getElementById("btnAbout").addEventListener("click", handler)
#document.getElementById("btnProducts").addEventListener("click", handler)
#document.getElementById("btnContact").addEventListener("click", handler)
#document.getElementById("btnAdmin").addEventListener("click", handler)





