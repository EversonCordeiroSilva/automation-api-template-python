from src.services.service_environment import ServiceEnvironment
import requests


class AuthService:
    def login_valid_user(self):
        return self.login("john@mail.com", "changeme")

    def login(self, email, password):
        payload = {}

        if email is not None:
            payload["email"] = email
        else:
            payload["email"] = ""
        if password is not None:
            payload["password"] = password
        else:
            payload["password"] = ""

        return requests.post(f"{ServiceEnvironment.BASE_URL}/api/v1/auth/login",json=payload)
