from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

SQL_DIR = PROJ_ROOT / "sql"

# Set up the database name
DATABASE = "ecommerce.db"

# SQL Queries used in the project
SQL_CUSTOMER_BUY_DATA = 'customer_buys_data.sql'

# Set up output file names
CUSTOMER_BUY_DATA = 'customer_data.csv'
CUSTOMER_BUY_DATA_TRANS = 'customer_data_trans.csv'

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)

except ModuleNotFoundError:
    pass


## below there is a mapping of dtypes for every column of each csv file
## data_mapping is a dictionary which its key = csv file and
## value = dict (dtype mapping, where key = column and value = dtype)
product_category_name_translation_map = {
    'product_category_name' : 'string',
    'product_category_name_english' : 'string'
}

olist_sellers_dataset_map = {
    'seller_id': 'string',
    'seller_zip_code_prefix': 'int64',
    'seller_city': 'string',
    'seller_state': 'string'
}

olist_geolocation_dataset_map = {
    'geolocation_zip_code_prefix': 'int64',
    'geolocation_lat': 'float64',
    'geolocation_lng': 'float64',
    'geolocation_city': 'string',
    'geolocation_state': 'string'
}

olist_products_dataset_map = {
    'product_id': 'string',
    'product_category_name': 'string',
    'product_name_lenght': 'float64',
    'product_description_lenght': 'float64',
    'product_photos_qty':  'float64',
    'product_weight_g': 'float64',
    'product_length_cm': 'float64',
    'product_height_cm': 'float64',
    'product_width_cm': 'float64'
}

olist_order_items_dataset_map = {
    'order_id': 'string',
    'order_item_id': 'int64',
    'product_id': 'string',
    'seller_id': 'string',
    'shipping_limit_date': 'object',
    'price': 'float64',
    'freight_value': 'float64'
}

olist_order_payments_dataset_map = {
    'order_id': 'string',
    'payment_sequential': 'int64',
    'payment_type': 'string',
    'payment_installments': 'int64',
    'payment_value': 'float64',
}

olist_orders_dataset_map = {
    'order_id': 'string',
    'customer_id': 'string',
    'order_status': 'string',
    'order_purchase_timestamp': 'object',
    'order_approved_at': 'object',
    'order_delivered_carrier_date': 'object',
    'order_delivered_customer_date': 'object',
    'order_estimated_delivery_date': 'object'
}

olist_order_reviews_dataset_map = {
    'review_id': 'string',
    'order_id': 'string',
    'review_score': 'int64',
    'review_comment_title': 'string',
    'review_comment_message': 'string',
    'review_creation_date': 'object',
    'review_answer_timestamp': 'object'
}

olist_customers_dataset_map = {
     'customer_id': 'string',
     'customer_unique_id': 'string',
     'customer_zip_code_prefix': 'int64',
     'customer_city': 'string',
     'customer_state': 'string'
}

data_mapping = {
    'product_category_name_translation': product_category_name_translation_map,
    'olist_sellers_dataset': olist_sellers_dataset_map,
    'olist_geolocation_dataset': olist_geolocation_dataset_map,
    'olist_products_dataset': olist_products_dataset_map,
    'olist_order_items_dataset': olist_order_items_dataset_map,
    'olist_order_payments_dataset': olist_order_payments_dataset_map,
    'olist_orders_dataset': olist_orders_dataset_map,
    'olist_order_reviews_dataset': olist_order_reviews_dataset_map,
    'olist_customers_dataset': olist_customers_dataset_map
}
