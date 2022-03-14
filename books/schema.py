from graphene_django import DjangoObjectType
import graphene
from .models import Book

class BooksType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ["id","title","excerpt"]

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)

    @graphene.resolve_only_args
    def resolve_users(self):
        return Book.objects.all()

schema = graphene.Schema(query=Query)