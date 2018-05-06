import flask
from flask import render_template, url_for, request, flash, redirect
from utils.form import urlForm, formData
from utils.scrape import extractArticle


APP = flask.Flask(__name__)
articleInfo = formData()

@APP.route('/', methods=['GET', 'POST'])
def route():
        form = urlForm()
        if form.validate_on_submit():
                articleInfo.set_url(form.url.data)
                # implement in utils.scrape.extractArticle with goose or beautifulsoup
                downloadArticle = extractArticle(articleInfo.url)
                downloadArticle.article_contents()
                articleInfo.set_header(downloadArticle.header)
                articleInfo.set_body(downloadArticle.body)
                # analyse stance

                return render_template('/processed.html', article=articleInfo)
        return render_template('index.html', title='Submit article', form=form)





@APP.route('/processed', methods=['GET', 'POST'])
def processed(article=None):
        if request.method == "POST":
                return render_template('processed.html', article=article)
 
if __name__ == '__main__':
        APP.secret_key = 'secret key'
        APP.config['SESSION_TYPE'] = 'filesystem'
        # APP.run(debug=True,port=5000)
        APP.run()