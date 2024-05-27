import datetime

def add_folder_to_xml():
    current_data_file = 'C:/github/triggers/triggers.xml'

    now = datetime.datetime.now()
    backup_data_file = 'C:/github/triggers/backups/triggers-'+ str(now).replace(":", "-")[0:-7] + ".xml"

    original_data_file = 'C:/github/triggers/original/triggers.xml'

    with open(current_data_file, 'r') as file:
        filedata = file.read()

    #Make Backup
    with open(backup_data_file, 'w') as file:
        file.write(filedata)

    #Replace Current with Original
    with open(original_data_file, 'r') as file:
        filedata = file.read()

    with open(current_data_file, 'w') as file:
        file.write(filedata)

    #Add New Trigger Folder
    with open(current_data_file, 'r') as file:
        filedata = file.read()

    new_triggers = 'C:/github/triggers/new_triggers.xml'

    with open(new_triggers, 'r') as file:
        new_trigger_data = file.read()

    filedata = filedata.replace("      <!--replace-->", new_trigger_data)

    print(filedata)
    with open(current_data_file, 'w') as file:
        file.write(filedata)

add_folder_to_xml()