# Security Policy

## Reporting Vulnerabilities

If you discover a security vulnerability in ProvChart documentation or examples, please report it responsibly:

- Do not create public GitHub issues for security vulnerabilities
- Contact the maintainers directly
- Provide details of the vulnerability
- Allow time for a fix before public disclosure

## API Keys

- Never commit API keys to repositories
- Use environment variables for keys
- Rotate keys regularly
- The ProvChart API uses `X-API-Key` header authentication

## Content Security

- ProvChart charts are pure CSS with no JavaScript execution
- No external scripts are required in compiled mode
