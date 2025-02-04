# MCP Config Manager

Configuration management utilities for Model Context Protocol (MCP) servers. This package provides functionality to manage MCP server configurations for different clients like Claude Desktop and VSCode extensions (Cline and Roo).

## Features

- Automatic configuration file path detection for different environments
- Support for Claude Desktop and VSCode extensions (Cline and Roo)
- Environment variable validation
- Generic configuration management functions
- VSCode extension specific settings (disabled, autoApprove) for Cline and Roo

## Installation

```bash
pip install mcp-config-manager
```

## Usage

```python
from mcp_config_manager import add_to_config

# Define your required environment variables
REQUIRED_ENV_VARS = ["API_KEY", "API_URL"]

# Add to Claude Desktop configuration
add_to_config(
    server_name="my-mcp-server",
    required_env_vars=REQUIRED_ENV_VARS,
    config_type="claude"
)

# Add to Cline configuration (VSCode extension)
add_to_config(
    server_name="my-mcp-server",
    required_env_vars=REQUIRED_ENV_VARS,
    config_type="cline"  # Will include disabled=False and autoApprove settings
)

# Add to Roo configuration (VSCode extension)
add_to_config(
    server_name="my-mcp-server",
    required_env_vars=REQUIRED_ENV_VARS,
    config_type="roo"  # Will include disabled=False and autoApprove settings
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

### Claude Desktop
- EC2: `~/.vscode-server/data/User/globalStorage/anthropic.claude/settings/claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

### VSCode Extensions

#### Cline
- EC2: `~/.vscode-server/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- macOS: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- Windows: `%APPDATA%/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

#### Roo
- EC2: `~/.vscode-server/data/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json`
- macOS: `~/Library/Application Support/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json`
- Windows: `%APPDATA%/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json`

## VSCode Extension Settings

When adding configurations for VSCode extensions (Cline or Roo), the following additional settings are automatically included:

```json
{
  "disabled": false,  // Server is enabled by default
  "autoApprove": []  // List of operations to auto-approve
}
```

## Development

1. Clone the repository
2. Install development dependencies: `pip install -e ".[dev]"`
3. Run tests: `pytest`
4. Submit pull requests

## License

MIT License - see LICENSE file for details.
