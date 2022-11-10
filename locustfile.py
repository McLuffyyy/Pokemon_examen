from locust import HttpUser, task, between


class QuickStarUser(HttpUser):
    wait_time = between(1,5)

    trainer_1_id: int
    trainer_2_id: int = 1

    pokemon_1_id: int
    pokemon_2_id: int = 1
    
    @task
    def get_home(self):
        response = self.client.post("/trainers/", json={"name": "Thomas", "birthdate": "2022-11-08"})
        self.trainer_2_id = response.json()["id"]
        
        response = self.client.post("/trainers/"+str(self.trainer_1_id)+"/pokemon/", json={"api_id": 3, "custom_name": "Florizard"})
        self.pokemon_1_id = response.json()["id"]

        response = self.client.get("/pokemons/battle/"+str(self.pokemon_1_id)+"/"+str(self.pokemon_2_id)).json()

