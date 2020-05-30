from utils import setupLogger
from mlspeclib import MLObject
import yaml as YAML

# Making this a class in case we want sub functions.
class StepExecution:
    input_params = {}  # noqa
    execution_params = {}  # noqa
    ml_object = MLObject()  # noqa
    logger = None  # noqa

    def __init__(self, input_params, execution_params):
        self.input_params = input_params
        self.execution_params = execution_params
        self.rootLogger = setupLogger().get_root_logger()

        # Execute all work in here.

        # Output input params & execution params
        if self.input_params is not None:
            self.rootLogger.debug(f"Input params: {self.input_params}")

        if self.execution_params is not None:
            self.rootLogger.debug(f"Execution params: {self.execution_params}")

    def execute(self, result_object_schema_type, result_object_schema_version):
        # Create Result object
        results_object = MLObject()
        results_object.set_type(
            schema_type=result_object_schema_type,
            schema_version=result_object_schema_version,
        )

        # Mocked up results
        return_dict = YAML.safe_load(
            """
servable: True
package_size: 1029310298
tested_platforms: ['kubeflow', 'azureml', 'sagemaker']
model_source:
    servable_model:
        data_store: 's3'
        bucket: 'nlp-bucket'
        path: 'a231653454ca8e07f42adc7941aeec6b'
serving_container_image:
    container_image_url: 'https://hub.docker.com/repository/docker/contoso/nlp-base-images'
"""
        )

        results_object.servable = return_dict["servable"]
        results_object.tested_platforms = return_dict["tested_platforms"]
        results_object.package_size = return_dict["package_size"]
        results_object.model_source.servable_model.data_store = return_dict[
            "model_source"
        ]["servable_model"]["data_store"]
        results_object.model_source.servable_model.bucket = return_dict["model_source"][
            "servable_model"
        ]["bucket"]
        results_object.model_source.servable_model.path = return_dict["model_source"][
            "servable_model"
        ]["path"]
        results_object.serving_container_image.container_image_url = return_dict[
            "serving_container_image"
        ]["container_image_url"]

        return results_object
