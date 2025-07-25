from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Post/Comment owner faqat o'z post/commentini
    tahrirlashi yoki o'chirishi munkin.

    Boshqalar faqat ko'ra oladi
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
