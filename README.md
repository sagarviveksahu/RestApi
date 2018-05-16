
# REST APIs

Language: Python 3
Web Framework: Flask
Liberaries: flask, unittest
Database: In Memory JSON DB, We can use any Database according to our need.
API Development Tool: Postman, API Testing client(google chrome 	extension or using Command line (using CURL))

# Files included: 
	
	1) run.py (main program file)
	2) test.py (unittest file)
	3) README.txt (readme)


# API Endpoints:

1) Get all records

	http://localhost:5000/employee/			method: GET

2) Create a contact record:

	http://localhost:5000/employee/create		method: POST

3) Retrieve a contact record:

	http://localhost:5000/employee/<name>		method: GET

4) Update a contact record:

	http://localhost:5000/employee/<name>		method: PUT

5) Delete a contact record:

	http://localhost:5000/employee/<name>		method: DELETE

6) Search for a record by email or phone number:

	http://localhost:5000/employee/<string>	method: GET

7) Retrieve all records from the same state or city:

	http://localhost:5000/employee/<place>		method: GET


Contact record has followinf feilds:

- name
- company
- image(image path)
- email
- birthdate
- phone
	- work
	- personal
- address
	- street
	- city
	- state




# HOW TO RUN APIs :

1) Install python

2) Install Flask
	
	- pip install Flask

3) Open 2 terminals:

	- 1 for running web server
	- 1 for api operations

4) In 1st terminal run:

	- python run.py

5) In 2nd terminal run following commands:

	a) To create a contact record:

	$ curl -i -H "Content-type: application/json" -X POST -d 	'{"name":"vivek","company":"Google","image":"1.png","email":	"abc@gmail.com","birthdate":"01/01/1991","phone":{"work":"
	3123123123","personal":"1223123332"},"address":{"street":"88	01","city":"nyc","state":"ny"}}' 	http://localhost:5000/employee/create

	- you can create any number of contacts just replacing the 	values inside the dictionary


	b) To retrieve a contact record:

	$ curl -i http://localhost:5000/employee/<name>


	c) To get all records:

	$ curl -i http://localhost:5000/employee


	d) To update a record:
	
	$ curl -i -H "Content-type: application/json" -X PUT -d 	'{"email":"efgv@gmail.com","company":"Apple"}' 	http://localhost:5000/employee/<name>


	e) To delete a record:
	
	$ curl -i -X DELETE http://localhost:5000/employee/<name>

	
	f) To Search for a record by email or phone number:

	$ curl -i http://localhost:5000/employee/<email or phone>


	f) To Retrieve all records from the same state or city:

	$ curl -i http://localhost:5000/employee/<place>




How to run Unittest:

	- python -m unittest



# PROGRAM EXPLAINATION:

- I have created an in-memory JSON DB to store and manipulate a simple contact record database and develop RESTful APIs to perform CRUD operations using GET, POST, PUT, and DELETE methods.

- First I have created a web server, and a dictionary to hold a JSON objects for a couple of contact records and then we add RESTful APIs for each supported operations.

- POST method is used to create a new contact record inside the database. createEmp() function simply reads the request.json for the expected values, and stores them in the local dictionary object and appends it to the employee DB dictionary. This also returns the newly added employee object as the response.

- GET method is used to retrieve a specific contact record or all of them from the DB. getEmp() and getAllEmp() will find the contact object with the given name and send the JSON object in the data.

- PUT method is used to update the existing resource. updateEmp() gets the name from the URL and finds the respective object.  It checks the request.json from the request for the new data & then it overwrites the existing. 

- DELETE method is used to delete the existing resource. deleteEmp() gets the name from the URL and deletes the respective object. 

- searchEmp() gets the emailid or phone number from the URL and retrieves the contact object with the given emailid or phone number.

- searchEmpAdd() gets the state or city from the URL and retrieves the contact records with the same city or state.

- app.run() starts the web server and ready to handle the request. The server is available in the URL http://localhost:5000/. You can access it via your browser, command line terminal or any API development tool.

- Used regular expression to match input date, phone number and email format correctly. 



# UNITTEST

- after starting the web server you can test the code using unittest. 

- just run $python -m unittest in the command line terminal and it will trigger unittest functions which will test the input date, phone or email format and status code of server response one by one. 



# SAMPLE DATASET

- If you don't want to create your database manually one by one than for testing purpose please add follwing sample JSON database below "app = Flask(__name__)" inside run.py file:



empDB: [
    {
      "address": {
        "city": "nyc",
        "state": "newyork",
        "street": "8801"
      },
      "birthdate": "09/19/2001",
      "company": "cts",
      "email": "111@gmail.com",
      "image": "1.png",
      "name": "vivek",
      "phone": {
        "personal": "1111111111",
        "work": "2222222222"
      }
    },
{
      "address": {
        "city": "chicago",
        "state": "illinois",
        "street": "1201"
      },
      "birthdate": "09/03/2002",
      "company": "wipro",
      "email": "222@gmail.com",
      "image": "2.png",
      "name": "sagar",
      "phone": {
        "personal": "3333333333",
        "work": "4444444444"
      }
    },
{
      "address": {
        "city": "atlanta",
        "state": "georgia",
        "street": "211"
      },
      "birthdate": "09/09/2000",
      "company": "tcs",
      "email": "333@gmail.com",
      "image": "3.png",
      "name": "sahu",
      "phone": {
        "personal": "5555555555",
        "work": "6666666666"
      }
    },
{
      "address": {
        "city": "atlanta",
        "state": "georgia",
        "street": "813"
      },
      "birthdate": "02/02/2002",
      "company": "cogni",
      "email": "444@gmail.com",
      "image": "4.png",
      "name": "saurabh",
      "phone": {
        "personal": "7777777777",
        "work": "8888888888"
      }
    },
{
      "address": {
        "city": "nyc",
        "state": "newyork",
        "street": "801"
      },
      "birthdate": "04/09/2001",
      "company": "apple",
      "email": "555@gmail.com",
      "image": "5.png",
      "name": "khetan",
      "phone": {
        "personal": "9999999999",
        "work": "1212121212"
      }
    },
    {
      "address": {
        "city": "chicago",
        "state": "illinois",
        "street": "2901"
      },
      "birthdate": "12/12/2002",
      "company": "google",
      "email": "666@gmail.com",
      "image": "6.png",
      "name": "neha",
      "phone": {
        "personal": "3232323232",
        "work": "4545454545"
      }
    }
  ]














