

# Core Settings ########################################################
CORE_NAME = 'YoutubeCrawler'
CORE_ID = 'youtube_crawler'
CORE_PORT = 7085
########################################################################

# YT API INFO ##########################################################
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyD9O5FIwU3V1teLw0UcssN8TxL7Zl15erA"
DEVELOPER_KEY2 = "AIzaSyAV1WWrct68Fj4fIoGrb89nY5RwdUgU0Ak"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
########################################################################

# Jobs #################################################################
period_days = 120
period_years = 1
max_page_crawl = 100000
retry_update_count = 15
########################################################################

# Debug mode ###########################################################
DEBUG = True
########################################################################

# Threading ############################################################
background_process_thread_pool = 120
main_min_thread = 30
main_max_thread = 80
########################################################################

# Server Port Address ##################################################
# CORE_HOST_MAIN = 'localhost'
# CORE_PORT_MAIN = 7080
CORE_HOST_SELF = 'localhost'
CORE_PORT_SELF = 7085
########################################################################

# MongoDB Configuration ################################################
MONGO_HOST_LOCAL = 'localhost'
MONGO_PORT_LOCAL = 27017
BALANCING = False
MONGO_HOST_GLOBAL = 'localhost'
MONGO_PORT_GLOBAL = 27017
MONGO_HOST_SELF = 'localhost'
MONGO_PORT_SELF = 27017
########################################################################

# Extra Data ###########################################################
keyword_list = [
    'music',
    'video clip',
    'love song',
    'song',
    'gitar',
    'singer'
]
########################################################################

# Logging ##############################################################
log_dir = '/var/log/core/{0}/'.format(CORE_ID)
path_error = '/var/log/core/{0}/error.log'.format(CORE_ID)
path_object = '/var/log/core/{0}/object.log'.format(CORE_ID)
path_service = '/var/log/core/{0}/service.log'.format(CORE_ID)
path_db = '/var/log/core/{0}/db.log'.format(CORE_ID)
path_debug = '/var/log/core/{0}/debug.log'.format(CORE_ID)
path_jobs = '/var/log/core/{0}/jobs.log'.format(CORE_ID)
path_request = '/var/log/core/{0}/request.log'.format(CORE_ID)
path_apscheduler = '/var/log/core/{0}/apscheduler.log'.format(CORE_ID)
max_bytes = 1000000
backup_count = 10
########################################################################
