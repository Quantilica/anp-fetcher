---
dataset:
  id: rodadas
  fonte: anp
  titulo: Rodadas de licitações de petróleo e gás natural
  resumo: Blocos ofertados e ofertas vencedoras nas 9ª a 17ª Rodadas de Licitações e o histórico dos processos de cessão de contratos de E&P desde 2001.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/rodadas-de-licitacoes-de-petroleo-e-gas-natural
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'blocos ofertados e ofertas vencedoras: após cada rodada; cessão de contratos: semestral (metadados da ANP)'
  cobertura:
    inicio: '2001'
    fim: '2026'
  unidade: um bloco ofertado numa rodada (rlpgn-blocos), uma oferta vencedora para um bloco (rlpgn-vencedoras) ou um processo de cessão de contrato (rlpgn-cessao)
  granularidade:
    espacial: bloco, setor e bacia sedimentar; ambiente (terra, águas rasas, águas profundas)
    temporal: rodada de licitação; na cessão, data de aprovação da decisão (2001 a 2026 na amostra)
  formato_bruto: 'três CSV (rlpgn: blocos-ofertados-rodadas, ofertas-vencedoras-rodadas e processos-cessao-contratos), separador ponto e vírgula, ISO-8859-1, um por tabela'
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 30
  unidades_de_medida:
    ' Bonus Mínimo ': R$ (reais)
    ' Bônus ': R$ (reais)
    ' PEM (R$) ': R$ (reais)
    PEM (UT): unidades de trabalho (UT)
    Conteúlo Local  - Exploração: '%'
    Conteúdo Local Médio -  Desenvolvimento: '%'
    Pontos: pontos
    Prazo (dias) ²: dias
  dados_pessoais:
  - coluna: Antes da cessão
    categoria: nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos
  - coluna: Cedente
    categoria: nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos
  - coluna: Cessionária
    categoria: nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos
  - coluna: Após efetivação da cessão
    categoria: nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos
  - coluna: Empresa/Consórcio(*operador)
    categoria: nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Rodadas de licitações de petróleo e gás natural

## Resumo

