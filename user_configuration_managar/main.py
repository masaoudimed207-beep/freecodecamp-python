test_settings = {
    "theme": "dark",
}
def add_setting(setting,setting_tuple):
    (key,value)=setting_tuple
    key=key.lower()
    value=value.lower()
    if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(setting,setting_tuple):
    (key,value)=setting_tuple
    key=key.lower()
    value=value.lower()
    if key in setting:
        setting[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting,key):
    key=key.lower()
    if key in setting:
        del setting[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(setting):
    if not setting:
        return "No settings available."
    else:
        settings_liste="".join([f"{key.capitalize()}: {value}\n" for key, value in setting.items()])
        return f"Current User settings:\n{settings_liste}"  
