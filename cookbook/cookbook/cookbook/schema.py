import graphene

from ingredients import schema
from users import schema

from swapi import schema
#import graphene.schema

class Query(schema.Query,graphene.ObjectType):

    pass


class Mutation(schema.Mutation, graphene.ObjectType):

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

class Query(schema.Query, graphene.ObjectType):
    pass

class Mutation(schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

#swapi


class Query(schema.Query, graphene.ObjectType):
    pass

class Mutation(schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)