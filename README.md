# Password Generator CLI

This project is built with the purpose of generating a password which can be customized up to any character length (10 characters by default) with a unique randomness added to each password generated. It can be used to generate a quick password with good security so that the hassle of thinking about passwords that could potentially be weak is resolved.

Source code is available in the [repository](https://github.com/kisaraF/pw-gen-cli) for your reference and modification at your own free will. The directory `src/` holds the relavant content.

Furthermore, the docker image is available in the GitHub Container Registry for you to generate a password without having to focus on installing dependencies. Just simply run the below commands.

**1. Pull the Docker image from `ghcr`**

```bash
docker pull ghcr.io/kisaraf/pwgen-cli:latest
```

**2. Generate a password**

```bash
docker run -it pwgen-cli:<tag> pwdgen gen-password --char_count 20
```

**Helpful Commands**

1. List all available commands
```bash
pwdgen --help
```

2. Generate a password
```bash
pwdgen gen-password --char_count <len>
```
