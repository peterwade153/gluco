"""
Utility function to read environments  
which specify environment either local or production
"""
import os


def read_env_file(file_name):
    try:
        with open(os.path.join('environments/', file_name), 'r') as f:
            lines = [line.rstrip('/n').split('=', 1) for line in f]
            for line in lines:
                if line[0] not in os.environ:
                    print(f'Setting env var {line[0]} to {line[1]}')
                    os.environ.setdefault(line[0], line[1])
    except FileNotFoundError:
        print(f'Env file {file_name} not found')
