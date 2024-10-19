import random

def generate_schedule(topics, activities):
    days = 7
    topics_per_day = 2
    activities_per_day = 2
    topic_count = {topic: 0 for topic in topics}
    activity_count = {activity: 0 for activity in activities}
    schedule = []

    def is_valid_pair(pair, day_schedule):
        topic, activity = pair
        if topic in [t for t, _ in day_schedule] or activity in [a for _, a in day_schedule]:
            return False
        if schedule and (topic in [t for t, _ in schedule[-1]] or activity in [a for _, a in schedule[-1]]):
            return False
        return True

    for day in range(days):
        day_schedule = []
        attempts = 0

        while len(day_schedule) < topics_per_day and attempts < 100:
            topic = random.choice(topics)
            activity = random.choice(activities)
            pair = (topic, activity)

            if is_valid_pair(pair, day_schedule):
                day_schedule.append(pair)
                topic_count[topic] += 1
                activity_count[activity] += 1

            attempts += 1

        schedule.append(day_schedule)

        if attempts == 100:
            print("Failed to generate a valid schedule. Try again.")
    return schedule

topics = ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"]
activities = ["Articles", "Rewrite", "Review", "Flashcards", "Self-Taught"]

schedule = generate_schedule(topics, activities)
for day, pairs in enumerate(schedule):
    print(f"Day {day + 1}:")
    for topic, activity in pairs:
        print(f"  {topic}: {activity}")

