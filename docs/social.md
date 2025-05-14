# Social Media Integration

The Solentra package provides social media integration capabilities through the `SocialMediaTools` class, allowing agents to interact with Twitter for research updates and engagement analysis.

## Installation

```bash
pip install solentra
```

## Basic Usage

```python
from solentra import SolentraAgent

# Initialize agent with Twitter configuration
twitter_config = {
    'api_key': 'your_api_key',
    'api_secret': 'your_api_secret',
    'access_token': 'your_access_token',
    'access_token_secret': 'your_access_token_secret'
}

agent = SolentraAgent(twitter_config=twitter_config)
```
