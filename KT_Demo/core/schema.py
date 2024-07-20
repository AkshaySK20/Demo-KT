import graphene
from graphene_django import DjangoObjectType
from .models import CarDetails, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class CarDetailsType(DjangoObjectType):
    class Meta:
        model = CarDetails
        fields = ("id", "title", "brand", 'category')

class Query(graphene.ObjectType):
    all_category = graphene.List(CategoryType)
    all_cardetails = graphene.List(CarDetailsType)

    def resolve_all_category(root, info):
        return Category.objects.all()
    def resolve_all_cardetails(root, info):
        return CarDetails.objects.all()

class CategoryMutation(graphene.Mutation):
    class Arguments:
        category_name = graphene.String(required=True)
        #category_id = graphene.Int(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls,root, info,category_name):
        new_catname = Category(name=category_name)
        new_catname.save()
        #To delete the category
        #new_catname.delete()
        return cls(category=new_catname)

class CarMutation(graphene.Mutation):
    class Arguments:
        new_title = graphene.String(required=True)
        new_brand = graphene.String(required=True)
        category_name = graphene.String(required=True)

    cardetails = graphene.Field(CarDetailsType)

    @classmethod
    def mutate(cls, root, info, new_title, new_brand, category_name):
        try:
            category_instance = Category.objects.get(name=category_name)
        except Category.DoesnotExist:
            raise Exception(f'Category with name "{category_name} does not exist.')

        cardetails = CarDetails(title=new_title, brand=new_brand, category=category_instance)
        cardetails.save()
        return cls(cardetails=cardetails)

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()
    update_cardetails = CarMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
