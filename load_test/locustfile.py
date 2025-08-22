from locust import HttpUser, task, between
from datetime import datetime, timezone

class HelloWorldUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_products(self):
        self.client.get("/v1/api/item-types") # Get items
    
    @task
    def make_order(self):
        timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
        self.client.post("/v1/api/orders", json={
            "commandType":0,
            "orderSource":0,
            "location":0,
            "loyaltyMemberId":"3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "timestamp":timestamp,
            "baristaItems":[
                {"itemType":5},
                {"itemType":4},
                {"itemType":0},
                {"itemType":2},
                {"itemType":3}
            ],
            "kitchenItems":[
                {"itemType":8},
                {"itemType":9},
                {"itemType":6},
                {"itemType":7}
            ],
        })
    
    @task
    def get_orders(self):
        self.client.get("/v1/fulfillment-orders") # Get orders




# http://192.168.1.107:5000