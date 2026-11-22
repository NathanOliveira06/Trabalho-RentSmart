# RentSmart — Sistema de Orçamento de Locação

Projeto em Python para calcular orçamentos de locação da R.M Imóveis.

## Arquivos
- `rentsmart.py`: código principal do sistema.
- `projecao_rentsmart.csv`: exemplo de arquivo de projeção. Ao executar o programa, um novo CSV será gerado com os dados informados.
- `parte_teorica.pdf`: documentação da parte teórica.

## Como executar
1. Instale o Python 3, caso ainda não esteja instalado.
2. Abra a pasta do projeto no VS Code ou em outro editor.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python rentsmart.py
```

5. Responda às perguntas apresentadas no terminal.
6. Ao final, o programa exibirá o orçamento e criará o arquivo `projecao_rentsmart.csv` na mesma pasta.

## Regras implementadas
- Apartamento de 1 quarto: R$ 700,00.
- Apartamento de 2 quartos: R$ 900,00.
- Casa de 1 quarto: R$ 900,00.
- Casa de 2 quartos: R$ 1.150,00.
- Estúdio: R$ 1.200,00.
- Vaga para casa ou apartamento: adicional de R$ 300,00 por mês.
- Estúdio: pacote inicial de 2 vagas por R$ 250,00; cada vaga além das duas custa R$ 60,00.
- Apartamento sem crianças: desconto de 5% sobre o aluguel após os adicionais.
- Taxa contratual: R$ 2.000,00, parcelada em até 5 vezes.

## Observação
Para estúdios, o programa aceita 0 vagas ou 2 ou mais vagas, pois a regra fornecida descreve o estacionamento como um pacote inicial de duas vagas. A taxa contratual é apresentada separadamente do aluguel e suas parcelas entram na projeção dos meses correspondentes.
