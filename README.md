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
