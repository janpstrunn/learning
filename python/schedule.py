import random

def generate_schedule(primary_topics, secondary_activities, tasks):
    days = 7
    schedule = []

    # Initialize counters to track usage
    primary_topic_count = {topic: 0 for topic in primary_topics}
    secondary_activity_count = {activity: 0 for activity in secondary_activities}
    task_count = {task: 0 for task in tasks}

    def is_valid_pair(pair, day_schedule):
        primary_topic, secondary_activity, task = pair
        if (primary_topic in [p for p, _, _ in day_schedule] or 
            secondary_activity in [s for _, s, _ in day_schedule] or 
            task in [t for _, _, t in day_schedule]):
            return False
        if schedule and (
            primary_topic in [p for p, _, _ in schedule[-1:]] or
            secondary_activity in [s for _, s, _ in schedule[-1:]] or
            task in [t for _, _, t in schedule[-1:]]):
            return False
        return True

    def get_least_used_item(item_count):
        min_count = min(item_count.values())
        least_used_items = [item for item, count in item_count.items() if count == min_count]
        return random.choice(least_used_items)

    for day in range(days):
        day_schedule = []
        attempts = 0

        while len(day_schedule) < 1 and attempts < 100:
            primary_topic = get_least_used_item(primary_topic_count)
            secondary_activity = get_least_used_item(secondary_activity_count)
            task = get_least_used_item(task_count)
            pair = (primary_topic, secondary_activity, task)

            if is_valid_pair(pair, day_schedule):
                day_schedule.append(pair)
                primary_topic_count[primary_topic] += 1
                secondary_activity_count[secondary_activity] += 1
                task_count[task] += 1

            attempts += 1

        if len(day_schedule) == 0:
            print("Failed to generate a valid schedule. Try again.")
            return None

        schedule.append(day_schedule[0])

    return schedule

def print_schedule_md(schedule):
    headers = ["Day", "Topic", "Project", "Activity"]
    table = [headers]

    for day, (primary_topic, secondary_activity, task) in enumerate(schedule):
        day_str = f"Day {day + 1}"
        table.append([day_str, primary_topic, secondary_activity, task])

    # Print Markdown table
    md_table = "| " + " | ".join(headers) + " |\n"
    md_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in table[1:]:
        md_table += "| " + " | ".join(row) + " |\n"

    print(md_table)

# Define topics, activities, and tasks
primary_topics = ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"]
secondary_activities = ["Blogging", "Programming", "Improving", "Visualizing", "Gaming"]
tasks = ["Articles", "Rewrite", "Review", "Flashcards", "Self-taught study"]

# Generate and print schedule
schedule = generate_schedule(primary_topics, secondary_activities, tasks)
if schedule:
    print_schedule_md(schedule)
