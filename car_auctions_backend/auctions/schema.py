import graphene



class Query(graphene.ObjectType):
    hello = graphene.String(default_value="TEST")

schema = graphene.Schema(query=Query)