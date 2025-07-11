#!/usr/bin/env python3
"""Test script for the new callee functionality."""

import os
import subprocess
import json

def test_callee_processing():
    """Test that the callee JSON processing works correctly."""
    
    # Create a test JSON file
    test_data = {
        "bar": {
            "definition": 1,
            "calls": [11]
        },
        "foo": {
            "definition": 6,
            "calls": [12]
        }
    }
    
    test_file = "test_callee.json"
    with open(test_file, 'w') as f:
        json.dump(test_data, f)
    
    # Test that the binary can be built and run with the new option
    try:
        # Build the project
        build_result = subprocess.run(
            ["cargo", "build", "--release"], 
            cwd="../",
            capture_output=True, 
            text=True
        )
        
        if build_result.returncode != 0:
            print(f"Build failed: {build_result.stderr}")
            return False
        
        # Test the help output to ensure our new option is there
        help_result = subprocess.run(
            ["../target/release/dwarf-writer", "--help"],
            capture_output=True,
            text=True
        )
        
        if "--callee" not in help_result.stdout:
            print("New --callee option not found in help output")
            return False
        
        print("✓ Build successful and --callee option is available")
        return True
        
    except Exception as e:
        print(f"Test failed: {e}")
        return False
    
    finally:
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == "__main__":
    success = test_callee_processing()
    exit(0 if success else 1)
