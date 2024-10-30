import os

def check_volume_folder_existence(config):
    """
    Check if a certain folder exists based on the configuration dictionary.

    Parameters:
    config (dict): A dictionary containing configuration information.

    Returns:
    tuple: A tuple where the first element is a boolean indicating success,
           and the second element is a message.
    """
    # Check if the necessary keys exist in the dictionary

    
    if 'folder_check' in config and isinstance(config['folder_check'], dict):
        folder_check = config['folder_check']

        # Get the check condition and the folder path
        should_check = folder_check.get('check', False)
        folder_path = folder_check.get('path', None)

        # If the folder check is enabled
        if should_check:
            if folder_path is None:
                return (False, "Error: No folder path provided to check.")

            # Check if the folder exists
            if not os.path.exists(folder_path):
                
                return (False, f"Error: The folder '{folder_path}' does not exist.")
            else:
                return (True, f"The folder '{folder_path}' exists.")
        else:
            return (True, "Folder check is disabled.")
    else:
        return (False, "Error: Invalid configuration. 'folder_check' key missing or not a dictionary.")

# Example usage
if __name__ == "__main__":
    config = {
        'folder_check': {
            'check': True,
            'path': '/path/to/your/folder'
        }
    }
    
    result = check_folder_existence(config)
    print(result)