install_requirements:
	pip install requirements.txt

run_streamlit:
	streamlit run app.py

heroku_login:
	heroku login

heroku_create_app:
	heroku create taxiwebapp-sgk --region eu

deploy_heroku:
	git push heroku master
	heroku ps:scale web=1

git_push:
	git add .
	git commit -m "Ready for deployment"
	git push origin master
