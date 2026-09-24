class GameTime:
    def __init__(self):
        self.minutes = 7 * 60  # Start at 7:00 AM

        # How many game minutes pass per real second
        self.speed = 2
        self.day = 1

    def update(self, dt):
        self.minutes += self.speed * dt

        if self.minutes >= 24 * 60:
            days_passed = int(
                self.minutes // (24 * 60)
            )

            self.minutes %= 24 * 60

            self.day += days_passed


    def get_time(self):
        hours = int(self.minutes // 60)
        minutes = int(self.minutes % 60)

        period = "AM"

        if hours >= 12:
            period = "PM"

        display_hour = hours % 12

        if display_hour == 0:
            display_hour = 12

        return f"{display_hour}:{minutes:02d} {period}"

    def get_hour(self):
        return self.minutes / 60

    def advance_hours(self, hours):
        self.minutes += hours * 60

        if self.minutes >= 24 * 60:
            days_passed = int(
                self.minutes // (24 * 60)
            )

            self.minutes %= 24 * 60

            self.day += days_passed