import pandas as pd
import re
from regras import regras

# ====== ETAPA 1: Extrair ======
def carregar_dados():
    return pd.read_csv("data/clientes.csv", dtype={"cpf": str})

df = carregar_dados()


# ====== ETAPA 2: Transformar / Validar ======
def validar_dados(df, regras):
    erros = []

    for coluna, regra in regras.items():
        if coluna not in df.columns:
            erros.append(f"Coluna ausente: {coluna}")
            continue

        # Verifica valores obrigatórios
        if regra.get("obrigatorio"):
            nulos = df[coluna].isnull().sum()
            if nulos > 0:
                erros.append(f"Coluna {coluna} contém {nulos} valores nulos")

        # Verifica tipo
        if regra.get("tipo") == "int":
            # Tenta converter para número
            coluna_num = pd.to_numeric(df[coluna], errors="coerce")
            invalidos = coluna_num.isna().sum() - df[coluna].isna().sum()
            if invalidos > 0:
                erros.append(f"Coluna {coluna} contém {invalidos} valores não numéricos")
        elif regra.get("tipo") == "string":
            if not pd.api.types.is_string_dtype(df[coluna].dropna()):
                erros.append(f"Coluna {coluna} não é string")

        # Verifica tamanho
        if "tamanho" in regra:
            max_len = df[coluna].dropna().astype(str).map(len).max()
            if max_len > regra["tamanho"]:
                erros.append(f"Coluna {coluna} excede tamanho máximo {regra['tamanho']}")

        # Verifica regex (exemplo: e-mail)
        if "regex" in regra:
            padrao = re.compile(regra["regex"])
            invalidos = df[coluna].dropna().apply(lambda x: not bool(padrao.match(str(x)))).sum()
            if invalidos > 0:
                erros.append(f"Coluna {coluna} contém {invalidos} valores fora do padrão regex")

        # Verifica limites (idade, valores etc.)
        if "min" in regra or "max" in regra:
            coluna_num = pd.to_numeric(df[coluna], errors="coerce")

            if "min" in regra:
                abaixo = (coluna_num.dropna() < regra["min"]).sum()
                if abaixo > 0:
                    erros.append(f"Coluna {coluna} contém {abaixo} valores abaixo do mínimo {regra['min']}")

            if "max" in regra:
                acima = (coluna_num.dropna() > regra["max"]).sum()
                if acima > 0:
                    erros.append(f"Coluna {coluna} contém {acima} valores acima do máximo {regra['max']}")

    return erros


# ====== ETAPA 3: Carregar (relatório de qualidade) ======
def gerar_relatorio(erros):
    if not erros:
        print("✅ Dados aprovados! Nenhum problema encontrado.")
    else:
        print("⚠️ Problemas de qualidade encontrados:")
        for e in erros:
            print(" -", e)


# ====== EXECUÇÃO ======
if __name__ == "__main__":
    df = carregar_dados()
    erros = validar_dados(df, regras)
    gerar_relatorio(erros)
