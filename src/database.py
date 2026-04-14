import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def salvar_analise_db(amostra: dict, status, recomendacao: str) -> None:
    """
    Algoritmo para persistir a análise no Oracle Database.
    """

    conn = None
    try:
        # Pega as credenciais do .env
        user = os.getenv("USUARIO")
        password = os.getenv("PASSWORD")
        banco = os.getenv("BANCO")

        # Conectar ao banco
        conn = oracledb.connect(user=user, password=password, dsn=banco)
        cursor = conn.cursor()

        # Query de inserção
        sql = """
            INSERT INTO ANALISE_SOLO (cultura, nitrogenio, fosforo, potassio, ph, status, recomendacao)
            VALUES (:1, :2, :3, :4, :5, :6, :7)
        """

        valores = (
            amostra['cultura'], 
            amostra['nitrogenio'], 
            amostra['fosforo'], 
            amostra['potassio'], 
            amostra['ph'],
            status,
            recomendacao
        )

        cursor.execute(sql, valores)
        conn.commit()
        print("\n[DB] Dados salvos no Oracle com sucesso!")

    except Exception as e:
        print(f"\n[Erro DB] Falha ao salvar no banco: {e}")
    
    finally:
        if conn:
            conn.close()