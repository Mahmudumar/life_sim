import pygame

from settings import WIDTH, HEIGHT


class Shop:
    def __init__(self):
        self.font = pygame.font.Font(
            None,
            max(20, int(WIDTH * 0.02)),
        )

        self.counter = pygame.Rect(
            WIDTH * 0.35,
            HEIGHT * 0.30,
            WIDTH * 0.30,
            HEIGHT * 0.15,
        )

        self.exit_rect = pygame.Rect(
            WIDTH * 0.45,
            HEIGHT * 0.82,
            WIDTH * 0.10,
            HEIGHT * 0.08,
        )

        self.food_price = 5

    def draw(self, screen):
        screen.fill((170, 170, 160))

        wall = max(10, int(WIDTH * 0.015))

        # Walls
        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (0, 0, WIDTH, wall),
        )

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (0, 0, wall, HEIGHT),
        )

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (WIDTH - wall, 0, wall, HEIGHT),
        )

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (0, HEIGHT - wall, WIDTH, wall),
        )

        # Counter
        pygame.draw.rect(
            screen,
            (130, 85, 45),
            self.counter,
            border_radius=8,
        )

        counter_text = self.font.render(
            "FOOD ₦5",
            True,
            (255, 255, 255),
        )

        screen.blit(
            counter_text,
            counter_text.get_rect(
                center=self.counter.center
            ),
        )

        # Exit
        pygame.draw.rect(
            screen,
            (100, 55, 40),
            self.exit_rect,
            border_radius=5,
        )

        exit_text = self.font.render(
            "EXIT",
            True,
            (255, 255, 255),
        )

        screen.blit(
            exit_text,
            exit_text.get_rect(
                center=self.exit_rect.center
            ),
        )

    def get_interaction(self, player_rect):
        if player_rect.colliderect(self.counter):
            return "buy_food"

        if player_rect.colliderect(self.exit_rect):
            return "exit"

        return None

    def get_interaction_text(self, player_rect, money):
        if player_rect.colliderect(self.counter):

            if money >= self.food_price:
                return f"Press E to buy food - NGN {self.food_price}"

            return "Not enough money"

        if player_rect.colliderect(self.exit_rect):
            return "Press E to leave"

        return None