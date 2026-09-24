class ActionSystem:

    @staticmethod
    def sleep(player, game_time):
        game_time.advance_hours(8)

        player.energy = 100

        player.hunger = min(
            100,
            player.hunger + 20
        )

        player.hygiene = max(
            0,
            player.hygiene - 10
        )

        return "Slept for 8 hours."

    @staticmethod
    def eat(player):
        if player.food <= 0:
            return "You have no food."

        player.food -= 1

        player.hunger = max(
            0,
            player.hunger - 30
        )

        return "You ate a meal."

    @staticmethod
    def shower(player):
        player.hygiene = 100

        return "You took a shower."

    @staticmethod
    def buy_food(player, shop):
        
        if player.money < shop.food_price:
            return "Not enough money."

        player.money -= shop.food_price
        player.food += 1

        return f"Bought food. Food: {player.food}"

    @staticmethod
    def work(player, job, game_time):
        if not job.can_work(game_time):

            hour = game_time.get_hour()

            if hour < 8:
                return "Work starts at 8:00 AM."

            if hour >= 17:
                return "Work is finished for today."

            return "You already worked today."

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

        return job.work(
            player,
            game_time
        )