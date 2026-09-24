import pygame

from settings import (
    PLAYER_SPEED,
    PLAYER_COLOR,
    WIDTH,
    HEIGHT,
)


class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - 15,
            HEIGHT // 2 - 15,
            30,
            30,
        )

        # Needs
        self.hunger = 20
        self.energy = 100
        self.hygiene = 100

        # Resources
        self.money = 10

    def update(self, dt):
        self.move(dt)
        self.update_needs(dt)

    def move(self, dt):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            dy -= 1

        if keys[pygame.K_s]:
            dy += 1

        if keys[pygame.K_a]:
            dx -= 1

        if keys[pygame.K_d]:
            dx += 1

        if dx != 0 or dy != 0:
            direction = pygame.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * PLAYER_SPEED * dt
            self.rect.y += direction.y * PLAYER_SPEED * dt

            # Moving consumes energy
            self.energy -= 2 * dt

            # Moving makes you slightly hungry
            self.hunger += 0.5 * dt

            # Moving makes you slightly less clean
            self.hygiene -= 0.2 * dt

        # Keep player inside the world
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)

        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(HEIGHT, self.rect.bottom)

    def update_needs(self, dt):
        # Hunger slowly increases with time
        self.hunger += 1 * dt

        # Energy slowly decreases
        self.energy -= 0.15 * dt

        # Keep values between 0 and 100
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.hygiene = max(0, min(100, self.hygiene))

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            PLAYER_COLOR,
            self.rect,
        )