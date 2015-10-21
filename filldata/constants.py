
#QUERIES
#QUERY_GET_HOT_DEALS = 'SELECT gdo.offer_id, gdo.offer_title, gdo.property_id, DATE_FORMAT(gdo.offer_end_time, \"%Y/%m/%d %H:%m\") as offer_end_time, gdo.required_total_users, gdo.enrolled_no_of_users, gdo.market_psft_price, gdo.offer_discount, gdo.status, am.name, am.area, am.city FROM group_deal_offers gdo, apartment_main am  where gdo.is_hot=1 and gdo.status=\'Alive\' and gdo.property_id=am.property_id'
QUERY_GET_HOT_DEALS = 'SELECT gdo.offer_id, gdo.offer_title, gdo.property_id, DATE_FORMAT(gdo.offer_end_time, \"%Y/%m/%d %H:%m\") as offer_end_time, gdo.required_total_users, gdo.enrolled_no_of_users, gdo.market_psft_price, gdo.offer_discount, gdo.status FROM group_deal_offers gdo where gdo.is_hot=1 and gdo.status=\'Alive\''

#QUERY_GET_DEAL_DETAIL = 'SELECT gdo.offer_id, gdo.offer_title, gdo.property_id, DATE_FORMAT(gdo.offer_end_time, \"%Y/%m/%d %H:%m\") as offer_end_time, gdo.required_total_users, gdo.enrolled_no_of_users, gdo.market_psft_price, gdo.offer_discount, gdo.status, gdo.deal_fine_print, gdo.main_highlights, am.name, am.area, am.city FROM group_deal_offers gdo, apartment_main am  where gdo.is_hot=1 and gdo.status=\'Alive\' and gdo.property_id=am.property_id and gdo.offer_id='
QUERY_GET_DEAL_DETAIL = 'SELECT gdo.offer_id, gdo.offer_title, gdo.property_id, DATE_FORMAT(gdo.offer_end_time, \"%Y/%m/%d %H:%m\") as offer_end_time, gdo.required_total_users, gdo.enrolled_no_of_users, gdo.market_psft_price, gdo.offer_discount, gdo.status, gdo.deal_fine_print, gdo.main_highlights FROM group_deal_offers gdo  where gdo.is_hot=1 and gdo.status=\'Alive\' and gdo.offer_id='

QUERY_GET_USERS = 'SELECT * from group_deal_users'

QUERY_GET_CUSTOMERS = "Select gdbc.customer_name, gdbc.customer_email, gdbc.customer_phone, concat( gdb.first_name, ' ',  gdb.last_name) as broker_name, gdb.company_name as broker_company, gdb.pan_card_number from group_deal_broker_customers gdbc, group_deal_users gdb where gdbc.broker_id=gdb.user_id and gdbc.offer_id="


GET_PROPERTY_API_URL = 'http://www.commonfloor.com/api/project-v2/full-details?property_id='
GET_CITIES_API_URL = 'http://www.commonfloor.com/api/geo-local-v2/get-cities'
GET_PROPERTIES_BY_CITY_API_URL = 'http://www.commonfloor.com/api/project-v2/get-projects?city='
GET_AREA_BY_CITY_API_URL = 'http://www.commonfloor.com/autosuggest.php?item=area&c='
GET_PROPERTIES_BY_AREA_API_URL = 'http://www.commonfloor.com/api/project-v2/get-projects?page_size=200&project_location_filter[]=null_area_'

api_key = 'nk8qh4vtri7l3hwotbsdtv2zl3p5u168'

PAYMENT_DEAL_UDF = '0'
PAYMENT_BUYERS_UDF = '1'
PAYMENT_DEAL_BUYERS_UDF = '2'
PAYMENT_NOT_KNOWN_UDF = '-1'

CUSTOMER_ADDITION_COST = 499
DEAL_REGISTRATION_FEES = 14999
CUSTOMER_ADDITION_REST_COST = 4500
MAX_NUMBER_OF_FREE_CUSTOMERS=10