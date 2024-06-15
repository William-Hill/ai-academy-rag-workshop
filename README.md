Dream Machine AI Academy: Build Your Personal ChatGPT with Python, LangChain, and Ollama

## Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

- **Python**: Ensure you have Python 3.10.x or above installed. It's recommended to use `pyenv` to manage Python versions if necessary.
- **Ollama**: You need to download and start the Ollama server.

## Download and start Ollama

Download [Ollama](https://ollama.com/) for your operating system.

Once downloaded, start Ollama 

```bash
ollama serve
```

Download the Llama3 model

```bash
ollama pull llama3
```

Download nomic text embeddings

```bash
ollama pull nomic-embed-text
```

### Installing Python with pyenv

If you don't have Python 3.10.x installed, you can use `pyenv` to manage your Python versions.

1. **Install pyenv**:

   ```bash
   curl https://pyenv.run | bash

   ```

2. **Add pyenv to PATH**: 

For Bash users

```bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc && echo 'eval "$(pyenv init --path)"' >> ~/.bashrc && echo 'eval "$(pyenv init -)"' >> ~/.bashrc && echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc && source ~/.bashrc
```

For Zsh users

```bash
,echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc && echo 'eval "$(pyenv init --path)"' >> ~/.zshrc && echo 'eval "$(pyenv init -)"' >> ~/.zshrc && echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc && source ~/.zshrc
```

3. **Install and activate Python 3.10.x**:

```bash
pyenv install 3.10.x
pyenv local 3.10.x
```

4. **Install dependencies**:

```bash
pip install -r requirements.txt
```
