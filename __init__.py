version = '0.0.100'
chrome_version = '81'

project_directory = './'

chrome_driver_location = project_directory + 'chromedriver/'+ chrome_version +'/chromedriver'

webscrapping_directory =  project_directory + 'webscrapping/'
download_directory = project_directory + 'data/'

ip_address_and_port_no = '127.0.0.1'
db_name = 'jobDB'
col_name = 'webscrappingdata'

spark_mongo_server_connection_string = 'mongodb://' + ip_address_and_port_no + '/' + db_name + '.' + col_name

PreProcessing_Done = False
Machine_Learning_Done = False
GUI_Done = False

Libraries_Required = [
    'threaded',
    'selenium',
    'scikit-learn'
]