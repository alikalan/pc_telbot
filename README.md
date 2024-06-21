# PistachioCrawler Telegram Bot

Welcome to the PistachioCrawler Telegram Bot repository! This bot allows users to check the availability of the product "KoRo Pistazienschnitte mit 45 % Pistazie" in DM branches through Telegram.

## Overview

This project consists of two main components:
1. **Telegram Bot** (this repository) - Handles user interactions on Telegram.
2. **API** ([pistachio-crawler repository](https://github.com/alikalan/pistachio-crawler)) - Scrapes data from the DM online shop to check product availability.

## Features

- Interact with users via Telegram.
- Check the availability of the specified product in various DM branches.
- Provide real-time updates to users.

## Installation

### Prerequisites

- Python 3.10+
- pip (Python package installer)
- Docker (optional, for containerized deployment)

### Clone the Repository

```bash
git clone https://github.com/alikalan/pc_telbot.git
cd pc_telbot
```

### Install Dependencies

```bash
make install
```

## Usage

### Running the Bot

To run the bot, execute:

```bash
make run
```

### Webhook Setup (Optional)

If you want to set up the bot with a webhook, configure the `webhook.py` file and run:

```bash
make webhook
```

## Docker Deployment

### Build the Docker Image

```bash
make docker_build
```

### Run the Docker Container

```bash
make docker_run
```

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Related Projects

- [PistachioCrawler API](https://github.com/alikalan/pistachio-crawler) - The API that scrapes DM's online shop to check product availability.
