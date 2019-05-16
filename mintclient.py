from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

configuration = mint_client.Configuration()

api_instance = mint_client.UserApi()

username = 'tuka_tuka'  # str | The user name for login
password = 'password'  # str | The password for login in clear text
# user = mint_client.User(username=username, password=password) # User | Created user object
#
# try:
#    # Create user
#    api_instance.create_user(user)
# except ApiException as e:
#    print("Exception when calling UserApi->create_user: %s\n" % e)

try:
    # Logs user into the system
    configuration.access_token = api_instance.login_user(username, password)
    print("Log in success! Token: %s\n" % configuration.access_token)
except ApiException as e:
    print("Exception when calling UserApi->login_user: %s\n" % e)

# create model
api_instance = mint_client.ModelApi(mint_client.ApiClient(configuration))
# create an instance of the API class
model = {
    "description": "SSCYP is built upon deep learning of past harvest data and satellite images of a certain area, it is able to predict the yield of a given crop in a given region based on its current satellite images of at least 6 days of time span. The current model is trained for South Sudan and pre-trained on Ethiopia, the prediction can be of the same region, or it can be of neighboring countries or regions with similar underlying distributions.",
    "hasDocumentation": [
        "https://cloud.docker.com/repository/docker/minyinsri/crop-yield-transfer-learning-cpu"
    ],
    "hasModelCategory": [
        "Agriculture"
    ],
    "hasSoftwareVersion": [
        {
            "id": "SSCYP_1.0"
        }
    ],
    "id": "SSCYP",
    "label": "DSSCYP",
    "type": [
        "https://w3id.org/mint/modelCatalog#Model",
        "https://w3id.org/mint/modelCatalog#TheoryBasedModel"
    ]
}

# Create a model if the it is not already cre
model_id = "SSCYP"
try:
    api_response = api_instance.create_model(model)
except ApiException as e:
    print("Exception: %s\n" % e)

# Get the model
try:
    # Get a Model
    api_response = api_instance.get_model(model_id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->get_model: %s\n" % e)

# Create a model version
model_version = {
    "hasConfiguration": [
        {
            "id": "sscyp_historgram_output"
        }
    ],
    "hasVersionId": "1.0",
    "id": "SSCYP_1.0",
    "label": "SSCYP v1.0",
    "type": [
        "http://ontosoft.org/software#SoftwareVersion"
    ]
}

# Create a ModelVersion if it's not already exist
api_instance = mint_client.ModelversionApi(
    mint_client.ApiClient(configuration))
try:
    api_instance.create_model_version(model_version)
    pprint("Created")
except ApiException as e:
    print("Exception: %s\n" % e)

model_version_id = "SSCYP_1.0"

# Get the Model Version
try:
    # Get a ModelVersion
    api_response = api_instance.get_model_version(
        model_version_id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelversionApi->get_model_version: %s\n" % e)

# Create model configuration make histograms
model_configuration = {
    "description": "The model works on the histograms of pixel intensities rather than pixels itself. The configuration creates histograms based on time series satellite images.",
    "hasContainer": [
        {
            "id": "https://cloud.docker.com/repository/docker/minyinsri/crop-yield-transfer-learning-cpu"
        }
    ],
    "hasImplementationScriptLocation": "https://github.com/min-yin-sri/deep-transfer-learning-crop-prediction/blob/master/code/histograms.sh",
    "hasInput": [
        {
            "id": "sscyp_satellite_image_directory"
        },
        {
            "id": "sscyp_cover_image_directory"
        },
        {
            "id": "sscyp_temperature_image_directory"
        },
        {
            "id": "sscyp_output_histogram_directory"
        }
    ],
    "hasOutput": [
        {
            "id": "sscyp_historgram_output"
        }
    ],
    "id": "sscyp_generate_histogram",
    "label": "Generate histograms for SSCYP"
}
api_instance = mint_client.ModelconfigurationApi(
    mint_client.ApiClient(configuration))

# Create a model configuration if it's not already exist
try:
    api_instance.create_model_configuration(model_configuration)
except ApiException as e:
    print("Exception: %s\n" % e)

model_config_id = "sscyp_generate_histogram"
try:
    # Get modelconfiguration
    api_response = api_instance.get_model_configuraton(
        model_config_id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->get_model_configuraton: %s\n" % e)
