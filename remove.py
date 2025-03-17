import subprocess

def reset_repository():
    # Remove the .git directory
    subprocess.run(['rm', '-rf', '.git'])
    
    # Reinitialize the repository
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])
    
    # Add remote repository
    remote_url = input("Enter your remote repository URL: ")
    subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
    
    # Force push to overwrite history
    confirm = input("WARNING: This will overwrite the remote history. Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        subprocess.run(['git', 'branch', '-M', 'main'])
        subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'])

if __name__ == '__main__':
    reset_repository()