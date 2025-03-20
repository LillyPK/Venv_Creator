import os
import subprocess
import platform
import sys
import shutil

def create_project():
    """Create a new Python project with virtual environment."""
    project_name = input("Enter project name: ").strip()
    
    if not project_name:
        print("Project name cannot be empty.")
        return
    
    # Store the script's directory path
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Create project directory
    try:
        os.makedirs(project_name)
        print(f"Created project directory: {project_name}")
    except FileExistsError:
        print(f"Directory '{project_name}' already exists.")
        if input("Continue anyway? (y/n): ").lower() != 'y':
            return
    
    # Change to project directory
    os.chdir(project_name)
    
    # Create virtual environment
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    
    # Create initial files
    with open("main.py", "w") as f:
        f.write('def main():\n    print("Hello, World!")\n\nif __name__ == "__main__":\n    main()')
    
    with open("README.md", "w") as f:
        f.write(f"# {project_name}\n\nA Python project.")
    
    # Copy activate.bat file from script directory
    if platform.system() == "Windows":
        source_bat = os.path.join(script_directory, "activate.bat")
        if os.path.exists(source_bat):
            shutil.copy(source_bat, "activate.bat")
            print("Copied activate.bat file from script directory")
        else:
            print("Warning: activate.bat not found in script directory")
    else:
        # For non-Windows, copy activate.sh if available, otherwise create it
        source_sh = os.path.join(script_directory, "activate.sh")
        if os.path.exists(source_sh):
            shutil.copy(source_sh, "activate.sh")
            os.chmod("activate.sh", 0o755)  # Make executable
            print("Copied activate.sh file from script directory")
        else:
            print("Warning: activate.sh not found in script directory")
    
    print(f"Project '{project_name}' created successfully.")
    
    # Open VS Code
    print("Opening VS Code...")
    if platform.system() == "Windows":
        subprocess.Popen(["cmd", "/c", "code", "."])
    else:
        subprocess.Popen(["code", "."])

def main():
    print("Python Project Manager")
    print("-" * 30)
    print("1. Create a new project")
    print("-" * 30)
    
    choice = input("Enter your choice (1): ").strip()
    
    if choice == "1":
        create_project()
    else:
        print("Invalid choice. Please select 1.")

if __name__ == "__main__":
    main()