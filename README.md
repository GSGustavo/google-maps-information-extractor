## Programa com o intuito de fazer buscas de empresas em cidades no google maps e guardar as informações dessas empresas (Nome, telefone, endereço), baseado em web scraping, usando selenium

## Esse script percorre as seguintes categorias em uma cidade:
### Para cada categoria, é extraídas as informações das empresas

- Supermercados
- Oficinas
- Restaurantes
- Lanchonetes
- Informática e Eletrônicos
- Eletrodomésticos
- Roupas
- Papelarias
- Gráficas
- Serviços de Internet
- Farmácias
- Hotéis

## Bibliotecas necessárias

> pyautogui |
> unicodedate |
> selenium |
> help (Desenvolvida por mim, ja esta na pasta)

## Como fazer funcionar?

- Você deve rodar o arquivo main.py e escolher a opção 1
- Após isso, caso queira personalizar quais categorias gostaria de buscar em uma cidade, basta digitar 0, caso não, digite 1
- O programa vem com cidades pré-cadastradas, porém você pode edita-las na linha 20 (Ignore a linha 23) do arquivo main.py
- Para adicionar mais cidades, recomendo buscar como o nome dela esta escrito no google maps, e adicionar/colar na lista da linha 20

## Observações (Importantes)

- O script conta com vários prints no console para debbuging, acabei não retirando pois pode lhe ajudar a entender com funciona
- O programa não funciona sem um webdriver, no caso, o script foi pensado e executado no chromedriver, no repositório, você ja encontra um, porém caso apresente erro, va ao site de downloads do chromedriver, e tente baixar a versão que o erro pede (https://chromedriver.chromium.org/downloads)
