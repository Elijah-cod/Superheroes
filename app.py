from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models AFTER initializing db
from models import Hero, Power, HeroPower

@app.route('/')
def index():
    return '<h1>Welcome Heroes</h1>'

@app.route('/heroes', methods=['GET'])
def get_all_heroes():
    all_heroes = Hero.query.all()
    heroes_list = [hero.to_dict(depth=0) for hero in all_heroes]
    # print(heroes_list)
    return jsonify(heroes_list)

@app.route('/heroes/<int:heroes_id>', methods=['GET'])
def get_heroes(heroes_id):
    hero = Hero.query.get(heroes_id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict())


@app.route('/powers', methods=['GET'])
def get_all_powers():
    all_powers = Power.query.all()
    powers_list = [power.to_dict(depth=0) for power in all_powers]
    # print(heroes_list)
    return jsonify(powers_list)

@app.route('/powers/<int:powers_id>', methods=['GET'])
def get_powers(powers_id):
    power = Power.query.get(powers_id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())


@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    """Updates a power's information by ID."""
    power = Power.query.get(power_id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    try:
        if 'description' in data:
            power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict())
    except KeyError:
        return jsonify({"error": "Invalid fields"}), 400
    

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    """Creates a new HeroPower."""
    data = request.get_json(force=True)  # Ensure we get JSON data

    # Validate input data
    required_fields = {"strength", "power_id", "hero_id"}
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if the referenced Hero and Power exist
    hero = Hero.query.get(data["hero_id"])
    power = Power.query.get(data["power_id"])

    if not hero or not power:
        return jsonify({"error": "Hero or Power not found"}), 404

    # Create new HeroPower entry
    new_hero_power = HeroPower(
        strength=data["strength"],
        hero_id=data["hero_id"],
        power_id=data["power_id"]
    )

    db.session.add(new_hero_power)
    db.session.commit()

    return jsonify(new_hero_power.to_dict()), 200