As rodadas de licitação são os leilões em que a União concede o direito de explorar e produzir petróleo e gás natural. O grupo reúne três tabelas da Superintendência de Promoção de Licitações da ANP: os blocos ofertados nas rodadas de licitação de blocos exploratórios (da 9ª à 17ª), as ofertas vencedoras (empresa ou consórcio, bônus de assinatura, conteúdo local, programa exploratório mínimo e pontos) e o histórico dos processos de cessão de contratos (transferência de direitos e obrigações, mudança de operadora, entre outros), com a composição do contrato antes e depois de cada cessão. Não incluem acumulações marginais, contratos de partilha de produção nem os ciclos da Oferta Permanente.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/rodadas` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/rodadas-de-licitacoes-de-petroleo-e-gas-natural |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | blocos ofertados e ofertas vencedoras: após cada rodada; cessão de contratos: semestral (metadados da ANP) |
| Cobertura | 2001 a 2026 |
| Unidade (uma linha) | um bloco ofertado numa rodada (rlpgn-blocos), uma oferta vencedora para um bloco (rlpgn-vencedoras) ou um processo de cessão de contrato (rlpgn-cessao) |
| Granularidade | espacial: bloco, setor e bacia sedimentar; ambiente (terra, águas rasas, águas profundas); temporal: rodada de licitação; na cessão, data de aprovação da decisão (2001 a 2026 na amostra) |
| Formato bruto | três CSV (rlpgn: blocos-ofertados-rodadas, ofertas-vencedoras-rodadas e processos-cessao-contratos), separador ponto e vírgula, ISO-8859-1, um por tabela |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 30 |
| Unidades de medida | ` Bonus Mínimo `: R$ (reais); ` Bônus `: R$ (reais); ` PEM (R$) `: R$ (reais); `PEM (UT)`: unidades de trabalho (UT); `Conteúlo Local  - Exploração`: %; `Conteúdo Local Médio -  Desenvolvimento`: %; `Pontos`: pontos; `Prazo (dias) ²`: dias |
| Dados pessoais | `Antes da cessão` (nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos); `Cedente` (nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos); `Cessionária` (nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos); `Após efetivação da cessão` (nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos); `Empresa/Consórcio(*operador)` (nomes de empresas (pessoas jurídicas) que ofertaram, ganharam ou cederam participação em contratos) |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Promoção de Licitações (SPL); os blocos ofertados e as ofertas vêm do Sistema de Análise de Ofertas (SAOF), e as cessões do histórico de processos da SPL (metadados da ANP). Contato: rodadas@anp.gov.br.
- **Catálogo do fetcher:** 3 arquivos: `rlpgn-blocos`, `rlpgn-vencedoras` e `rlpgn-cessao` (conferido em 2026-11-15). A página oficial indica atualização em 6/3/2026 para blocos ofertados e ofertas vencedoras e em 1/7/2026 para as cessões.
- **Escopo:** só blocos ofertados em rodadas de licitação de blocos exploratórios (sem acumulações marginais, partilha de produção ou ciclos da Oferta Permanente), segundo os metadados.
- **Texto da página:** a página diz que o histórico de cessões vai «de 2001 a 2017», mas o arquivo vai até 2026 (as datas de aprovação da amostra vão de 2001 a 2026).

## Conteúdo

O grupo tem três tabelas independentes:

| Arquivo no lake | Conteúdo | Linhas na amostra |
|---|---|---|
| `rlpgn-blocos` | blocos ofertados nas rodadas 9ª a 17ª: rodada, bacia, setor, bloco, habilitação mínima, bônus mínimo, localização e se foi arrematado | 1.681 |
| `rlpgn-vencedoras` | ofertas vencedoras nas rodadas 9ª a 17ª: empresa ou consórcio, bônus, conteúdo local, programa exploratório mínimo e pontos | 498 |
| `rlpgn-cessao` | histórico dos processos de cessão de contratos, desde 2001: tipo, contrato, bacia, composição antes e depois, cedente, cessionária, decisão e data | 1.294, das quais 147 vazias (1.147 de dados) |

- **Blocos ofertados e arrematados:** na amostra, de 1.681 blocos ofertados, 498 foram arrematados (`Bloco arrematado` = `Sim`), o mesmo número de linhas de `rlpgn-vencedoras`; o 17ª Rodada tem 92 blocos ofertados e 5 arrematados.
- **Rodadas cobertas:** 9ª a 17ª nos blocos e nas vencedoras (as rodadas 1 a 8 não estão neste conjunto).
- **Localização dos blocos ofertados:** 964 de terra, 337 em água profunda ou ultraprofunda, 251 em água rasa de 100 a 400 m e 129 em água rasa de 0 a 100 m.
- **Cessões:** 5 tipos de solicitação (códigos 1 a 5, às vezes combinados, como `1 e 3`); 782 pedidos do tipo 1, 176 do tipo `1 e 3` e 106 do tipo 2. A `Rodada` do contrato cedido usa códigos como `R0` (317 linhas), `R9` (159) e `R7` (114).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `rlpgn-blocos` (8); `rlpgn-cessao` (16); `rlpgn-vencedoras` (11) |

## Variáveis

As descrições vêm dos metadados da ANP para as três tabelas (documentos «Blocos ofertados», «Ofertas vencedoras» e «Processos de cessão de contratos»), com os nomes das colunas ajustados aos do arquivo. As colunas `Data do requerimento`, `Entrega da documentação completa`, `Assinatura do Termo Aditivo` e `Prazo (dias) ²` do arquivo de cessões não constam do dicionário e têm descrição deduzida do nome. O lake guarda tudo como texto, inclusive valores com pontos de milhar e vírgula decimal. A coluna *Arquivos* diz em quais tabelas a coluna aparece.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Rodada de Licitações` | `Rodada de Licitações` | texto | Rodada de licitação (por exemplo, `09ª Rodada de Licitações`) | — | — | `rlpgn-blocos`, `rlpgn-vencedoras` |
| `Bacia` | `Bacia` | texto | Bacia sedimentar onde está o bloco ofertado (blocos e vencedoras) ou o contrato (cessões) | — | — | `rlpgn-blocos`, `rlpgn-cessao`, `rlpgn-vencedoras` |
| `Setor` | `Setor` | texto | Código do setor ofertado (por exemplo, `SC-AR4`) | — | — | `rlpgn-blocos`, `rlpgn-vencedoras` |
| `Bloco` | `Bloco` | texto | Código do bloco ofertado (blocos) ou do bloco que recebeu ofertas na sessão pública (vencedoras) | — | — | `rlpgn-blocos`, `rlpgn-vencedoras` |
| `Habilitação Mínima` | `Habilitação Mínima` | texto | Habilitação mínima exigida da empresa para ofertar pelo bloco: operadora A (águas ultraprofundas, profundas, rasas e áreas terrestres), B (águas rasas e áreas terrestres) ou C (áreas terrestres) | — | — | `rlpgn-blocos` |
| ` Bonus Mínimo ` | ` Bonus Mínimo ` | texto | Valor, em reais, do bônus de assinatura mínimo aceito como oferta, escrito com pontos de milhar e vírgula decimal (por exemplo, ` 3.936.000,00 ` com espaços); nas 92 linhas da 17ª Rodada vem com o prefixo `R$ `; nome da coluna com espaços no início e no fim (o nome da coluna tem espaços no início ou no fim) | — | — | `rlpgn-blocos` |
| `Localização` | `Localização` | texto | Localização do bloco: `TERRA`, `ÁGUA RASA (0 a 100 m)`, `ÁGUA RASA (100 a 400 m)` ou `ÁGUA PROFUNDA OU ULTRAPROFUNDA` | — | — | `rlpgn-blocos` |
| `Bloco arrematado` | `Bloco arrematado` | texto | Indica se o bloco foi arrematado: `Sim` ou `Não` | — | — | `rlpgn-blocos` |
| `Tipo de solicitação ¹` | `Tipo de solicitação ¹` | texto | Tipo do pedido de cessão: 1 transferência, total ou parcial, de direitos e obrigações; 2 fusão, cisão ou incorporação que muda a concessionária ou contratada; 3 mudança de operadora; 4 isenção ou substituição de garantia de performance; 5 divisão da área de concessão; combinações como `1 e 3` são possíveis | — | — | `rlpgn-cessao` |
| `Data do requerimento` | `Data do requerimento` | texto | Data do requerimento do pedido de cessão (dd/mm/aaaa); preenchida só em parte das linhas (659 de 1.147 na amostra); não consta do dicionário da ANP | — | — | `rlpgn-cessao` |
| `Entrega da documentação completa` | `Entrega da documentação completa` | texto | Data da entrega da documentação completa do pedido; preenchida só em parte das linhas; descrição deduzida do nome e dos valores observados; não consta do dicionário da ANP | — | — | `rlpgn-cessao` |
| `Processo de cessão` | `Processo de cessão` | texto | Número do processo administrativo que tratou a cessão (por exemplo, `48610.014705/2001`; o sufixo do dígito verificador varia) | — | — | `rlpgn-cessao` |
| `Rodada` | `Rodada` | texto | Rodada de licitação do contrato cedido, em código (por exemplo, `R0`, `R9`, `R11`) | — | — | `rlpgn-cessao` |
| `Contrato` | `Contrato` | texto | Identificador do contrato, com o nome do bloco entre parênteses (por exemplo, `48000.003570/97-01 (BS-1)`) | — | — | `rlpgn-cessao` |
| `Ambiente operacional` | `Ambiente operacional` | texto | Ambiente do contrato: água rasa, água profunda, terra, terra e mar (a grafia varia: `Águas rasas`, `Águas profundas`) | — | — | `rlpgn-cessao` |
| `Antes da cessão` | `Antes da cessão` | texto | Participantes do contrato antes da cessão, com a participação percentual; vários integrantes separados por quebra de linha; `(*)` marca a operadora | — | — | `rlpgn-cessao` |
| `Cedente` | `Cedente` | texto | Empresa que cedeu a participação (vazia nas 12 linhas de tipo 5, divisão da área) | — | — | `rlpgn-cessao` |
| `Cessionária` | `Cessionária` | texto | Empresa que recebeu a participação (vazia nas 12 linhas de tipo 5, divisão da área) | — | — | `rlpgn-cessao` |
| `Após efetivação da cessão` | `Após efetivação da cessão` | texto | Participantes do contrato depois da cessão, com a participação percentual; vários integrantes separados por quebra de linha; `(*)` marca a operadora | — | — | `rlpgn-cessao` |
| `Decisão de Diretoria nº` | `Decisão de Diretoria nº` | texto | Número da decisão da Diretoria que aprovou a cessão, no formato `nnn/aaaa` | — | — | `rlpgn-cessao` |
| `Data da aprovação` | `Data da aprovação` | texto | Data da aprovação da cessão (dd/mm/aaaa) | — | — | `rlpgn-cessao` |
| `Assinatura do Termo Aditivo` | `Assinatura do Termo Aditivo` | texto | Data da assinatura do termo aditivo ao contrato; preenchida só em parte das linhas; descrição deduzida do nome e dos valores observados; não consta do dicionário da ANP | — | — | `rlpgn-cessao` |
| `Prazo (dias) ²` | `Prazo (dias) ²` | texto | Prazo, em dias, entre a entrega da documentação completa e a aprovação, ou outro prazo do trâmite; descrição deduzida do nome (a nota ² do arquivo não está no dicionário da ANP); preenchida só em parte das linhas | — | — | `rlpgn-cessao` |
| `Empresa/Consórcio(*operador)` | `Empresa/Consórcio(*operador)` | texto | Empresa ou consórcio vencedor, com a participação percentual de cada integrante; o operador vem marcado com asterisco (por exemplo, `OGX (100%)*`) | — | — | `rlpgn-vencedoras` |
| ` Bônus ` | ` Bônus ` | texto | Valor, em reais, do bônus de assinatura da oferta vencedora (pontos de milhar e vírgula decimal); nome da coluna com espaços no início e no fim (o nome da coluna tem espaços no início ou no fim) | — | — | `rlpgn-vencedoras` |
| `Conteúlo Local  - Exploração` | `Conteúlo Local  - Exploração` | texto | Percentual de conteúdo local ofertado para a fase de exploração (por exemplo, `60%`); `Definido no edital` em 76 das 498 linhas; o nome da coluna tem um erro de grafia e dois espaços na fonte | — | — | `rlpgn-vencedoras` |
| `Conteúdo Local Médio -  Desenvolvimento` | `Conteúdo Local Médio -  Desenvolvimento` | texto | Percentual médio de conteúdo local ofertado para a etapa de desenvolvimento da produção (por exemplo, `70%`) | — | — | `rlpgn-vencedoras` |
| `PEM (UT)` | `PEM (UT)` | texto | Programa exploratório mínimo ofertado, em unidades de trabalho (UT), com ponto de milhar (por exemplo, `4.088`) | — | — | `rlpgn-vencedoras` |
| ` PEM (R$) ` | ` PEM (R$) ` | texto | Programa exploratório mínimo ofertado, em reais (pontos de milhar e vírgula decimal); nome da coluna com espaços no início e no fim (o nome da coluna tem espaços no início ou no fim) | — | — | `rlpgn-vencedoras` |
| `Pontos` | `Pontos` | texto | Pontos obtidos pela licitante no certame (vírgula decimal, quatro casas) | — | — | `rlpgn-vencedoras` |

