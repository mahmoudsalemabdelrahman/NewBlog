# create models(Post):
                        -author
                        -title
                        -description
                        -image
                        -active
                        -slug
                        -publish_at

# step 2:
        -admin.site.register(Post)
        -python manage.py makemigrations
        -python manage.py migrate