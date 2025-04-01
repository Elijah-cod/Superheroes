from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade="all, delete")


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade="all, delete")


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id', ondelete='CASCADE'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')