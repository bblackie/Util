#!/usr/bin/env python3
import os
import fnmatch
import argparse
import sys


'''
How to Use the New Features:

To see what patterns are being loaded:
python audit.py -v

To see which paths are being ignored:
python audit.py --show-ignored -r

Example patterns for directories in your fileignore file:
# Ignores the "node_modules" directory and all its contents
node_modules/

# Ignores all "build" directories anywhere in the tree
**/build/

# Ignores specific directories by path
.git/
__pycache__/


'''


def load_ignore_patterns(ignore_file_path):
    """Load patterns from the ignore file, similar to .gitignore format."""
    if not os.path.exists(ignore_file_path):
        print(f"Warning: Ignore file '{ignore_file_path}' not found.")
        return []
    
    patterns = []
    with open(ignore_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
                
            # Normalize directory separators
            line = line.replace('\\', '/')
            
            # Handle negation patterns (lines starting with !)
            if line.startswith('!'):
                # We'll implement this as a future enhancement if needed
                # For now, just skip negation patterns
                continue
                
            patterns.append(line)
    
    return patterns


def should_ignore(path, ignore_patterns, is_dir=False):
    """Check if a path should be ignored based on the ignore patterns."""
    # Get the basename and normalized path for matching
    basename = os.path.basename(path)
    normalized_path = path.replace('\\', '/')
    
    for pattern in ignore_patterns:
        original_pattern = pattern
        
        # Handle directory-specific patterns (ending with /)
        if pattern.endswith('/'):
            if not is_dir:  # Only apply directory patterns to directories
                continue
            pattern = pattern[:-1]  # Remove trailing slash for matching
        
        # Match against basename
        if fnmatch.fnmatch(basename, pattern):
            return True
            
        # Match against full path
        if fnmatch.fnmatch(normalized_path, pattern):
            return True
        
        # For directories, also check if any parent pattern matches
        if is_dir:
            # Check for pattern like "node_modules/**" or "node_modules/*"
            if original_pattern.endswith('/**') or original_pattern.endswith('/*'):
                dir_pattern = original_pattern.split('/*')[0].split('/**')[0]
                if basename == dir_pattern or normalized_path.endswith('/' + dir_pattern):
                    return True
    
    return False


def list_files(directory, ignore_patterns, recursive=True):
    """List files in the directory that don't match any ignore patterns."""
    files_list = []
    
    for root, dirs, files in os.walk(directory):
        # Filter out ignored directories to prevent recursion into them
        if recursive:
            dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns, is_dir=True)]
        
        # Filter files
        for file in files:
            file_path = os.path.join(root, file)
            if not should_ignore(file_path, ignore_patterns, is_dir=False):
                files_list.append(file_path)
        
        # If not recursive, break after the first iteration
        if not recursive:
            break
    
    return files_list


def list_ignored_paths(directory, ignore_patterns, recursive=True):
    """List paths that ARE being ignored (for debugging purposes)."""
    ignored_list = []
    
    for root, dirs, files in os.walk(directory):
        # Check directories
        for d in dirs[:]:
            dir_path = os.path.join(root, d)
            if should_ignore(dir_path, ignore_patterns, is_dir=True):
                ignored_list.append((dir_path, "directory"))
        
        # Check files
        for file in files:
            file_path = os.path.join(root, file)
            if should_ignore(file_path, ignore_patterns, is_dir=False):
                ignored_list.append((file_path, "file"))
        
        # If not recursive, break after the first iteration
        if not recursive:
            break
    
    return ignored_list

def count_non_empty_lines(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # This checks if the line is non-empty after stripping whitespace
                count += 1
    return count

def main():
    print("Command line arguments received:")
    print(f"sys.argv: {sys.argv}")
    
    print("\nAttempting to parse arguments:")
    parser = argparse.ArgumentParser(description='Debug command line arguments')
    parser.add_argument('-d', '--directory', default='.', help='Directory to start searching')
    parser.add_argument('-i', '--ignore-file', default='ignore_file', help='Path to ignore file')
    parser.add_argument('-r', '--recursive', action='store_true', help='Search recursively through subdirectories')
    parser.add_argument('--show-ignored', action='store_true', help='Show ignored paths instead of showing included files')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show more information, including loaded ignore patterns')
    
    try:
        args = parser.parse_args()
        
        # Load ignore patterns
        ignore_patterns = load_ignore_patterns(args.ignore_file)
        
        if args.verbose:
            print("Loaded ignore patterns:")
            for pattern in ignore_patterns:
                print(f"  - {pattern}")
            print()
        
        if args.show_ignored:
            # List ignored paths
            ignored = list_ignored_paths(args.directory, ignore_patterns, args.recursive)
            
            if ignored:
                print("Ignored paths:")
                for path, path_type in sorted(ignored):
                    print(f"  {path} ({path_type})")
                print(f"\nTotal ignored: {len(ignored)}")
            else:
                print("No paths are being ignored.")
        else:
            # List files
            files = list_files(args.directory, ignore_patterns, args.recursive)
            
            total_lines = 0
            # Print results
            for file_path in sorted(files):
                print(f"Counting non-empty lines in: {file_path}")
                line_count = count_non_empty_lines(file_path)
                total_lines += line_count
                print(f"{file_path} ({line_count} lines)")
            
            print(f"\nTotal lines counted: {total_lines}")
            print(f"Total files listed: {len(files)}\n")
    except SystemExit as e:
        print("\nError with command-line arguments.")
        print("Make sure you're using the correct format:")
        print("  python script.py [-d DIRECTORY] [-i IGNORE_FILE] [-r]")
        print("\nFor help, use: python script.py --help")


if __name__ == "__main__":
    main()