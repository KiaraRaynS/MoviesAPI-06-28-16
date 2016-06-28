# hold
def define_rater_data(apps, schema_edditor):
    import csv
    Rater = apps.get_model('appmoviesapi', 'Rater')
    with open('u.user', encoding='latin1') as csvfile:
        fieldname = ['id', 'age', 'gender', 'occupation', 'zip']
        userdata = csv.DictReader(csvfile, fieldnames=fieldname, delimiter='|')
        for row in userdata:
            Rater.objects.create(id=row['id'], age=row['age'], gender=row['gender'], occupation=row['occupation'], zip_code=row['zip'])


def define_movie_data(apps, schema_edditor):
    import csv
    Movie = apps.get_model('appmoviesapi', 'Movie')
    with open('u.item', encoding='latin1') as csvfile:
        fieldnames = [
                'id', 'title', 'release', 'video',
                'imdb', 'unknown', 'action', 'adventure',
                'animation', 'childrens', 'comedy', 'crime',
                'doc', 'drama', 'fant', 'film',
                'horror', 'music', 'myst', 'rom',
                'scifi', 'thril', 'war', 'west'
                ]
        moviedata = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter='|')
        for row in moviedata:
            Movie.objects.create(id=row['id'], title=row['title'], release_date=row['release'], video_release=row['video'],
                                 imdb=row['imdb'], unknown=row['unknown'], action=row['action'],
                                 adventure=row['adventure'], animation=row['animation'], childrens=row['childrens'],
                                 comedy=row['comedy'], crime=row['crime'], documentary=row['doc'], drama=row['drama'], fantasy=row['fant'],
                                 film_noir=row['film'], horror=row['horror'], music=row['music'], mystery=row['myst'],
                                 romance=row['rom'], scifi=row['scifi'], thriller=row['thril'], war=row['war'],
                                 western=row['west'])


def assign_movie_ratings(apps, schema_editor):
    import csv
    Rater = apps.get_model('appmoviesapi', 'Rater')
    Movie = apps.get_model('appmoviesapi', 'Movie')
    MovieRating = apps.get_model('appmoviesapi', 'MovieRating')
    with open('u.data', encoding='latin1') as csvfile:
        fieldnames = ['rid', 'mid', 'rating', 'time']
        movieratingdata = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter='\t')
        for row in movieratingdata:
            rater_id = Rater.objects.get(id=row['rid'])
            movie_id = Movie.objects.get(id=row['mid'])
            MovieRating.objects.create(rating=row['rating'], timestamp=row['time'],
                                       movie=movie_id, rater=rater_id)


class Migration(migrations.Migration):

    dependencies = [
        ('appmoviesapi', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(define_rater_data),
            migrations.RunPython(define_movie_data),
            migrations.RunPython(assign_movie_ratings),
    ]