# check if connection is made successfully from mongodb atlas

# from sensor.configuration.mongodb_connections import MongoDBClient
# from sensor.exception import SensorException
# import os, sys
# from sensor.logger import logging
# from sensor.pipeline import training_pipeline
# from sensor.pipeline.training_pipeline import TrainPipeline

# if __name__ == "__main__":
    
#     mongodb_client = MongoDBClient()
#     print(mongodb_client.database.list_collection_names())

#     training_pipeline = TrainPipeline()
#     training_pipeline.run_pipeline()

from sensor.configuration.mongodb_connections import MongoDBClient
from sensor.exception import SensorException
import os, sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
import os
from sensor.utils.main_utils import read_yaml_file

def set_env_variable(env_file_path):
    env_config = read_yaml_file(env_file_path)
    os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']

if __name__ == '__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)
