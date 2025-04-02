from app import db

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade="all, delete")

    def to_dict(self, depth=1):
        """Convert model to dictionary with controlled recursion depth."""
        data = {
            "id": self.id,
            "name": self.name
        }

        if depth > 0:
            data["hero_powers"] = [hp.to_dict(depth - 1) for hp in self.hero_powers]

        return data


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade="all, delete")

    def to_dict(self, depth=1):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

        if depth > 0:
            data["hero_powers"] = [hp.to_dict(depth - 1) for hp in self.hero_powers]

        return data


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id', ondelete='CASCADE'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    def to_dict(self, depth=1):
        data = {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id
        }

        if depth > 0:
            data["hero"] = {"id": self.hero.id, "name": self.hero.name} if self.hero else None
            data["power"] = {"id": self.power.id, "name": self.power.name} if self.power else None

        return data