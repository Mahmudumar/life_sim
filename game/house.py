import pygame

from settings import WIDTH, HEIGHT


class House:
    def __init__(self):
        self.font = pygame.font.Font(
            None,
            max(20, int(WIDTH * 0.02)),
        )

        wall = max(10, int(WIDTH * 0.015))

        # Outer walls
        self.walls = [
            pygame.Rect(0, 0, WIDTH, wall),
            pygame.Rect(0, 0, wall, HEIGHT),
            pygame.Rect(WIDTH - wall, 0, wall, HEIGHT),
            pygame.Rect(0, HEIGHT - wall, WIDTH, wall),
        ]

        # Rooms
        self.bedroom = pygame.Rect(
            WIDTH * 0.06,
            HEIGHT * 0.10,
            WIDTH * 0.38,
            HEIGHT * 0.32,
        )

        self.kitchen = pygame.Rect(
            WIDTH * 0.56,
            HEIGHT * 0.10,
            WIDTH * 0.38,
            HEIGHT * 0.32,
        )

        self.bathroom = pygame.Rect(
            WIDTH * 0.06,
            HEIGHT * 0.55,
            WIDTH * 0.25,
            HEIGHT * 0.25,
        )

        # Furniture
        self.bed = pygame.Rect(
            WIDTH * 0.12,
            HEIGHT * 0.17,
            WIDTH * 0.22,
            HEIGHT * 0.12,
        )

        self.fridge = pygame.Rect(
            WIDTH * 0.62,
            HEIGHT * 0.16,
            WIDTH * 0.08,
            HEIGHT * 0.16,
        )

        self.table = pygame.Rect(
            WIDTH * 0.75,
            HEIGHT * 0.20,
            WIDTH * 0.12,
            HEIGHT * 0.08,
        )

        self.shower = pygame.Rect(
            WIDTH * 0.10,
            HEIGHT * 0.60,
            WIDTH * 0.12,
            HEIGHT * 0.12,
        )

        # Exit
        self.exit_rect = pygame.Rect(
            WIDTH * 0.45,
            HEIGHT * 0.88,
            WIDTH * 0.10,
            HEIGHT * 0.07,
        )

    def draw_label(self, screen, text, rect):
        label = self.font.render(
            text,
            True,
            (255, 255, 255),
        )

        screen.blit(
            label,
            label.get_rect(center=rect.center),
        )

    def draw(self, screen):
        # Floor
        screen.fill((185, 165, 135))

        # Rooms
        pygame.draw.rect(
            screen,
            (205, 190, 165),
            self.bedroom,
        )

        pygame.draw.rect(
            screen,
            (195, 180, 155),
            self.kitchen,
        )

        pygame.draw.rect(
            screen,
            (175, 195, 195),
            self.bathroom,
        )

        # Room boundaries
        room_wall = max(5, int(WIDTH * 0.008))

        pygame.draw.rect(
            screen,
            (90, 80, 70),
            self.bedroom,
            room_wall,
        )

        pygame.draw.rect(
            screen,
            (90, 80, 70),
            self.kitchen,
            room_wall,
        )

        pygame.draw.rect(
            screen,
            (90, 80, 70),
            self.bathroom,
            room_wall,
        )

        # Bed
        pygame.draw.rect(
            screen,
            (80, 120, 190),
            self.bed,
            border_radius=8,
        )

        self.draw_label(
            screen,
            "BED",
            self.bed,
        )

        # Fridge
        pygame.draw.rect(
            screen,
            (180, 180, 185),
            self.fridge,
            border_radius=5,
        )

        self.draw_label(
            screen,
            "FRIDGE",
            self.fridge,
        )

        # Table
        pygame.draw.rect(
            screen,
            (130, 85, 50),
            self.table,
            border_radius=5,
        )

        self.draw_label(
            screen,
            "TABLE",
            self.table,
        )

        # Shower
        pygame.draw.rect(
            screen,
            (100, 160, 180),
            self.shower,
            border_radius=5,
        )

        self.draw_label(
            screen,
            "SHOWER",
            self.shower,
        )

        # Outer walls
        for wall in self.walls:
            pygame.draw.rect(
                screen,
                (65, 55, 50),
                wall,
            )

        # Exit
        pygame.draw.rect(
            screen,
            (100, 55, 40),
            self.exit_rect,
            border_radius=5,
        )

        self.draw_label(
            screen,
            "EXIT",
            self.exit_rect,
        )
        
    def get_interaction(self, player_rect):
        if player_rect.colliderect(self.bed):
            return "sleep"

        if player_rect.colliderect(self.fridge):
            return "eat"

        if player_rect.colliderect(self.shower):
            return "shower"

        if player_rect.colliderect(self.exit_rect):
            return "exit"

        return None

    def get_interaction_text(self, player_rect):
        if player_rect.colliderect(self.bed):
            return "Press E to sleep"

        if player_rect.colliderect(self.fridge):
            return "Press E to eat"

        if player_rect.colliderect(self.shower):
            return "Press E to shower"

        if player_rect.colliderect(self.exit_rect):
            return "Press E to leave"

        return None