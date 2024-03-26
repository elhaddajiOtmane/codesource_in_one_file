
# SpellSourceCauldron

SpellSourceCauldron is a powerful tool designed to magically concatenate JavaScript files from various nested directories into a single, unified file. Ideal for projects requiring consolidation of JS scripts for analysis, deployment, or any form of processing where merging JS files becomes necessary. This project leverages Python for scripting and Docker for easy and consistent setup and execution across any environment.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11 or later
- Docker

### Installing

1. **Clone the repository**

    ```bash
    git clone https://github.com/elhaddajiotmane/SpellSourceCauldron.git
    cd SpellSourceCauldron
    ```

2. **Build the Docker image**

    Navigate to the project directory and build the Docker image:

    ```sh
    docker build -t spellsourcecauldron .
    ```

3. **Run the container**

    With the Docker image built, you can now run the container. Adjust the volume paths to match your project structure:

    ```sh
    docker run -e START_PATH=/data -e OUTPUT_FILE_PATH=/data/combined.js -v <path/to/your/js/files>:/data spellsourcecauldron
    ```

## Usage

The primary function of SpellSourceCauldron is to search through a specified directory for JavaScript files, concatenating their contents into a single file. This is particularly useful for preparing scripts for certain types of deployment or analysis.

To customize the paths and behavior, modify the environment variables `START_PATH` and `OUTPUT_FILE_PATH` in the Docker run command accordingly.

## Built With

- [Python](https://www.python.org/) - The scripting language used.
- [Docker](https://www.docker.com/) - Containerization platform.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/elhaddajiotmane/SpellSourceCauldron/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **OTMANE ELHADDAJI** - *Initial work* - [elhaddajiotmane](https://github.com/elhaddajiotmane)

See also the list of [contributors](https://github.com/elhaddajiotmane/SpellSourceCauldron/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 

- Hat tip to anyone whose code was used
- Inspiration
- etc

