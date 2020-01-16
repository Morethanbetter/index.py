from index.view import View
from index.test import TestView


class HTTP(View):
    def get(self):
        raise ValueError("some error")


class Test(TestView):
    def test_valueerror(self):
        resp = self.client.get()
        assert resp.text == "Something went wrong with the server."
