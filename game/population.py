from game.npc import NPC

from settings import WIDTH, HEIGHT


class Population:

    def __init__(self, buildings):

        self.npcs = [
            NPC(
                buildings,
                "Amina",
                (
                    WIDTH * 0.25,
                    HEIGHT * 0.25
                )
            ),

            NPC(
                buildings,
                "David",
                (
                    WIDTH * 0.70,
                    HEIGHT * 0.25
                )
            ),

            NPC(
                buildings,
                "John",
                (
                    WIDTH * 0.25,
                    HEIGHT * 0.70
                )
            ),

            NPC(
                buildings,
                "Fatima",
                (
                    WIDTH * 0.70,
                    HEIGHT * 0.70
                )
            ),
        ]

    def update(self, dt, game_time, player_rect):

        for npc in self.npcs:
            npc.update(
                dt,
                game_time,
                player_rect
            )

    def draw(self, screen):

        for npc in self.npcs:
            npc.draw(screen)

    def get_nearby_npc(self, player_rect):

        nearby_npc = None
        closest_distance = float("inf")

        for npc in self.npcs:

            distance = player_rect.centerx - npc.rect.centerx
            distance_y = player_rect.centery - npc.rect.centery

            distance = (
                distance ** 2
                + distance_y ** 2
            ) ** 0.5

            if distance <= 40 and distance < closest_distance:
                nearby_npc = npc
                closest_distance = distance

        return nearby_npc