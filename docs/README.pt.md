<!-- language-bar -->
[English](../README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · **Português** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)
<!-- /language-bar -->

# PC Hardware Advisor

> Tradução automática, não revisada por um humano. A versão em inglês ([../README.md](../README.md)) prevalece. Correções são bem-vindas, veja [../CONTRIBUTING.md](../CONTRIBUTING.md).

PC Hardware Advisor é um plugin para o Claude (Claude Code e Cowork no aplicativo desktop do Claude) que torna o Claude confiável em hardware de PC de mesa. Ele encontra o melhor preço entregue de uma peça em qualquer lugar do mundo, verifica se as peças funcionam juntas, monta configurações completas para um uso e um orçamento, dimensiona máquinas para IA local, avalia anúncios de segunda mão e acompanha preços em uma agenda. Cada valor informado é datado, tem fonte e recebe uma classificação de confiança, e o plugin apenas lê: ele nunca compra nada e nunca entra em contato com um vendedor.

O Claude responde no idioma em que você escreve. Nomes de peças, SKUs e unidades permanecem como publicados.

## O que ele faz

Seis skills e um subagente.

- **`hunt-prices`**: encontra o melhor preço entregue (com IVA, impostos de importação e frete) para um item exato, em todo o mundo. Lojas diretas aparecem primeiro, os marketplaces são listados separadamente, e cada linha traz uma coluna de confiança. Ele usa o agente `price-scout` para ler vários sites em paralelo.
- **`check-compatibility`**: dá vereditos em pares entre peças: compatível, compatível com condições ou incompatível. Um veredito condicional informa a condição exata e a fonte.
- **`build-config`**: projeta uma montagem completa a partir do uso, do orçamento, do país e das suas restrições. Retorna uma montagem principal, mais uma variante mais barata e uma variante mais potente. Propõe apenas peças novas e peças recondicionadas profissionalmente.
- **`size-local-ai`**: dimensiona hardware para rodar modelos localmente. Cobre VRAM, largura de banda de memória, estimativas de tokens por segundo (rotuladas como estimativas), multi-GPU, APUs, eGPUs e pilhas de software.
- **`review-used-listing`**: analisa um anúncio de segunda mão e retorna um veredito: comprar, negociar ou evitar. Acrescenta perguntas para o vendedor, testes a fazer na entrega e uma margem de negociação.
- **`track-price`**: configura reverificações agendadas de um preço, alerta você apenas quando ele cai abaixo do seu limite e mantém um arquivo de histórico. Nunca compra.
- **`price-scout`** (agente): lê várias páginas de lojas ou marketplaces para uma peça exata e retorna linhas de preço normalizadas, sem análise. O `hunt-prices` o inicia.

Fora do escopo: consoles, smartphones, tablets, notebooks como produtos e qualquer coisa que compre ou entre em contato com vendedores.

## Princípios

- **Todo preço é datado.** Um preço sem data de leitura não é informado.
- **O vendedor é tipado.** Loja direta, vendedor de marketplace, recondicionador e pessoa física são linhas diferentes, nunca misturadas.
- **Preço entregue, ou "sem taxas".** Os preços incluem IVA, impostos de importação e frete até o seu país. Quando um componente não pode ser estabelecido, a linha diz "sem taxas" em vez de chutar.
- **A confiança é exibida.** Cada valor indica o quanto está bem sustentado.
- **Nada é inventado.** Se uma especificação, um preço ou uma regra não puder ser comprovado, o Claude diz isso.
- **Sites bloqueados: recurso ao navegador, nunca artifícios.** Se um site recusar a leitura automatizada e houver uma ferramenta de navegador disponível, o Claude abre por iniciativa própria as poucas páginas que importam no navegador, somente leitura, e informa isso. Ele para diante de qualquer captcha ou verificação de bot e nunca imita um humano para superá-lo. Caso contrário, pede a você uma captura de tela ou texto colado. Não são usados user agents alternativos, caches nem espelhos.
- **Somente leitura.** O plugin nunca compra, nunca cria contas, nunca envia formulários e nunca entra em contato com vendedores. Isso você faz por conta própria.

Dez referências compartilhadas (método de pesquisa, lojas por país, critérios para lojas, compras internacionais, checklist do mercado de usados, soquetes e chipsets, memória, fontes de alimentação e conectores, formatos e gabinetes, largura de banda de GPU para IA) são datadas e têm fonte. Foram revisadas pela última vez em 2026-11-07.

## Instalação

### Claude Code

Use o repositório como marketplace e instale o plugin a partir dele.

```
claude plugin marketplace add <owner/repo or local path>
claude plugin install pc-hardware-advisor@pc-hardware-advisor
```

`marketplace add` aceita um repositório do GitHub (`owner/repo`), uma URL git ou https, ou um caminho local. Para este repositório, o endereço no GitHub é `brissonjo-sudo/pc-hardware-advisor`. Adicione `--scope project` ou `--scope local` a qualquer um dos comandos se você não quiser uma instalação para todo o usuário (o padrão é `user`).

Verifique o que está instalado com `claude plugin marketplace list`.

