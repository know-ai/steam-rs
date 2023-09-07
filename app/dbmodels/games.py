from .base import BaseModel
from app.extensions.db import db
from datetime import datetime
from .publishers import Publishers
from .developers import Developers
from .genres import Genres
from .tags import Tags
from .specs import Specs

DATE_FORMAT = "%Y-%m-%d"


games_genres = db.Table(
    'games_genres',
    db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'))
)

games_tags = db.Table(
    'games_tags',
    db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

games_specs = db.Table(
    'games_specs',
    db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
    db.Column('spec_id', db.Integer, db.ForeignKey('specs.id'))
)

games_users = db.Table(
    'games_users',
    db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)
 

class Games(BaseModel):

    __tablename__ = 'games'
    title = db.Column(db.String(50), unique=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))
    release_date = db.Column(db.DateTime())
    discount_price = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float)
    early_access = db.Column(db.Boolean)
    metascore = db.Column(db.Float, nullable=True)
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'))
    genres = db.relationship('Genres', secondary=games_genres, backref='games', lazy='dynamic', cascade="all, delete") 
    tags = db.relationship('Tags', secondary=games_tags, backref='tags', lazy='dynamic', cascade="all, delete")
    specs = db.relationship('Specs', secondary=games_specs, backref='specs', lazy='dynamic', cascade="all, delete")
    users = db.relationship('Users', secondary=games_users, backref='games', lazy='dynamic', cascade="all, delete")
    playtime = db.relationship('Playtime',  backref='game', lazy='dynamic', cascade="all, delete")

    @classmethod
    def add(
        cls, 
        id:int, 
        name:str,
        title:str,
        price:float,
        release_date:str,
        discount_price:float=0.0,
        publisher:str=None,
        developer:str=None,
        early_access:bool=False,
        metascore:float=0.0
        ):
        """
        Documentation here
        """
        if (not cls.id_exists(id) and not cls.name_exists(name) and not cls.title_exists(title)):

            if price <= 0.0:

                raise ValueError(f"price must be > 0.0, you summit: {price}")
            if discount_price is not None:

                if discount_price >= price or discount_price < 0:

                    raise ValueError(f"price > discount_price must be > 0, you summit: {discount_price}")
            
            publisher = Publishers.get_by_name_or_create(name=publisher)
            developer = Developers.get_by_name_or_create(name=developer)
            attr = cls(
                id=id,
                name=name,
                title=title,
                price=price,
                release_date=datetime.strptime(release_date, DATE_FORMAT).date(),
                discount_price=discount_price,
                publisher_id=publisher.id,
                developer_id=developer.id,
                early_access=early_access,
                metascore=metascore
            )
            db.session.add(attr)
            db.session.commit()

            return attr

    @classmethod
    def title_exists(cls, title:str):
        r"""
        Documentation here
        """
        attr = cls.get(title=title)

        if attr:
            
            return True
        
        return False
    
    def add_genre(self, genre:str):
        """
        Documentation here
        """

        return Genres.get_by_name_or_create(name=genre)
    
    def add_genres(self, *genres):
        """
        Documentation here
        """
        for genre in genres:
            
            obj = self.add_genre(genre)
            self.genres.append(obj)

    def add_tag(self, tag:str):
        """
        Documentation here
        """

        return Tags.get_by_name_or_create(name=tag)
    
    def add_tags(self, *tags):
        """
        Documentation here
        """
        for tag in tags:
            
            obj = self.add_tag(tag)
            self.tags.append(obj)

    def add_spec(self, spec:str):
        """
        Documentation here
        """

        return Specs.get_by_name_or_create(name=spec)
    
    def add_specs(self, *specs):
        """
        Documentation here
        """
        for spec in specs:
            
            obj = self.add_spec(spec)
            self.specs.append(obj)

    def get_all_users(self):
        """
        Documenation here
        """
        return [user.serialize() for user in self.users.all()]

    def serialize(self):
        """
        Documentation here
        """
        return {
            "id": self.id,
            "title": self.title,
            "name": self.name,
            "price": self.price,
            "release_date": self.release_date.date().strftime(DATE_FORMAT),
            "discount_price": self.discount_price,
            "publisher": None if self.publisher is None else self.publisher.name,
            "developer": None if self.developer is None else self.developer.name,
            "early_access": self.early_access,
            "metascore": self.metascore,
            "genres": [genre.name for genre in self.genres],
            "tags": [tag.name for tag in self.tags],
            "specs": [spec.name for spec in self.specs],
            "url": f"http://store.steampowered.com/app/{self.id}/{self.name}/"
        }