## No lake

- Dataset `anp/rodadas`, sem partições; um Parquet por tabela: `rlpgn-blocos.parquet`, `rlpgn-vencedoras.parquet` e `rlpgn-cessao.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (acentos, espaços, notas ¹ ²); os nomes ` Bonus Mínimo `, ` Bônus ` e ` PEM (R$) ` têm espaços no início e no fim.
- As 147 linhas vazias do final do arquivo de cessões são mantidas pelo conversor (ver Cuidados).

## Cuidados de uso

- **Valores numéricos em texto.** Bônus e PEM (R$) vêm como `237.241.063,00` (pontos de milhar, vírgula decimal), PEM (UT) como `4.088`, e os percentuais de conteúdo local como `60%`. Troque os separadores antes de converter. O bônus mínimo dos blocos tem o prefixo `R$ ` nas 92 linhas da 17ª Rodada, e o conteúdo local exploratório traz o texto `Definido no edital` em 76 das 498 ofertas vencedoras.
- **Nomes de coluna com espaços.** ` Bonus Mínimo `, ` Bônus ` e ` PEM (R$) ` têm espaços no início e no fim, e a coluna `Conteúlo Local  - Exploração` tem erro de grafia e dois espaços; cite exatamente ao consultar, ou renomeie.
- **Linhas vazias em `rlpgn-cessao`.** 147 das 1.294 linhas não têm nenhum campo preenchido; descarte as de `Processo de cessão` nulo.
- **`Cedente` e `Cessionária` vazios** nas 12 linhas de tipo 5 (divisão da área de concessão), que não têm cedente nem cessionária (1.135 de 1.147 preenchidos).
- **Composição do contrato em texto de várias linhas.** `Antes da cessão` e `Após efetivação da cessão` juntam os participantes com quebra de linha dentro do campo (por exemplo, `(*) Petróleo Brasileiro S/A 40%` e na linha seguinte o outro participante); separe antes de analisar. Os nomes de empresas variam de grafia entre linhas (`Petróleo Brasileiro S/A` nas composições e `Petróleo Brasileiro S.A. - Petrobras` em `Cedente`).
- **`Processo de cessão` não é único** (730 valores distintos em 1.147 linhas de dados): o mesmo processo cobre vários contratos.
- **Texto corrompido em três linhas.** `Cedente` traz `Petróleo Brasileiro S.A.  Petrobras` (caractere de controle U+0096 no lugar do travessão) em 3 linhas: o arquivo de origem usa o travessão do Windows-1252 e o conversor o lê como ISO-8859-1. Troque `` por `-`.
- **Escopo parcial.** Só rodadas 9 a 17 de blocos exploratórios, sem as rodadas anteriores nem partilha ou oferta permanente; não some bônus e programa exploratório de rodadas diferentes sem checar o regime.
- **Dados identificáveis.** Os nomes de empresas e consórcios são pessoas jurídicas; o arquivo não traz pessoas físicas.

## Exemplos

Número de blocos ofertados e arrematados em cada rodada, com o bônus mínimo médio, a partir da tabela de blocos:

```python
import duckdb

duckdb.sql("""
    SELECT "Rodada de Licitações" AS rodada, count(*) AS ofertados,
           count(*) FILTER (WHERE "Bloco arrematado" = 'Sim') AS arrematados,
           round(avg(trim(replace(replace(replace(trim(" Bonus Mínimo "), 'R$', ''), '.', ''), ',', '.'))::DOUBLE) / 1e6, 1) AS bonus_minimo_medio_milhoes_rs
    FROM read_parquet('lake/anp/rodadas/rlpgn-blocos.parquet')
    GROUP BY ALL
    ORDER BY rodada
""").show()
```

## Referências

- Dados abertos da ANP, Rodadas de Licitações de Petróleo e Gás Natural: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/rodadas-de-licitacoes-de-petroleo-e-gas-natural
- Metadados: blocos ofertados (https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/rlpgn/metadado-blocos-ofertados-rodadas.pdf), ofertas vencedoras (.../rlpgn/metadado-ofertas-vencedoras-rodadas.pdf) e processos de cessão (.../rlpgn/metadado-processos-cessao-contratos.pdf)
- Rodadas de licitações da ANP: https://www.gov.br/anp/pt-br/rodadas-anp
