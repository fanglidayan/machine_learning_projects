
Please read the following article for a comprehensive guide.

https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf

===============================================================

To get prediction for user number 7 (this is not user id but 
the corresponding vocabulary number for some user id) please
type the following code in mac terminal.

curl -X POST \
   0.0.0.0:80/predict \
   -H 'Content-Type: application/json' \
   -d ‘7’

===============================================================

Some files are too large to be uploaded to GitHub. For a
complete list of files please see "complete_list_of_files.png"

===============================================================

When containerizing with Docker, don't forget to tune up the 
memory from 4GB to 16GB. 

After docker run command, the program takes quite a bit a time
to load, during the loading phase, if we submit a POST request
in terminal, the app will return the following:

"curl: (52) Empty reply from server".

This is normal. Please be patient, and wait until the app
finishes loading, then submit POST request the same way
we did when using the Flask API. 

Typing "docker stats" in terminal help use visualize the
containers running.

===============================================================

use the bash command below to log in to the ec2 instance:

ssh -i ~/path/my-key-pair.pem ec2-user@ec2-54-196-243-93.compute-1.amazonaws.com

===============================================================

use the bash command below to copy some files to the ec2 instance:

scp -i /path/my-key-pair.pem -r ~/desktop/folder_to_be_copied ec2-user@ec2-54-196-243-93.compute-1.amazonaws.com:/home/ec2-user

===============================================================

use the following curl post request to make a prediction ('1231' is a user vocabulary number)

curl -X POST \
http://ec2-54-196-243-93.compute-1.amazonaws.com:80/predict \
-H 'Content-Type: application/json' \
-d '1231'

===============================================================

Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

solution: sudo systemctl start docker


