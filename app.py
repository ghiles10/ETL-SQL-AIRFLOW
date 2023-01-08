import sys 
sys.path.append('./extract_transform')
sys.path.append('./load')


from extract_transform.app import extract_and_transform
from load.load_csv import load_data_to_csv 



extract_and_transform() 
load_data_to_csv()