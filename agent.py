import subprocess

def run_in_sandbox(command):
    """Run a command inside the sealed box and return the output."""
    # Start a temporary container, run the command, then delete the container
    result = subprocess.run(
        [
            "docker", "run", "--rm",
            "-v", f"{subprocess.check_output(['pwd']).decode().strip()}:/workspace",
            "coding-sandbox:latest",
            "bash", "-c", command
        ],
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr

# Test it
print("Testing the sealed box from Python...\n")

output, error = run_in_sandbox("python3 --version")
print("Python version inside the box:")
print(output)

output, error = run_in_sandbox("echo 'Hello from inside the sealed box'")
print("Message from the box:")
print(output)
