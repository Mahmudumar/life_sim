class GameState:

    def __init__(self, player, game_time, job, npc):
        self.player = player
        self.game_time = game_time
        self.job = job
        self.npc = npc

    def get_observation(self, current_location):
        return {
            # World
            "location": current_location,
            "day": self.game_time.day,
            "time": self.game_time.get_time(),
            "period": self.game_time.get_period(),

            # Player
            "hunger": self.player.hunger,
            "energy": self.player.energy,
            "hygiene": self.player.hygiene,
            "health": self.player.health,

            "money": self.player.money,
            "food": self.player.food,

            # Job
            "job": self.job.title,
            "job_level": self.job.level,
            "salary": self.job.salary,

            # Social
            "npc": {
                "name": self.npc.name,
                "distance": self.get_npc_distance(),
                "relationship": self.npc.relationship,
                "relationship_label": (
                    self.npc.get_relationship_label()
                ),
                "activity": self.npc.activity,
            },

            # Life
            "alive": self.player.alive,
        }

    def get_npc_distance(self):
        player_position = self.player.rect.center
        npc_position = self.npc.rect.center

        dx = player_position[0] - npc_position[0]
        dy = player_position[1] - npc_position[1]

        return (dx ** 2 + dy ** 2) ** 0.5