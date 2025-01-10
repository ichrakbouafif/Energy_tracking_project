#This is just an example to test codecarbon

from codecarbon import EmissionsTracker

# Initialize the emissions tracker
tracker = EmissionsTracker(project_name="Test Project")

# Start tracking emissions
tracker.start()

# Sample computation (e.g., calculating squares of numbers)
results = [i ** 2 for i in range(1000000)]

# Stop tracking emissions
tracker.stop()
