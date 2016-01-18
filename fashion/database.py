import sqlite3

from fashion.defaults import FASHION_DATABASE


def get_fashion_items(page, items_per_page):
    """
    Retrieves a list of fashion items from the db
    :param page: Page of items
    :param items_per_page: number of items per page
    :return: List of fashion items
    """
    try:
        con = sqlite3.connect(FASHION_DATABASE)
        with con:
            cur = con.cursor()
            # Gets a subset of fashion items based on the page and items per page
            cur.execute("SELECT title, blurb, author, thumbnail_url, details_url "
                        "FROM FashionItem "
                        "order by id ASC LIMIT {}, {}".format(
                            (page - 1) * items_per_page, items_per_page))
            rows = cur.fetchall()
        con.commit()
        return rows
    except sqlite3.Error:
        if con:
            con.rollback()
    finally:
        if con:
            con.close()
