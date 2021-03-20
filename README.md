# BUSINFOAPP
Instructions 
Download the BUSINFO Folder.
Navigate to the app folder. BUSINFOAPP/fla/App or BUSINFOAPP\fla\App
Start the application 
1)	Using the script for windows run        for linux/mac run 
2)	Alternatively use the following commands to manually run
 Linux/Max 
pip install -r requirements.txt
export FLASK_APP=app.py
flask run

Windows
pip install -r requirements.txt
set FLASK_APP=app.py
flask run

Using the browser navigate to : http://127.0.0.1:5000/index
See Bus Arrival Times 
A list of the 5 most recent Bus Arrivals times will be displayed. To refresh this list press the BUS Arrivals Button. 

 







For More information click on the bus information header.
 






List the history of Bus Arrival Times
To view a list of All the Bus Arrival API Call data sorted by Timestamp  Click the Time Stamped Arrivals Button. This will display a list of all the data retrieved from the API and the Time Stamp.


 

For more information click on the Time Stamp header
 

Clearing the Database
To Clear the Database, click the Clear Bus Arrival Database Button. All of the data in the database will be removed.

 