### Desenvolvimento local

Para testar o plugin a partir de uma cópia de trabalho, sem instalá-lo:

```
claude --plugin-dir <path to this repository>
```

### Claude desktop / Cowork

Obtenha o arquivo `pc-hardware-advisor.plugin` (anexado a uma release quando houver uma publicada, ou gerado a partir de uma cópia de trabalho com `python scripts/build_plugin.py`, que o grava em `dist/`), arraste-o para o aplicativo desktop do Claude e aceite o prompt de instalação.

## Exemplos de pedidos

O Claude escolhe a skill certa a partir do pedido. Alguns exemplos:

1. "Encontre o melhor preço entregue na Alemanha para um Ryzen 7 9800X3D. Lojas diretas primeiro, marketplaces em separado."
2. "Compensa importar uma RTX 5070 Ti dos EUA para o Canadá, depois de incluir impostos e frete?"
3. "Este kit DDR5-6000 funciona com uma placa ASUS TUF B650 e um Ryzen 7 7700? Dê um veredito por par."
4. "Monte um PC para jogos em 1440p, silencioso, por 1.400 EUR na Espanha. Inclua também uma variante mais barata e uma mais potente."
5. "Quero rodar um modelo de 70B localmente com uma velocidade utilizável. De quanta VRAM e de qual largura de banda de memória eu preciso, e duas GPUs usadas de 24 GB dariam conta?"
6. "Confira para mim este anúncio de RTX 3090 usada (link abaixo). Comprar, negociar ou evitar? O que devo perguntar ao vendedor?"
7. "Acompanhe o preço do Samsung 990 Pro de 2 TB no Reino Unido e me avise apenas se ele cair abaixo de 120 GBP."
8. En français : "Trouve-moi le meilleur prix livré en France pour une alimentation 850 W ATX 3.1, vendeurs directs d'abord, places de marché à part."
9. En español : "Quiero montar un PC para edición de vídeo con 1.800 EUR en España. ¿Qué configuración me recomiendas, y qué compatibilidad debo vigilar entre placa, RAM y GPU?"
10. "Uma APU com 64 GB de memória unificada consegue rodar um modelo de 32B, e que velocidade devo esperar? Rotule o que for estimativa."

## Conectores

As skills se referem às ferramentas por categoria (busca na web, leitura de páginas web, comparador de preços, site de classificados, navegador, agendador, notificações), não por produto, então qualquer ferramenta equivalente serve. Nada no plugin exige uma conta, uma chave de API ou um serviço pago. As categorias, as fontes de dados opcionais e as regras que se aplicam a todas as ferramentas estão em [CONNECTORS.md](../CONNECTORS.md).

## Limites

- **Preços são perecíveis.** Um preço só é válido na data de leitura. Estoque e promoções mudam em questão de horas.
- **Alguns sites bloqueiam a leitura automatizada.** Essas linhas são marcadas como bloqueadas, e o Claude pede a você uma captura de tela ou um texto colado.
- **Regras de impostos e tarifas são voláteis.** IVA, direitos aduaneiros e limites de isenção (de minimis) mudaram repetidamente em 2025 e 2026. Confira a fonte oficial antes de uma importação grande.
- **Estimativas são estimativas.** Os valores de tokens por segundo e projeções semelhantes são modelados, não medidos na sua máquina, e são rotulados como tal.
- **A cobertura da pesquisa tem lacunas.** Alguns países, lojas e peças de nicho são cobertos de forma superficial. As referências indicam onde.
- **Não é aconselhamento financeiro nem jurídico.** O plugin informa uma decisão de compra. Ele não aconselha sobre questões fiscais, aduaneiras ou de direito do consumidor.

## Privacidade

O próprio plugin não coleta nada e não envia nada a lugar algum. Os históricos de preço gravados pelo `track-price` ficam onde você decidir mantê-los. As ferramentas que o Claude usa para buscar e ler páginas (busca na web, leitura de páginas web, agendador) seguem os termos e as políticas de privacidade dos próprios provedores.

## Traduções

Traduções automáticas deste README, não revisadas por um humano: [README.fr.md](README.fr.md), [README.es.md](README.es.md), [README.zh-CN.md](README.zh-CN.md), [README.hi.md](README.hi.md), [README.pt.md](README.pt.md), [README.ar.md](README.ar.md), [README.de.md](README.de.md), [README.ja.md](README.ja.md). A versão em inglês prevalece.

## Contribuindo

Contribuições são bem-vindas sob condições específicas, incluindo a cessão de direitos. Leia [CONTRIBUTING.md](../CONTRIBUTING.md) antes de abrir um pull request.

## Licença

PC Hardware Advisor é de código-fonte disponível sob a PolyForm Noncommercial License 1.0.0 (SPDX: PolyForm-Noncommercial-1.0.0). O uso não comercial é permitido para todos; o uso comercial exige uma licença separada do autor. A mesma licença cobre as skills, as referências, a documentação e as traduções.

Texto completo: [LICENSE](../LICENSE) e <https://polyformproject.org/licenses/noncommercial/1.0.0>.
