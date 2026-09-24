import pygame

from game.job import Job
from game.shop import Shop
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

shop = Shop()
job = Job()

current_location = "city"

job_message = ""
job_message_timer = 0

# Font for the HUD
font = pygame.font.Font(None, 28)


running = True

while running:
    dt = clock.tick(FPS) / 1000
    if job_message_timer > 0:
        job_message_timer -= dt

    if job_message_timer <= 0:
        job_message = ""

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:

                if current_location == "city":

                    if player.rect.colliderect(world.home_door):
                        current_location = "house"

                        player.rect.center = (
                            WIDTH // 2,
                            HEIGHT // 2
                        )

                    elif player.rect.colliderect(world.shop_door):
                        current_location = "shop"

                        player.rect.center = (
                            WIDTH // 2,
                            HEIGHT // 2
                        )
                    elif player.rect.colliderect(
                        world.buildings[2]["rect"]
                    ):
                        game_time.advance_hours(8)

                        player.energy = max(
                            0,
                            player.energy - 35
                        )

                        player.hunger = min(
                            100,
                            player.hunger + 20
                        )

                        player.hygiene = max(
                            0,
                            player.hygiene - 10
                        )

                        job_message = job.work(
                                        player,
                                        game_time
                                    )
                        job_message_timer = 4

                elif current_location == "house":
                    interaction = house.get_interaction(
                        player.rect
                    )

                    if interaction == "sleep":
                        game_time.advance_hours(8)
                        player.energy = 100

                        # Sleeping makes you hungry
                        player.hunger += 20

                        # Sleeping makes you slightly less clean
                        player.hygiene -= 10

                    elif interaction == "eat":

                        if player.food > 0:
                            player.food -= 1

                            player.hunger = max(
                                0,
                                player.hunger - 30
                            )

                    elif interaction == "shower":
                        player.hygiene = 100

                    elif player.rect.colliderect(
                        house.exit_rect
                    ):
                        current_location = "city"

                        player.rect.center = (
                            WIDTH * 0.19,
                            HEIGHT * 0.50
                        )

                elif current_location == "shop":

                    interaction = shop.get_interaction(
                        player.rect
                    )

                    if interaction == "buy_food":

                        if player.money >= shop.food_price:
                            player.money -= shop.food_price
                            player.food += 1

                    elif interaction == "exit":

                        current_location = "city"

                        player.rect.center = (
                            WIDTH * 0.75,
                            HEIGHT // 2
                        )


    # Update

    game_time.update(dt)
    player.update(dt)

    if not player.alive:
        current_location = "dead"

    if current_location == "city":
        world.draw(screen)

    elif current_location == "house":
        house.draw(screen)

    elif current_location == "shop":
        shop.draw(screen)

    elif current_location == "dead":
        screen.fill((20, 20, 20))

        death_font = pygame.font.Font(
            None,
            60
        )

        death_text = death_font.render(
            "YOU DIED",
            True,
            (220, 60, 60)
        )

        death_rect = death_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(
            death_text,
            death_rect
        )

    player.draw(screen)

    if current_location == "house":

        interaction_text = house.get_interaction_text(
            player.rect
        )

        if interaction_text:
            prompt_font = pygame.font.Font(
                None,
                28
            )

            prompt = prompt_font.render(
                interaction_text,
                True,
                (255, 255, 255)
            )

            prompt_rect = prompt.get_rect(
                center=(WIDTH // 2, HEIGHT - 40)
            )

            # Background behind the prompt
            background = pygame.Surface(
                (
                    prompt_rect.width + 20,
                    prompt_rect.height + 10
                ),
                pygame.SRCALPHA
            )

            background.fill(
                (20, 20, 20, 190)
            )

            screen.blit(
                background,
                (
                    prompt_rect.x - 10,
                    prompt_rect.y - 5
                )
            )

            screen.blit(
                prompt,
                prompt_rect
            )

    if job_message:

        message_font = pygame.font.Font(
            None,
            28
        )

        message = message_font.render(
            job_message,
            True,
            (255, 255, 255)
        )

        message_rect = message.get_rect(
            center=(WIDTH // 2, 80)
        )

        background = pygame.Surface(
            (
                message_rect.width + 30,
                message_rect.height + 20
            ),
            pygame.SRCALPHA
        )

        background.fill(
            (20, 20, 20, 200)
        )

        screen.blit(
            background,
            (
                message_rect.x - 15,
                message_rect.y - 10
            )
        )

        screen.blit(
            message,
            message_rect
        )

    # HUD
    title_font = pygame.font.Font(None, 30)
    stat_font = pygame.font.Font(None, 25)

    padding = 15

    bar_x = 85
    bar_width = 125
    bar_height = 14

    row_gap = 30


    # -------------------------
    # Text we need to display
    # -------------------------

    title = title_font.render(
        job.title,
        True,
        (255, 255, 255)
    )

    job_info = stat_font.render(
        f"Level {job.level}   Salary: NGN {job.salary}",
        True,
        (220, 220, 220)
    )

    time_text = stat_font.render(
        game_time.get_time(),
        True,
        (255, 255, 255)
    )

    food_text = stat_font.render(
        f"Food: {player.food}",
        True,
        (255, 255, 255)
    )

    money_text = stat_font.render(
        f"NGN {player.money}",
        True,
        (255, 220, 100)
    )


    # -------------------------
    # Work out positions
    # -------------------------

    title_y = padding

    job_info_y = (
        title_y
        + title.get_height()
        + 4
    )

    time_y = (
        job_info_y
        + job_info.get_height()
        + 8
    )

    stats_start_y = (
        time_y
        + time_text.get_height()
        + 15
    )

    hunger_y = stats_start_y
    energy_y = hunger_y + row_gap
    hygiene_y = energy_y + row_gap
    health_y = hygiene_y + row_gap

    food_y = (
        health_y
        + stat_font.get_height()
        + 12
    )

    money_y = (
        food_y
        + food_text.get_height()
        + 5
    )


    # -------------------------
    # Let the height fit content
    # -------------------------

    hud_height = (
        money_y
        + money_text.get_height()
        + padding
    )


    # Width needs to fit the longest content
    hud_width = max(
        230,
        bar_x + bar_width + padding,
        title.get_width() + padding * 2,
        job_info.get_width() + padding * 2,
        food_text.get_width() + padding * 2,
        money_text.get_width() + padding * 2,
    )


    # -------------------------
    # Create HUD
    # -------------------------

    hud_surface = pygame.Surface(
        (hud_width, hud_height),
        pygame.SRCALPHA
    )

    # Semi-transparent background
    hud_surface.fill(
        (20, 20, 20, 180)
    )


    # -------------------------
    # Draw title
    # -------------------------

    hud_surface.blit(
        title,
        (padding, title_y)
    )


    # Job information
    hud_surface.blit(
        job_info,
        (padding, job_info_y)
    )


    # Time
    hud_surface.blit(
        time_text,
        (padding, time_y)
    )


    # -------------------------
    # Helper for stat bars
    # -------------------------

    def draw_stat(surface, name, value, y):

        label = stat_font.render(
            name,
            True,
            (255, 255, 255)
        )

        surface.blit(
            label,
            (padding, y)
        )

        # Bar background
        bar_y = y + 3

        pygame.draw.rect(
            surface,
            (60, 60, 60),
            (
                bar_x,
                bar_y,
                bar_width,
                bar_height
            ),
            border_radius=5
        )

        # Bar value
        fill_width = int(
            bar_width * (value / 100)
        )

        pygame.draw.rect(
            surface,
            (90, 200, 100),
            (
                bar_x,
                bar_y,
                fill_width,
                bar_height
            ),
            border_radius=5
        )


    # -------------------------
    # Stats
    # -------------------------

    draw_stat(
        hud_surface,
        "Hunger",
        player.hunger,
        hunger_y
    )

    draw_stat(
        hud_surface,
        "Energy",
        player.energy,
        energy_y
    )

    draw_stat(
        hud_surface,
        "Hygiene",
        player.hygiene,
        hygiene_y
    )

    draw_stat(
        hud_surface,
        "Health",
        player.health,
        health_y
    )


    # -------------------------
    # Food
    # -------------------------

    hud_surface.blit(
        food_text,
        (padding, food_y)
    )


    # -------------------------
    # Money
    # -------------------------

    hud_surface.blit(
        money_text,
        (padding, money_y)
    )


    # -------------------------
    # Put HUD on screen
    # -------------------------

    screen.blit(
        hud_surface,
        (15, 15)
    )
    pygame.display.flip()


pygame.quit()