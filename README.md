# -DVC-Airflow-in-MLOp-s
 DVC &amp; Airflow in MLOp's

More about the git-ignore and reason and explination.

Data management

Data versions

Hiding a Data

# Go back to the previous version of the data:

git log  [take id first 6-dig]

git checkout 900b03

dvc checkout   [get the data [previous version]

# Store in remote [E.g. S3,..]

dvc remote add -d <remote_storage_name> MLOPs\<Airflow-in-MLOp-s-1>

(base) PS F:\AI Egineer> dvc checkout   
Building workspace index                    |2.00 [00:00,  112entry/s]
Comparing indexes                          |3.00 [00:00, 1.11kentry/s]
Applying changes                            |1.00 [00:00,   286file/s]
M       data\data.csv

(base) PS F:\AI Egineer> dvc remote add -d remote_storage MLOPs\-DVC-Airflow-in-MLOp-s-1              
Setting 'remote_storage' as a default remote.

(base) PS F:\AI Egineer> dvc push
Collecting                                  |1.00 [00:00,  240entry/s]
Pushing
1 file pushed


