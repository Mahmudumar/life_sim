import pygame

from settings import (
    WIDTH,
    HEIGHT,
    GRASS,
    ROAD,
    HOUSE,
    SHOP,
    WORK,
    PARK,
)


class World:
    def __init__(self):
        # Everything is calculated from the current screen size.
        # Nothing here assumes a specific resolution.

        road_width = WIDTH * 0.08
        road_height = HEIGHT * 0.14

        building_width = WIDTH * 0.20
        building_height = HEIGHT * 0.20

        left_x = WIDTH * 0.08
        right_x = WIDTH - left_x - building_width

        top_y = HEIGHT * 0.10
        bottom_y = HEIGHT - building_height - (HEIGHT * 0.10)

        self.buildings = [
            {
                "name": "Home",
                "rect": pygame.Rect(
                    left_x,
                    top_y,
                    building_width,
                    building_height,
                ),
                "color": HOUSE,
            },
            {
                "name": "Shop",
                "rect": pygame.Rect(
                    right_x,
                    top_y,
                    building_width,
                    building_height,
                ),
                "color": SHOP,
            },
            {
                "name": "Work",
                "rect": pygame.Rect(
                    right_x,
                    bottom_y,
                    building_width,
                    building_height,
                ),
                "color": WORK,
            },
            {
                "name": "Park",
                "rect": pygame.Rect(
                    left_x,
                    bottom_y,
                    building_width,
                    building_height,
                ),
                "color": PARK,
            },
        ]

        #  Entrance to the house
        self.home_door = pygame.Rect(
            WIDTH * 0.16,
            top_y + building_height,
            WIDTH * 0.06,
            HEIGHT * 0.03,
        )
        self.shop_door = pygame.Rect(
            right_x + building_width * 0.45,
            top_y + building_height,
            WIDTH * 0.06,
            HEIGHT * 0.03,
        )

        self.road_vertical = pygame.Rect(
            (WIDTH - road_width) / 2,
            0,
            road_width,
            HEIGHT,
        )

        self.road_horizontal = pygame.Rect(
            0,
            (HEIGHT - road_height) / 2,
            WIDTH,
            road_height,
        )

        self.font = pygame.font.Font(
            None,
            max(20, int(WIDTH * 0.02)),
        )

    def draw(self, screen):
        # Ground
        screen.fill(GRASS)

        # Roads
        pygame.draw.rect(
            screen,
            ROAD,
            self.road_vertical,
        )

        pygame.draw.rect(
            screen,
            ROAD,
            self.road_horizontal,
        )

        # Buildings
        for building in self.buildings:
            rect = building["rect"]

            pygame.draw.rect(
                screen,
                building["color"],
                rect,
            )

            text = self.font.render(
                building["name"],
                True,
                (255, 255, 255),
            )

            text_rect = text.get_rect(
                center=rect.center
            )

            screen.blit(
                text,
                text_rect,
            )

        # Home entrance
        pygame.draw.rect(
            screen,
            (100, 60, 40),
            self.home_door,
        )
        # Shop entrance
        pygame.draw.rect(
            screen,
            (100, 60, 40),
            self.shop_door,
        )