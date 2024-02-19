# ElasticKibanaLab
The ElasticKibanaLab is for experimenting with ElasticSearch and Kibana utilizing containers to host both services

# Note
The parent directory for the project should not contain any spaces for the batch scripts to work as expected.

# Set Up

## ElasticSearch and Kibana
* Be sure Docker Desktop is currently running
* Run the Docker/launch.bat script to deploy ElasticSearch and Kibana as container services

## Python and Jupyter
* Run the UtilityScripts/Python Virtual Environment Initialization.bat script to set up the Python virtual environment
* Run the UtilityScripts/Python Packages Load Quick Reqs.bat script to load all Python packages from quick_reqs.txt into the Python virtual environment
* Run the UtilityScripts/Python Jupyter Initialization.bat script to add the Python virtual environment to Jupyter

# Kibana
* Kibana can be accessed at localhost:5601
    * The username and password is elastic

# Jupyter
* Run the jupyter/Python Jupyter Start.bat script to launch the Jupyter UI
