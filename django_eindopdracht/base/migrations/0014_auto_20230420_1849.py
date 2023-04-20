from django.db import migrations
from base.models import Book, User

def create_books(apps, schema_editor):
    Book = apps.get_model('base', 'Book')
    Book.objects.bulk_create([
        Book(
        Title = 'The Hobbit', 
        Description = 'The Hobbit is a childrens fantasy novel by English author J. R. R. Tolkien. It was published on 21 September 1937 to wide critical acclaim, being nominated for the Carnegie Medal and awarded a prize from the New York Herald Tribune for best juvenile fiction. The book remains popular and is recognized as a classic in childrens literature.', 
        Author = 'J. R. R. Tolkien', Genre = 'Fantasy', 
        NumberOfPages = 295, 
        Apporved = True),
        Book(
        Title = 'The Lord of the Rings',
        Description = 'The Lord of the Rings is an epic high fantasy novel written by English author and scholar J. R. R. Tolkien. The story began as a sequel to Tolkien\'s 1937 fantasy novel The Hobbit, but eventually developed into a much larger work. Written in stages between 1937 and 1949, The Lord of the Rings is one of the best-selling novels ever written, with over 150 million copies sold.',
        Author = 'J. R. R. Tolkien', 
        Genre = 'Fantasy',
        NumberOfPages = 1216,
        Apporved = True),
        Book(
        Title = 'The Chronicles of Narnia',
        Description = 'The Chronicles of Narnia is a series of seven fantasy novels by C. S. Lewis. It is considered a classic of children\'s literature and is the author\'s best-known work, having sold over 100 million copies in 47 languages. The books have been adapted for radio, television, the stage, and film, with the first series of films garnering over $1 billion in box office receipts.',
        Author = 'C. S. Lewis',
        Genre = 'Fantasy',
        NumberOfPages = 778,
        Apporved = True),
        Book(
        Title = 'The Hitchhiker\'s Guide to the Galaxy',
        Description = 'The Hitchhiker\'s Guide to the Galaxy is a comedy science fiction series created by Douglas Adams. Originally a radio comedy broadcast on BBC Radio 4 in 1978, it was later adapted to other formats, and over several years it gradually became an international multi-media phenomenon. The series follows the travails of Arthur Dent and his friend Ford Prefect after their world is destroyed to make way for a galactic freeway, as they travel through space aided by a galaxy-spanning computer named Deep Thought and his servant, the book The Hitchhiker\'s Guide to the Galaxy.',
        Author = 'Douglas Adams',
        Genre = 'Science Fiction',
        NumberOfPages = 224,
        Apporved = True),
        Book(
        Title = 'The Martian',
        Description = 'The Martian is a 2011 science fiction novel written by Andy Weir. It was his debut novel under his own name. It was originally self-published in 2011; Crown Publishing purchased the rights and re-released it in 2014. The story follows an American astronaut, Mark Watney, as he becomes stranded alone on Mars in the year 2035 and must improvise in order to survive.',
        Author = 'Andy Weir',
        Genre = 'Science Fiction',
        NumberOfPages = 384,
        Apporved = True),
        Book(
        Title = 'The Time Machine',
        Description = 'The Time Machine is a science fiction novella by H. G. Wells, published in 1895 and written as a frame narrative. The work is generally credited with the popularization of the concept of time travel by using a vehicle that allows an operator to travel purposefully and selectively. Wells\'s science fiction masterpiece has been adapted many times for stage, film, television, radio, and comic books.',
        Author = 'H. G. Wells',
        Genre = 'Science Fiction',
        NumberOfPages = 96,
        Apporved = True),
        Book(
        Title = 'The War of the Worlds',
        Description = 'The War of the Worlds is a science fiction novel by English author H. G. Wells. First serialised in 1897 by Pearson\'s Magazine in the UK and by Cosmopolitan magazine in the US, it was published as a novel the same year. The novel is about an invasion of late Victorian England by Martians using tripod fighting machines equipped with advanced weaponry and poisoned darts. Wells\'s use of the invasion plot, and the conflict between the tripod machines and the humans, has influenced an entire genre of science fiction stories.',
        Author = 'H. G. Wells',
        Genre = 'Science Fiction',
        NumberOfPages = 128,
        Apporved = True),
        Book(
        Title = 'The Picture of Dorian Gray',
        Description = 'The Picture of Dorian Gray is a philosophical novel by Oscar Wilde, first published complete in the July 1890 issue of Lippincott\'s Monthly Magazine. Fearing the story was indecent, the magazine did not print it until July 1891, by which time Wilde had resigned from his editorship. The work is a philosophical novel, possessing a profound interest in aesthetics, morality, and the nature of identity.',
        Author = 'Oscar Wilde',
        Genre = 'Philosophical',
        NumberOfPages = 256,
        Apporved = True),
    ])

def create_superuser(apps, schema_editor):
    superuser = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin',
    )
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_profile_email'),
    ]

    operations = [
        migrations.RunPython(create_books),
        migrations.RunPython(create_superuser),
    ]