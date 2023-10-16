import subprocess

try:
    server_process = subprocess.Popen("python manage.py runserver", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the server to start
    print("Django server is starting...")

    # Get the host and port from the subprocess output
    output = server_process.stdout.read().decode('utf-8')
    host = '127.0.0.1'  # Default host
    port = '8000'  # Default port

    # Parse the output to extract host and port information
    for line in output.split('\n'):
        if 'Starting development server' in line:
            parts = line.split(' at ')
            if len(parts) > 1:
                address_parts = parts[1].split(':')
                if len(address_parts) > 1:
                    host = address_parts[0]
                    port = address_parts[1]

    # Print the full address
    print(f"Django server is running at http://{host}:{port}")

    # Wait for the server process to finish (e.g., when you manually stop it)
    server_process.wait()

except KeyboardInterrupt:
    print("Server stopped.")
