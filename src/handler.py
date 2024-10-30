
import runpod
from volume_folder_check import check_volume_folder_existence

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.


def handler(job):
    """ Handler function that will be used to process jobs. """


    job_input = job['input']
    output = {}
    volume_check = check_volume_folder_existence(job)
    if not volume_check[0]:
        return {"error": volume_check[-1]}
    else:
        output["return message"] = volume_check[-1]


    
    name = job_input.get('name', 'World')
    output["name"] = name

    

    return output


runpod.serverless.start({"handler": handler})
