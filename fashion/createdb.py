"""
Creates a fresh db with data that contains fashion board items
"""

from fashion.defaults import FASHION_DATABASE


def create_default_fashion_items():
    """
    Default fashion items
    :return: List of default fashion items
    """
    return [
        # Populates a good fashion item
        ("Hat",
         "It's a hat dude. What more do you want",
         "Hat Man",
         "pikachu.png",
         "http://HatsOwnYou.com"),
        # Populates a fashion item entry with a non-existing picture
        ("Glove",
         "It keeps your hands warm and looks pretty. What else do you want?",
         "Glove Girl",
         "non-existent.png",
         "http://GlovesForGirls.com"),
        # Populates a fashion item entry with more than 32 words in the blurb
        ("Scarf",
         "Scarves are super warm. You will want to always have a scarf on you. "
         "If you don't have a scarf, you should buy one now. PLEASE BUY ONE NOW! "
         "IF YOU DON'T, I will be very sad.",
         "Scarf Stranger",
         "pikachu.png",
         "http://www.StrangeScarves.com")
    ]


#
def create_accessories(count):
    """
    Creates a large number of generic fashion accessories
    :param count: Number of accessories to create
    :return: list of accessories
    """
    return [("Awesome Accessory {}".format(i+1),
             "Random blurb that no one reads! This is going to be the same",
             "Fake Author #{}".format(i+1),
             "pikachu.png",
             "http://www.youtube.com")
            for i in xrange(count)]


def main():
    try:
        con = sqlite3.connect(FASHION_DATABASE)
        with con:
            cur = con.cursor()

            # Drops table if it already exists
            cur.execute("DROP TABLE IF EXISTS FashionItem")
            # Creates Table
            cur.execute("CREATE TABLE FashionItem("
                        "id INTEGER primary key autoincrement,"
                        "title TEXT,"
                        "blurb TEXT,"
                        "author TEXT,"
                        "thumbnail_url TEXT,"
                        "details_url TEXT)")
            # Populates table with data
            cur.executemany("INSERT INTO FashionItem(title, blurb, author, thumbnail_url, details_url)"
                            "VALUES(?, ?, ?, ?, ?)", create_default_fashion_items())
            cur.executemany("INSERT INTO FashionItem(title, blurb, author, thumbnail_url, details_url)"
                            "VALUES(?, ?, ?, ?, ?)", create_accessories(500))
        con.commit()
    except sqlite3.Error as e:
        print "Error while creating the fashion db.", e
        if con:
            con.rollback()
    finally:
        if con:
            con.close()
