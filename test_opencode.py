#!/usr/bin/env python3
"""
Test script to verify OpenCode integration works with Claude Code Agent Farm
"""

import subprocess
import sys
import tempfile
import os

def test_opencode_basic():
    """Test basic OpenCode functionality"""
    print("Testing OpenCode basic functionality...")
    
    # Test if OpenCode is available
    result = subprocess.run(["opencode", "--version"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ OpenCode not available")
        return False
    
    print(f"✅ OpenCode version: {result.stdout.strip()}")
    
    # Test if OpenCode can use GPT-4.1
    result = subprocess.run([
        "opencode", "run", 
        "--model", "github-copilot/gpt-4.1", 
        "What is 2+2?"
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ OpenCode GPT-4.1 test failed: {result.stderr}")
        return False
    
    if "4" in result.stdout:
        print("✅ OpenCode GPT-4.1 working correctly")
        return True
    else:
        print(f"❌ OpenCode GPT-4.1 unexpected response: {result.stdout}")
        return False

def test_agent_factory():
    """Test the AgentFactory with OpenCode"""
    print("\nTesting AgentFactory with OpenCode...")
    
    try:
        from agents import AgentFactory
        agent = AgentFactory.create_agent("open_code")
        
        # Test detection
        detection = agent.detect("test context")
        if detection.get("agent") == "OpenCode":
            print("✅ OpenCode agent detection working")
        else:
            print(f"❌ OpenCode agent detection failed: {detection}")
            return False
            
        # Test control
        control = agent.control("test command")
        if control.get("agent") == "OpenCode":
            print("✅ OpenCode agent control working")
        else:
            print(f"❌ OpenCode agent control failed: {control}")
            return False
            
        return True
    except Exception as e:
        print(f"❌ AgentFactory test failed: {e}")
        return False

def test_config_format():
    """Test config file format for OpenCode"""
    print("\nTesting config file format...")
    
    config_file = "configs/opencode_test_config.json"
    if not os.path.exists(config_file):
        print(f"❌ Config file not found: {config_file}")
        return False
    
    try:
        import json
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        if config.get("agent_type") == "open_code":
            print("✅ OpenCode config format is valid")
            return True
        else:
            print(f"❌ Config missing agent_type: {config.get('agent_type')}")
            return False
    except Exception as e:
        print(f"❌ Config file test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing OpenCode integration with Claude Code Agent Farm\n")
    
    tests = [
        test_opencode_basic,
        test_agent_factory,
        test_config_format
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                print()
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            print()
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All tests passed! OpenCode integration is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. OpenCode integration needs attention.")
        return 1

if __name__ == "__main__":
    sys.exit(main())