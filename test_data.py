"""Data to populate test db."""

from model import User, Location, Food, db

def example_data():
    """Creating some sample data."""
    

    liz = User(user_id=1, email="liz@test.com", password="test", user_name="liz")
    maggie = User(user_id=2, email="maggie@test.com", password="test", user_name="maggie")
    nadine = User(user_id=3, email="nadine@test.com", password="test", user_name="nadine")

    fridge = Location(loc_id=1, loc_name="Refrigerator")
    freezer = Location(loc_id=2, loc_name="Freezer")
    pantry = Location(loc_id=3, loc_name="Pantry")
    db.session.add_all([fridge, freezer, pantry])
    db.session.commit()

    banana = Food(food_id=1, food_name="banana", shelf_life=300, loc_id=3)
    chicken = Food(food_id=2, food_name="chicken", shelf_life=302400, loc_id=2)
    carrot = Food(food_id=3, food_name="carrot", shelf_life=43200, loc_id=1)
    peanuts = Food(food_id=4, food_name="peanuts", shelf_life=600, loc_id=3)

    db.session.add_all([liz, maggie, nadine, banana, chicken, carrot, peanuts])
    db.session.commit()

