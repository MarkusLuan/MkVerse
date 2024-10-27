# Sei que o ideal é usar o dot-venv e tal,
# Mas essa autenticação servirá apenas para
# Cadastrar novos usuários
BASIC_AUTH_USERNAME = 'api'
BASIC_AUTH_PASSWORD = 'dsnaj423nd'

SECRET_KEY = "#hcs51v^o!lwfa7h%wt*2elv4ew(@5k)r!t9e@f19#ecn%s$@k"
JWT_SECRET_KEY = SECRET_KEY

DATABASE =  {
    'ENGINE': 'postgresql',
    'NAME': 'mkverse_db',
    'USER': 'mkverse_db_user',
    'PASSWORD': 'Cnef[zx9CQ3PfH',
    'HOST': 'localhost',
    'PORT': '5432'
}