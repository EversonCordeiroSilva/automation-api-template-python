from src.services.service_environment import ServiceEnvironment
import requests


class AuthService:
    def login_valid_user(self):
        return self.login("qa.automation.aos01@gmail.com","qa_auto_user01", "Test@1234")

    def login(self, email, user, password):
        payload = {}
        if email is not None:
            payload["email"] = email
        else:
            payload["email"] = ""
        if email is not None:
            payload["loginUser"] = user
        else:
            payload["loginUser"] = ""
        if password is not None:
            payload["loginPassword"] = password
        else:
            payload["loginPassword"] = ""

        return requests.post(f"{ServiceEnvironment.BASE_URL}/accountservice/accountrest/api/v1/login",json=payload)
