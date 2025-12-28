from src.support.utils import normalize
from src.services.auth_service import AuthService


def before_scenario(context, scenario):
    context.normalize = normalize
    context.auth_service = AuthService()
