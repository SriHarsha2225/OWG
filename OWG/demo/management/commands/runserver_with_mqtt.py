# your_app/management/commands/runserver_with_mqtt.py
import subprocess
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    help = 'Run Django development server and MQTT client'

    def handle(self, *args, **options):
        mqtt_script = 'demo/mqtt_file.py'  # Replace with the actual path to your mqtt_client.py script
        mqtt_process = subprocess.Popen(['python', mqtt_script])

        super().handle(*args, **options)

        # Optionally, you can add code to gracefully stop the MQTT client when the server is shut down.
        mqtt_process.terminate()


