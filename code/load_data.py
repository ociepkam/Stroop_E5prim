import codecs
import yaml
import os
from psychopy.gui import Dlg
import platform


def load_config():
    try:
        with open(os.path.join("config.yaml")) as yaml_file:
            doc = yaml.safe_load(yaml_file)
        return doc
    except:
        raise Exception("Can't load config file")


def read_text_from_file(file_name, insert=''):
    """
    Method that read message from text file, and optionally add some
    dynamically generated info.
    :param file_name: Name of file to read
    :param insert: dynamically generated info
    :return: message
    """
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    msg = list()
    with codecs.open(file_name, encoding='utf-8', mode='r') as data_file:
        for line in data_file:
            if not line.startswith('#'):  # if not commented line
                if line.startswith('<--insert-->'):
                    if insert:
                        msg.append(insert)
                else:
                    msg.append(line)
    return ''.join(msg)


def check_if_font_exist(file_name):
    if platform.system() == 'Windows':
        if file_name in os.listdir(os.path.join("C:/", "Windows", "fonts")) or \
           file_name in os.listdir(os.path.join("C:/", "Users", os.getlogin(), "AppData", "Local", "Microsoft", "Windows", "Fonts")):
            return True
        else:
            myDlg = Dlg(title="No font file", labelButtonOK='Run procedure', labelButtonCancel='Exit')
            myDlg.addText(f"Font file {file_name} doesn't exist in fonts folder! Procedure will use default font instead!")
            myDlg.show()
            if myDlg.OK:
                return False
            else:
                print('user cancelled')
                exit(1)
    else:
        myDlg = Dlg(title="Font file", labelButtonOK='Run procedure', labelButtonCancel='Exit')
        myDlg.addText(f"Procedure can't veryfi if font {file_name} does exist on your computer.")
        myDlg.show()
        if myDlg.OK:
            return False
        else:
            print('user cancelled')
            exit(1)
