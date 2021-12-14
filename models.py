from app import db


class Wishlist(db.Model):
    __tabletitle__ = 'wishlist'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(150))
    link = db.Column(db.String(100))
    photo = db.Column(db.String(100))

    def __init__(self, title, description, link, photo):
        self.title = title
        self.description = description
        self.link = link
        self.photo = photo

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'link': self.link,
            'photo': self.photo
        }
