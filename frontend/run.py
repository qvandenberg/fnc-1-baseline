import flask
from flask import render_template, url_for, request, flash, redirect
from utils.form import urlForm, formData


APP = flask.Flask(__name__)
articleInfo = formData()


@APP.route('/', methods=['GET', 'POST'])
def route():
        form = urlForm()
        if form.validate_on_submit():
                flash('URL requested {}'.format(
                form.url.data))
                articleInfo.set_url(form.url.data)
                return render_template('/processed.html', link=form.url.data)
        return render_template('index.html', title='Submit article', form=form)

@APP.route('/processed', methods=['GET', 'POST'])
def processed(link = "www.google.co.uk"):
        articleInfo.set_header("Sample header")
        articleInfo.set_header("Sample body")

     
        return render_template('processed.html', articleInfo.url, articleInfo.header, articleInfo.body)
 


if __name__ == '__main__':
        APP.secret_key = 'secret key'
        APP.config['SESSION_TYPE'] = 'filesystem'
        APP.run(debug=False,port=5000)