import environs

env = environs.Env()
env.read_env("./.env")

TOKEN_1 = env.str('TOKEN_1')
API_HASH_1 = env.str('API_HASH_1')
API_ID_1 = env.int('API_ID_1')
ADMIN_CHATID_1 = env.int('ADMIN_CHATID_1')
ADMIN_USERNAME_1 = env.str('ADMIN_USERNAME_1')

TOKEN_2 = env.str('TOKEN_2')
API_HASH_2 = env.str('API_HASH_2')
API_ID_2 = env.int('API_ID_2')
ADMIN_CHATID_2 = env.int('ADMIN_CHATID_2')
ADMIN_USERNAME_2 = env.str('ADMIN_USERNAME_2')

channel_id = env.int('CHANNEL_ID')
db_name = env.str('DB_NAME')
modules_repo_branch = env.str('MODULES_REPO_BRANCH', 'master')
