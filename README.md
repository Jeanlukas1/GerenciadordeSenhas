# Gerenciador de Senhas (MVC)

## Executar o projeto
```bash
python main.py
```

## Estrutura
- models: entidades do sistema
- views: interação com usuário
- controllers: regras de negócio
- dals: acesso a dados (arquivo)

## Imports


```bash
main → view → controller → model → dal
```

| Camada     | Pode importar |
| ---------- | ------------- |
| main       | view          |
| view       | controller    |
| controller | model, dal    |
| dal        | model         |
| model      | ninguém       |

