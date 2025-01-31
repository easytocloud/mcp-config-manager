# MCP Config Manager

Configuration management utilities for Model Context Protocol (MCP) servers. This package provides functionality to manage MCP server configurations for different clients like Cline and Claude Desktop.

## Features

- Automatic configuration file path detection for different environments
- Support for both Cline and Claude Desktop configurations
- Environment variable validation
- Generic configuration management functions

## Installation

```bash
pip install mcp-config-manager
```

## Usage

```python
from mcp_config_manager import add_to_config

# Define your required environment variables
REQUIRED_ENV_VARS = ["API_KEY", "API_URL"]

# Add to Cline configuration
add_to_config(
    server_name="my-mcp-server",
    required_env_vars=REQUIRED_ENV_VARS,
    config_type="cline"
)

# Add to Claude Desktop configuration
add_to_config(
    server_name="my-mcp-server",
    required_env_vars=REQUIRED_ENV_VARS,
    config_type="claude"
)

# With custom environment variables
env_vars = {
    "API_KEY": "my-key",
    "API_URL": "https://api.example.com"
}

add_to_config(
    server_name="my-mcp-server",
    required_env_vars=REQUIRED_ENV_VARS,
    env_vars=env_vars,
    config_type="cline"
)
```

## Configuration File Locations

The package automatically detects the appropriate configuration file paths:

### Cline
- EC2: `~/.vscode-server/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- macOS: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

### Claude Desktop
- EC2: `~/.vscode-server/data/User/globalStorage/anthropic.claude/settings/claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

## Development

1. Clone the repository
2. Install development dependencies: `pip install -e ".[dev]"`
3. Run tests: `pytest`
4. Submit pull requests

## License

MIT License - see LICENSE file for details.
