from app import app
from forms import SearchForm
from flask import render_template
from ..models import video_model
from ..entidades import video


@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


@app.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    videos = video_model.Video.query
    if form.validate_on_submit():
        video.Video.search = form.searched.data
        videos = videos.filter(video_model.Video.titulo)

        return render_template('search.html', form=form, searched=video.Video.search,
                               videos=videos)

