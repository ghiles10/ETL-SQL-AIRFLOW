import sys 
sys.path.append('./extract_transform')
sys.path.append('./load')


from extract_transform.app import main
from load.load_csv import load_data_to_csv 



main() 
load_data_to_csv()