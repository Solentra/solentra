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

## Twitter Features

### Posting Tweets

```python
# Basic tweet
tweet = agent.post_tweet("Research update: New findings in quantum biology!")

# Tweet with media
tweet_with_media = agent.post_tweet(
    "Check out our latest results!",
    media_paths=["results_graph.png"]
)

# Tweet with hashtags
tweet_with_hashtags = agent.post_tweet(
    "Exciting quantum biology results! #Science #Research",
    hashtags=["quantum", "biology"]
)
```

### Scheduling Tweets

```python
from datetime import datetime, timedelta

# Schedule future tweet
future = datetime.now() + timedelta(days=1)
scheduled = agent.schedule_tweet(
    "Join our seminar tomorrow!",
    scheduled_time=future,
    hashtags=["seminar", "science"]
)
```
