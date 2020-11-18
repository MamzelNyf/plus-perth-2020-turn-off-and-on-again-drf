from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)


class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(Self, request, view, obj):
        logger.info(f"obj {str(obj.__dict__)}")
        logger.info(f"request.user {str(request.user.__dict__)}")
        logger.info(request.user == obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.username == request.user.username
        

