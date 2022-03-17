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