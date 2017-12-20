This doc is the explainatory intro for this mini app,
of some of the choices I made and reasons behind.

##
I have 10 username/password pairs, the password is hashed inside database:

Abagnale/Aba4567890!
Bloomberg/Blo4567890!
Charlies/Cha7890lie!
DouglasK/Dou3456las7890!
elainnaW/Ela456ina7890!
FrancisU/Fra78s9nci0!
Gillbert/Gil4567890l!
Hindenburg/Hin456en7890!
Isabella/Bel45la67890@!
JohnSnoow/snO34567890!w

Used Djangorestframework for creating the Rest API.
The backend is hosting on http://hywang39.pythonanywhere.com/, it only has one home page,
with one button, to generate accounts for the users and save to the database. 
This backend serves for rest API.

Used djangorestframework related library for JWT processing in the backend, with some CORS library to enable cross origin api call

The database consists 3 tables, user, deposit_account and loan_account

The simple rest API is set in the app/url.py.

Front end uses Angular framework, most of the logics lies there.

############
From pythonanywhere.com: 
We are scheduling a systems upgrade on Thursday 21st December 2017 (2017-12-21) at 06:00 AM UTC. We expect approximately 20 min of downtime.
Try not to use the site during that time.

Angular site is hosted on https://sampleappangular.firebaseapp.com/

