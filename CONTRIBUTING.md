# Contributing to BookBot

We welcome contributions! Please follow these guidelines to make the process smooth for everyone.

## Code Style

- **Language**: Python 3.11+
- **Formatting**: Use **Black** for automatic formatting. You can run `black .` before committing.
- **Linting**: Follow **PEP 8** conventions. The project includes a flake8 configuration; run `flake8` locally to catch style issues.
- **Type hints**: Add type hints where reasonable. The project uses **mypy** for static type checking.

## Commit Message Conventions

We use the **Conventional Commits** format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

- **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **scope** (optional): the module or area of the codebase the change affects
- **subject**: short description, max 72 characters, imperative mood
- **body** (optional): longer description, wrapped at 72 characters
- **footer** (optional): references to issues or breaking changes

Example:
```
feat(stats): add median calculation

Implemented median function in `stats.py` and added unit tests.

Closes #12
```

## Pull Request Process

1. **Fork** the repository and **clone** your fork.
2. **Create a new branch** for your feature or bug fix (`git checkout -b my-feature`).
3. **Write code** and **add tests** as needed.
4. **Run the test suite**: `pytest` (or the configured test command).
5. **Ensure linting passes**: `black . && flake8 . && mypy .`
6. **Commit** using the Conventional Commits format.
7. **Push** your branch to your fork.
8. Open a **Pull Request** against the `main` branch of this repository.
9. Fill out the PR template, linking any related issues.
10. Wait for CI checks to pass and for reviewers to approve.

### Review Checklist
- Does the PR follow the code style guidelines?
- Are tests included and passing?
- Is the commit history clean (squash/fixup if needed)?
- Is the documentation updated where applicable?

## Getting Help

If you have any questions, feel free to open an issue or ask in the project's discussion board.

Thank you for contributing!