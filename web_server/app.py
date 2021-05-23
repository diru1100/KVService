from api import app

if __name__ == "__main__":

    # start the web server
    print("* Starting web service...")
    app.run(debug=True)
