from lib import ConfigReader

def get_customers_schema():
    return "customer_id int, customer_fname string, customer_lname string, username string, password string, address string, city string, state string, pincode string"

def read_customers(spark, env):
    conf = ConfigReader.get_app_config(env)
    customers_file_path = conf["customers.file.path"]
    return spark.read.format("csv").option("header", "true").schema(get_customers_schema()).load(customers_file_path)