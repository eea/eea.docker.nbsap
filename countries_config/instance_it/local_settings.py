DEBUG = True
TEMPLATE_DEBUG = DEBUG

ASSETS_ROOT = 'src/nbsap/static'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'it.tct.biodiversity.europa.eu']

# define your language preference
ugettext = lambda s: s
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
  ('en-us', ugettext('English')),
)

# Set to True if your application is EU dependent
EU_STRATEGY = True
# Allow adding new targets
EU_STRATEGY_ADD = False

# Set to False for EU intance
NAT_STRATEGY = True

# Template settings
SITE_HEADER = 'Reporting tool towards the AICHI targets, contribution by Italy'

# Set to True for information header
#INFO_HEADER = False

# Set to True to show layout footer logo
#LAYOUT_FOOTER_LOGO_VISIBLE = False

# Set to True to show layout header logo
#LAYOUT_HEADER_LOGO_VISIBLE = False

# Set the path to the image to be used as background
#HEADER_BACKGROUND_IMG = '/static/header.png'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_auth_ldap.backend.LDAPBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://ldap.eionet.europa.eu"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=Users,o=EIONET,l=Europe"

