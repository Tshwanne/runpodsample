import os



def check_volume_folder_existence(config):
    """
    Check if a certain folder exists based on the configuration dictionary.
    If the folder exists, list all files in the directory if list volume files is present and True in the configuration.

    Parameters:
    config (dict): A dictionary containing configuration information.

    Returns:
    tuple: A tuple where the first element is a boolean indicating success,
           the second element is a message, and the third element is a list of files.
    """
    # Check if the necessary keys exist in the dictionary
    if 'folder_check' in config and isinstance(config['folder_check'], dict):
        folder_check = config['folder_check']

        # Get the folder path
        folder_path = folder_check.get('path', None)

        # If the folder path is provided
        if folder_path is not None:
            # Check if the folder exists
            if not os.path.exists(folder_path):
                return (False, f"Error: The folder '{folder_path}' does not exist.")
            else:
                
                list_files = folder_check.get('list volume files', None)
                if not list_files:
                    return (True, f"The folder '{folder_path}' exists.")
                # The folder exists, now list all files in the directory
                else:
                    try:
                        files = os.listdir(folder_path)
                        return (True, f"The folder '{folder_path}' exists. Files in the directory: {files}")
                    except PermissionError:
                        return (False, f"Error: Permission denied to access the folder '{folder_path}'.")
        else:
            return (False, "Error: No folder path provided to check.")
    else:
        return (False, "Error: Invalid configuration. 'folder_check' key missing or not a dictionary.")

# Example usage
if __name__ == "__main__":
    config = {
        'folder_check': {
            'path': 'C:\\Users\\pinkie\\Documents\\GitHub\\runpodsample-main\\src\\folder',
            'list volume files': False
        }
    }
    
    result = check_folder_existence(config)
    print(result)