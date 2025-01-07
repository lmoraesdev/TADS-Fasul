# Changelog

Todas as mudanças importantes serão documentadas neste arquivo.

## [1.1.1] - 2025-01-07

### Adicionado na versão 1.1.1

- **Refatoração do pipeline **`ci-pipeline.yml`** para incluir etapas de lint e testes com melhor configuração.**
  - Criação dos arquivos **`init.py`** para adequação do ambiente de testes.
  - Configuração do **`pytest.ini`** para padronizar a execução dos testes com suporte ao modo de importação importlib.

## [1.1.0] - 2024-12-24

### Adicionado na versão 1.1.0

- **Separação de responsabilidades em workflows independentes**:
  - **`ci-pipeline.yml`**: Workflow focado em lint, testes e verificações rápidas.
  - **`security-scan.yml`**: Workflow dedicado a verificações de segurança utilizando ferramentas como Trivy e OWASP Dependency-Check.
  - **`code-quality.yml`**: Workflow voltado para análise estática e qualidade do código.

Essas mudanças visam melhorar a modularidade do pipeline CI/CD, permitindo uma execução mais eficiente das diferentes tarefas de forma isolada.

### Alterado

- **Organização do pipeline CI/CD**: A estrutura de integração contínua foi modificada para separar as responsabilidades em workflows distintos. Isso melhora a clareza e a manutenção dos processos de verificação de segurança, qualidade do código e testes rápidos.

- **Organização do Algoritmos-e-Programacao**: A estrutura das pasta de exercicios agora tem o teste separado.

### Removido

- Nenhuma remoção ainda.

## [1.0.0] - 2024-12-22

### Adicionado na versão 1.0.0

- Primeira versão do projeto.
- Estrutura de repositório organizada com templates para PR e Feature Request.

### Alterado versão 1.0.0

- Organizado o código de forma modular.

### Removido versão 1.0.0

- Nenhuma remoção ainda.

## [0.1.0] - 2024-12-20

### Adicionado

- Criação do repositório e arquivos iniciais.
