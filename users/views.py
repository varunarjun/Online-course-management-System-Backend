from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .models import User
from .serializers import UserSerializer

# -----------------------------
# Register new user
# -----------------------------
class RegisterUserView(generics.CreateAPIView):
    """
    Register a new user.
    No authentication required.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# -----------------------------
# Login user (custom)
# -----------------------------
@swagger_auto_schema(
    method='POST',
    request_body=UserSerializer,
    responses={200: 'Returns JWT access token along with username and role'}
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_user(request):
    """
    Login user and return JWT token.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=400)

    if not user.check_password(password):
        return Response({"error": "Invalid credentials"}, status=400)

    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "username": user.username,
        "role": user.role
    })
