"""MCP Config Manager - Configuration management utilities for MCP servers.

This package provides functionality to manage MCP server configurations for different
clients like Cline and Claude Desktop.
"""

import json
import os
import sys
import getpass
from pathlib import Path
from typing import Dict, List, Optional

__version__ = "0.1.0"

def get_cline_config_path() -> Path:
    """Determine the appropriate Cline configuration file path based on the environment.
    
    Returns:
        Path: The path to the Cline configuration file
    """
    if getpass.getuser() == 'ec2-user':
        return Path.home() / ".vscode-server/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"
    elif sys.platform == 'darwin':
        return Path.home() / "Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"
    
    # Default to EC2 path for any other case
    return Path.home() / ".vscode-server/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"

def get_claude_config_path() -> Path:
    """Determine the appropriate Claude Desktop configuration file path based on the environment.
    
    Returns:
        Path: The path to the Claude Desktop configuration file
    """
    if getpass.getuser() == 'ec2-user':
        return Path.home() / ".vscode-server/data/User/globalStorage/anthropic.claude/settings/claude_desktop_config.json"
    elif sys.platform == 'darwin':
        return Path.home() / "Library/Application Support/Claude/claude_desktop_config.json"
    elif sys.platform == 'win32':
        return Path(os.getenv('APPDATA', '')) / "Claude/claude_desktop_config.json"
    
    # Default to EC2 path for any other case
    return Path.home() / ".vscode-server/data/User/globalStorage/anthropic.claude/settings/claude_desktop_config.json"

def add_to_config(
    server_name: str,
    required_env_vars: List[str],
    command: str = "uvx",
    env_vars: Optional[Dict[str, str]] = None,
    config_type: str = "cline"
) -> None:
    """Add an MCP server configuration to the specified config file.
    
    Args:
        server_name: Name of the MCP server
        required_env_vars: List of required environment variable names
        command: Command to run the server (default: "uvx")
        env_vars: Optional dict of environment variables to use instead of current env
        config_type: Type of config file ("cline" or "claude")
        
    Raises:
        ValueError: If config_type is invalid or required environment variables are missing
    """
    if config_type not in ["cline", "claude"]:
        raise ValueError("config_type must be 'cline' or 'claude'")
        
    # Get config file path
    settings_path = get_cline_config_path() if config_type == "cline" else get_claude_config_path()
    
    # Load existing settings
    try:
        with open(settings_path) as f:
            settings = json.load(f)
    except FileNotFoundError:
        settings = {"mcpServers": {}}
    
    # Use provided env vars or get from environment
    env = env_vars or {var: os.getenv(var) for var in required_env_vars}
    
    # Validate required environment variables
    missing_vars = [var for var in required_env_vars if not env.get(var)]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Create server configuration
    server_config = {
        "command": command,
        "args": [server_name],
        "env": env
    }
    
    # Add Cline-specific settings
    if config_type == "cline":
        server_config.update({
            "disabled": True,
            "autoApprove": []
        })
    
    # Add/update server configuration
    settings["mcpServers"][server_name] = server_config
    
    # Write updated settings
    os.makedirs(settings_path.parent, exist_ok=True)
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    
    print(f"Added {server_name} server configuration to {settings_path}")
