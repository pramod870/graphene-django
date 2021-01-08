from graphql import GraphQLError
from .models import Human

def resolver_humans():
    return Human.objects.all()

def resolver_human(id):

    try:
        return Human.objects.get(id=id)

    except Human.DoesNotExist:

        raise GraphQLError("Could not find the human object with given id: " + str(id))

    return


def resolver_delete_human(id):
    try:
        _ =Human.objects.get(id=id).delete()


    except Human.DoesNotExist:
        raise GraphQLError("Could not find the human object with the given id: "+str(id))

    return

def resolver_create_human(id, name,gender, birth_year, mass, height, home_planet):
    return Human.objects.create(
        id= id,
        name = name,
        gender = gender,
        birth_year = birth_year,
        mass = mass,
        height = height,
        home_planet = home_planet,

    )


def resolver_update_human(id, name, gender, birth_year, mass, height, home_planet):
    _ = Human.objects.get(id=id).delete()
    return Human.objects.create(
        id = id,
        name = name,
        gender = gender,
        birth_year = birth_year,
        mass = mass,
        height = height,
        home_planet = home_planet
    )
