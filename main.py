import pygame

from settings import WIDTH, HEIGHT, FPS, TITLE
from game.world import World
from game.player import Player
from game.time import GameTime
from game.house import House

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

world = World()
player = Player()
game_time = GameTime()
house = House()

current_location = "city"

# Font for the HUD
font = pygame.font.Font(None, 28)


running = True

while running:
    dt = clock.tick(FPS) / 1000

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:

                if current_location == "city":

                    home = world.buildings[0]["rect"]

                    if player.rect.colliderect(home):
                        current_location = "house"

                        player.rect.center = (
                            WIDTH // 2,
                            HEIGHT // 2
                        )

                elif current_location == "house":

                    if player.rect.colliderect(house.exit_rect):
                        current_location = "city"

                        player.rect.center = (
                            WIDTH * 0.25,
                            HEIGHT // 2
                        )

    # Update
    game_time.update(dt)
    player.update(dt)

    if current_location == "city":
        world.draw(screen)

    elif current_location == "house":
        house.draw(screen)

    player.draw(screen)

    # HUD
    hud_width = 230
    hud_height = 190

    hud_surface = pygame.Surface(
        (hud_width, hud_height),
        pygame.SRCALPHA
    )

    # Semi-transparent dark background
    hud_surface.fill((20, 20, 20, 180))

    # Small title
    title_font = pygame.font.Font(None, 30)
    stat_font = pygame.font.Font(None, 25)

    title = title_font.render(
        "LIFE",
        True,
        (255, 255, 255)
    )

    hud_surface.blit(title, (15, 12))


    # Time
    time_text = stat_font.render(
        game_time.get_time(),
        True,
        (255, 255, 255)
    )

    hud_surface.blit(time_text, (15, 45))


    # Helper function for stat bars
    def draw_stat(surface, name, value, y):
        label = stat_font.render(
            name,
            True,
            (255, 255, 255)
        )

        surface.blit(
            label,
            (15, y)
        )

        # Bar background
        bar_x = 85
        bar_y = y + 3
        bar_width = 125
        bar_height = 14

        pygame.draw.rect(
            surface,
            (60, 60, 60),
            (bar_x, bar_y, bar_width, bar_height),
            border_radius=5
        )

        # Bar value
        fill_width = int(
            bar_width * (value / 100)
        )

        pygame.draw.rect(
            surface,
            (90, 200, 100),
            (bar_x, bar_y, fill_width, bar_height),
            border_radius=5
        )


    draw_stat(
        hud_surface,
        "Hunger",
        player.hunger,
        75
    )

    draw_stat(
        hud_surface,
        "Energy",
        player.energy,
        105
    )

    draw_stat(
        hud_surface,
        "Hygiene",
        player.hygiene,
        135
    )


    # Money
    money_text = stat_font.render(
        f"NGN {player.money}",
        True,
        (255, 220, 100)
    )

    hud_surface.blit(
        money_text,
        (15, 162)
    )


    # Put HUD on screen
    screen.blit(
        hud_surface,
        (15, 15)
    )

    pygame.display.flip()


pygame.quit()