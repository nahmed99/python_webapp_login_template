from website import create_app

app = create_app()

if __name__ == '__main__':
   app.run(debug=True) # 'debug=True' for DEVELOPMENT only - to run the flask web server. Turn this off when running in production.
