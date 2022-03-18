
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
memory from 4GB to 16GB. T

After docker run command, the program takes quite a bit a time
to load, during the loading phase, if we submit a POST request
in terminal, the app will return the following:

"curl: (52) Empty reply from server".

This is normal. Please be patient, and wait until the app
finishes loading, then submit POST request the same way
we did when using the Flask API. 

Typing "docker stats" in terminal help use visualize the
containers running.