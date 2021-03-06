import os

CHECK_INTERVAL = 3600 # dload feed once per hour

### You sholdn't need to edit below here ###

base_dir = os.path.dirname(os.path.abspath( __file__ ))
data_dir = os.path.join(base_dir, "data")
BASE_HREF_FILE = os.path.join(data_dir, 'base_href')

# TODO: improve error handling for local file setup.
if os.path.exists(BASE_HREF_FILE):
    with open (BASE_HREF_FILE, 'r') as FILE:
        BASE_HREF = FILE.readline().strip()
    if not BASE_HREF.endswith('/'):
        BASE_HREF += '/'
else:
    BASE_HREF = "/"

CACHE_FILE = os.path.join(data_dir, "cache.db")
PLANETS_FILE = os.path.join(data_dir, "planets.db")
OUTPUT_DIR = os.path.join(base_dir, "www")
TEMPLATE_DIR = os.path.join(base_dir, "templates")
VERSION = "2.1.0"
DATA_FORMAT_VERSION = "0.1.0"
MAX_ENTRIES = 100
FEED_TIMEOUT = 100

# calculate value of domain here
# be nice. handle errors

opt={'website_name':"Planeteria",
     'title':"Planeteria",
     'generator':"Planeteria %s" % VERSION,
     'generator_uri':"http://planeteria.org/copyright.html",
     'force_check': False,
     'template_dir':TEMPLATE_DIR,
     'new_planet_dir':os.path.join(TEMPLATE_DIR, "new_planet"),
     'base_dir':base_dir,
     'log_dir':os.path.join(base_dir, "log"),
     'base_href':BASE_HREF,
# Set domain to the precomputed value
     'domain':BASE_HREF.split("//")[1],
     'data_dir':data_dir,
     'output_dir':OUTPUT_DIR,
     'template_dir':TEMPLATE_DIR,
     'check_interval':CHECK_INTERVAL,
     'version':VERSION,
     'data_format_version':DATA_FORMAT_VERSION,
     'check_interval':CHECK_INTERVAL,
     'max_entries':MAX_ENTRIES,
     }

#opt.update(locals())

import logging
logger = logging.getLogger('planeteria')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(opt['log_dir'], 'planeteria.log'), encoding = "UTF-8")
fh.setLevel(logging.DEBUG)
fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fh_formatter)
logger.addHandler(fh)


# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch_formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(ch_formatter)
logger.addHandler(ch)

