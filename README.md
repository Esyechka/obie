# obie

## Takehome API Challenge

Functionality included for retrieving all available states, all available carriers, all available policies, based on policy and state retrieve provider list (allow for null policy or state, if both missing retrieve all providers)

### Run Project
1. clone repo
2. activate environment by running `pipenv shell` (pipenv required)
3. in obie/ directory, same directory as manage.py run `./manage.py runserver` which will start the Django dev server. You can now try out the API urls. 

Endpoints available:
http://127.0.0.1:8000/states/ returns list of states
http://127.0.0.1:8000/policies/ returns list of policies
http://127.0.0.1:8000/carriers/ returns list of carriers
http://127.0.0.1:8000/offerings/?policy=policy_name&state=state_abreviation returns a list of companies who offer the policy for the specific state requested.


### Admin Portal
Use admin to view, edit model objects. Non-programmer friendly

1. from directory with manage.py file: python manage.py runserver
2. navigate to url: http://127.0.0.1:8000/admin/

admin (highly secure) name/password: admin/admin