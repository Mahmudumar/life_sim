import pygame

from settings import WIDTH, HEIGHT


class NPC:
    def __init__(self, buildings, name, start_position):
        self.rect = pygame.Rect(
            start_position[0],
            start_position[1],
            28,
            28
        )

        self.speed = 90
        self.color = (60, 80, 220)

        self.name = name

        self.target = None
        self.activity = "Home"
        self.buildings = buildings

        # Needs
        self.hunger = 20
        self.energy = 100
        self.hygiene = 100

        # Social
        self.relationship = 0
        self.last_message = ""
        self.last_talk_day = 0

        # Resources
        self.money = 30
        self.food = 2

        # Job
        self.salary = 20
        self.last_work_day = 0

        # Prevent repeated activity
        self.activity_done = False

    def get_target(self, game_time):
        hour = game_time.get_hour()

        if 8 <= hour < 17:
            return "Work"

        if 17 <= hour < 20:
            return "Park"

        if 20 <= hour < 22:
            return "Shop"

        return "Home"

    def update(self, dt, game_time, player_rect):
        self.update_needs(dt)

        target_name = self.get_target(game_time)

        # Schedule changed
        if target_name != self.activity:
            self.activity = target_name
            self.target = None
            self.activity_done = False

        # Find destination
        if self.target is None:
            for building in self.buildings:
                if building["name"] == self.activity:
                    self.target = pygame.Vector2(
                        building["rect"].center
                    )
                    break

        if self.target is None:
            return

        current_position = pygame.Vector2(
            self.rect.center
        )

        direction = self.target - current_position

        # Still travelling
        if direction.length() > 5:
            direction = direction.normalize()

            movement = (
                direction
                * self.speed
                * dt
            )

            self.rect.x += movement.x
            self.rect.y += movement.y

        else:
            # We have arrived
            self.perform_activity(
                game_time
            )

    def perform_activity(self, game_time):
        if self.activity_done:
            return

        self.activity_done = True

        if self.activity == "Work":
            self.money += self.salary

            self.energy -= 35
            self.hunger += 20
            self.hygiene -= 10

            self.last_work_day = game_time.day

        elif self.activity == "Park":
            self.energy += 15

        elif self.activity == "Shop":
            if self.money >= 5:
                self.money -= 5
                self.food += 1

        elif self.activity == "Home":
            # Eat if hungry
            if self.hunger >= 60 and self.food > 0:
                self.food -= 1
                self.hunger -= 30

            # Sleep
            self.energy = 100

            # Shower
            self.hygiene = 100

    def update_needs(self, dt):
        self.hunger += 1 * dt
        self.energy -= 0.15 * dt
        self.hygiene -= 0.2 * dt

        self.hunger = max(
            0,
            min(100, self.hunger)
        )

        self.energy = max(
            0,
            min(100, self.energy)
        )

        self.hygiene = max(
            0,
            min(100, self.hygiene)
        )

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=6
        )

        font = pygame.font.Font(
            None,
            max(18, int(WIDTH * 0.015))
        )

        text = font.render(
            self.name,
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(
                self.rect.centerx,
                self.rect.top - 10
            )
        )

        screen.blit(
            text,
            text_rect
        )

    def get_interaction(self, player_rect):
        if player_rect.colliderect(
            self.rect.inflate(40, 40)
        ):
            return "talk"

        return None

    def talk(self, game_time):
        # Relationship improves once per day
        if self.last_talk_day == game_time.day:
            return "We already talked today."

        self.last_talk_day = game_time.day

        self.relationship += 1

        if self.relationship <= 2:
            messages = [
                "Hey.",
                "Hello.",
            ]

        elif self.relationship <= 5:
            messages = [
                "Good to see you again.",
                "How has your day been?",
                "You around here often?",
            ]

        elif self.relationship <= 9:
            messages = [
                "Good to see you!",
                "How's life going?",
                "We should hang out sometime.",
            ]

        else:
            messages = [
                "Hey, my friend!",
                "Good to see you again.",
                "How are things going?",
            ]

        message = messages[
            self.relationship % len(messages)
        ]

        self.last_message = message

        return message

    def get_relationship_label(self):
        if self.relationship <= 2:
            return "Stranger"

        if self.relationship <= 5:
            return "Acquaintance"

        if self.relationship <= 9:
            return "Friend"

        return "Close Friend"