import time
import sys
import secrets

import validators

import sqlite3
from sqlite3 import Error

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

domain = "http://127.0.0.1:5000/"

class ShortDB():
    def __init__(self) -> None:
        self.dbname = r"short.db"
        self.tablename = "shorts"
        self.conn = None
        self.create_connection()
        pass

    def create_connection(self):
        """ create a database connection to a SQLite database """
        if self.dbname is None:
            raise Exception("No database file name!")

        try:
            self.conn = sqlite3.connect(self.dbname)
        except Error as e:
            print(e)
            sys.exit()

    def insert_short(self, short_tuple:tuple = None) -> bool:
        try:
            sql = f''' INSERT INTO {self.tablename}(short,url,datetime,hits)
                    VALUES(?,?,?,?) '''
            cur = self.conn.cursor()
            cur.execute(sql, short_tuple)
            self.conn.commit()
            return True
        except Error as e:
            print(e)  
            return False

    def check_short_exists(self, short:str = None) -> str: 
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT url, hits FROM {self.tablename} WHERE short=?", (short,))
            row = cur.fetchone()
            return row
        except Error as e:
            print(e)  
            return False

    def count_shorts(self) -> int:
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT Count() FROM {self.tablename}")
            return cur.fetchone()[0]
        except Error as e:
            print(e)  
            return 0        

    def update_short_hit(self, short:str = None) -> bool:
        try:
            sql = ''' UPDATE shorts
                    SET hits = hits+1
                    WHERE short = ?'''
            cur = self.conn.cursor()
            cur.execute(sql, (short,))
            self.conn.commit()
            return True
        except Error as e:
            print(e)  
            return False

    def get_url(self, url:str = None) -> str:
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT short FROM {self.tablename} WHERE url=?", (url,))

            row = cur.fetchone()
            return row
        except Error as e:
            print(e)  
            return False

    def save_short(self, short:str = None, url:str = None, datetime:int = None, hits:int = 0) -> str:
        try:
            with self.conn:
                # create a new project
                short_tuple = (short, url, datetime, hits)
                return self.insert_short(short_tuple=short_tuple)
        except Exception as e:
            print(e) 

class Shorts():

    def __init__(self) -> None:
        self.db = ShortDB()
        pass

    def short_to_url(self, short:str = None) -> str:
        row = self.db.check_short_exists(short)
        if row:
            self.db.update_short_hit(short)

        return row

    def url_to_short(self, url:str = None) -> str:
        short = self.db.get_url(url)
        if short:
            #url exsits so return short
            return short[0]

        short = self.randomizer()
        self.db.save_short(short=short, url=url, datetime=int(time.time()), hits=0)
        return short

    def randomizer(self) -> str:
        short = secrets.token_urlsafe(5)
        while self.db.check_short_exists(short=short):
            short = secrets.token_urlsafe(5)

        return short

    def nr_shorts(self):
        return self.db.count_shorts()

#this is the start of the site
@app.route("/")
def startpage():

    S = Shorts()
    shorts_no = S.nr_shorts()

    return render_template('url.html', message="")


#this is the short url
@app.route("/<short>")
def reroute(short):
    S = Shorts()
    try:
        print(short)
        row = S.short_to_url(short=short)
        print(row[0])
        return redirect(row[0], code=302)
    except Exception as e:
        print(e) 

@app.route("/url", methods=["GET", "POST"])
def process_url():
    if request.method == "POST":
        req = request.form
        if validators.url(req['short_url']):
            S = Shorts()
            short = S.url_to_short(url=req['short_url'])
            return f"We created this short for you : <a href='{domain}{short}'>{domain}{short}</a>"
        else:
            return render_template('url.html', message="Sorry that is not a correct URL")


if __name__ == "__main__":
    app.run()