from news_curation import create_app

app = create_app()

if __name__ == "main":
    app.run(debug=True)