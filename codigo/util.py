import pandas as pd

#  Carregar o dataset normalizado
CAMINHO_MAP = "../documentacao/PeNSE — map_codigo_descricao.csv"

def carregar_mapa_codigos() -> dict:
  """Lê um CSV com as colunas 'codigo' e 'descricao' e retorna um dicionário."""

  df = pd.read_csv(CAMINHO_MAP, sep=";", dtype={"codigo": str})

  # Remove espaços extras caso existam
  df["codigo"] = df["codigo"].str.strip()

  # Remove códigos duplicados mantendo o primeiro e ignora linhas sem código
  df = df.dropna(subset=["codigo"]).drop_duplicates(
      subset=["codigo"], keep="first"
  )

  return dict(zip(df["codigo"], df["descricao"]))


def obter_descricao( codigo, padrao: str = "Código não encontrado") -> str:
  mapa = carregar_mapa_codigos()
  """Retorna a descrição associada ao código informado."""
  if pd.isna(codigo):
    return padrao
  chave = str(codigo).strip()
  return mapa.get(chave, padrao)


carregar_mapa_codigos()
descricao = obter_descricao("B01003")
#print("Descrição:", descricao)