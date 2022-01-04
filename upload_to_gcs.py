
#########################Import the Libraries############################################################################# 
##########################################################################################################################
from flask import Flask, json, redirect ,url_for, render_template ,request,jsonify , make_response
from google.cloud import storage
from datetime import date
import os
#########################Flask Constructor which takes te name of the current module as argument##########################
##########################################################################################################################
app = Flask(__name__)

#########################It is used to set the endpoint of the application ###############################################
##########################################################################################################################
@app.route('/upload',methods=["POST"])

#########################Function of the Application used to upload the file and also function contains exception handling
##########################################################################################################################
def upload():
    try:
        request_data = request.form['jeet']
        file = request.files.get('file', '')
        print(file)
        data=json.loads(request_data)
        
    except ValueError as e:
        return "Json is having some error"

#########################Location were the file will store ###############################################################
##########################################################################################################################
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'rb-munish-playground456-********.json'


    
    todays_date = date.today()
    x=todays_date.month

#########################Creating the list of the months #################################################################
##########################################################################################################################
    month=["Not a valid month","january","february","march","april","may","june","juily","august","september","october","november","december"]

#########################Automatic setting of the json key in system environment ######################################### 
##########################################################################################################################
    storage_client = storage.Client()

#########################Selecting the bucket name in which the file will be store ####################################### 
##########################################################################################################################
    bucket = storage_client.get_bucket('jeet456_pio')
    
    if month==0:
        filename=0

#########################Setting the specific location to store the file in the gcp bucket ############################### 
##########################################################################################################################
    else:
        print(data)
        filename="%s/%s/%s/%s" % (data['orgId'],data['year'],month[x],"file-sales")
        blob = bucket.blob(filename)

#########################Selecting the location where the file is stored ################################################# 
##########################################################################################################################
        blob.upload_from_filename('D:/Python/Flask/Project/Project 9/pic.jpg')
    return "file upload" 

#########################It is used to execute the code when the user run the scripts directly  #############################
#############################################################################################################################
if __name__ == "__main__":
    app.run(debug=True)