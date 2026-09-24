class Job:
    def __init__(self):
        self.title = "Junior Worker"

        self.level = 1

        # Money earned per work shift
        self.salary = 20

        # Hidden performance score
        self.performance = 50

        # Number of shifts completed
        self.work_days = 0

        # Review every 5 shifts
        self.review_period = 5

    def work(self, player):
        self.work_days += 1

        # Performance depends on how well the character
        # is doing physically.
        if player.energy >= 50:
            self.performance += 5
        else:
            self.performance -= 5

        if player.hunger <= 60:
            self.performance += 3
        else:
            self.performance -= 3

        if player.hygiene >= 50:
            self.performance += 2
        else:
            self.performance -= 2

        self.performance = max(
            0,
            min(100, self.performance)
        )

        # Regular salary
        player.money += self.salary

        # Check for promotion or salary reduction
        if self.work_days % self.review_period == 0:
            return self.review()

        return (
            f"Worked shift. Earned ₦{self.salary}."
        )

    def review(self):

        # Promotion
        if self.performance >= 75:
            self.level += 1

            self.salary = int(
                self.salary * 1.25
            )

            self.performance = 60

            titles = {
                2: "Experienced Worker",
                3: "Senior Worker",
                4: "Supervisor",
                5: "Manager",
            }

            self.title = titles.get(
                self.level,
                "Senior Manager"
            )

            return (
                f"PROMOTION! You are now "
                f"{self.title}. "
                f"Salary: ₦{self.salary}"
            )

        # Salary reduction
        if self.performance <= 30:
            self.salary = max(
                5,
                int(self.salary * 0.85)
            )

            self.performance = 40

            return (
                f"Salary reduced to "
                f"₦{self.salary}."
            )

        # No major change
        self.performance = 50

        return (
            "Work review completed. "
            "Salary unchanged."
        )