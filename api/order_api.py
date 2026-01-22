import requests


class OrderAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    # -----------------------
    # Get Cart Details
    def get_cart(self,session_cookie):
        # Maintain session for cookies/authentication
        return requests.get(f"{self.base_url}/cart", cookies={"session_username": session_cookie}
                            )