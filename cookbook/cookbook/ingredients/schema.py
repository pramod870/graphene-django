import graphene


from graphene_django.types import DjangoObjectType

from .models import Category, Ingredient




class CategoryType(DjangoObjectType):
    class Meta:

        model = Category


class IngredientType(DjangoObjectType):

    class Meta:

        model = Ingredient



class Query(object):


    all_categories = graphene.List(CategoryType)

    all_ingredients = graphene.List(IngredientType)


    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()


    def resolve_all_ingredients(self, info, **kwargs):

        return Ingredient.objects.select_related('category').all()


# Add new category Mutation


class SubCategory(graphene.Mutation):
    class Arguments:

        subcategoryName = graphene.String(required = True)

    category = graphene.Field(CategoryType)


    def mutate(self, info, subcategoryName):

        _category = Category.objects.create(name=subcategoryName)


        return SubCategory(category=_category)


class Mutation(object):
    add_category = SubCategory.Field()
