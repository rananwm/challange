from rest_framework import response, decorators as rest_decorators, permissions as rest_permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='post',
    operation_description="Pay subscription endpoint",
    responses={
        200: openapi.Response(
            description="Success message",
            examples={
                "application/json": {
                    "msg": "Success"
                }
            }
        ),
        401: "Unauthorized"
    },
    security=[{'Bearer': []}]
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def paySubscription(request):
    return response.Response({"msg": "Success"}, 200)

@swagger_auto_schema(
    method='post',
    operation_description="List subscriptions endpoint",
    responses={
        200: openapi.Response(
            description="Success message",
            examples={
                "application/json": {
                    "msg": "Success"
                }
            }
        ),
        401: "Unauthorized"
    },
    security=[{'Bearer': []}]
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def listSubscriptions(request):
    return response.Response({"msg": "Success"}, 200)
