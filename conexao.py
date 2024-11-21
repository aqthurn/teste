import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from pandas.plotting import table

class Conexao:
    def __init__(self):
        self.connection = self.conectar()
        self.cursor = self.connection.cursor()

    def conectar(self):
        try:
            connection = sqlite3.connect("deleonhotel.db")
            return connection
        except sqlite3.Error as e:
            print(f'Erro ao conectar ao banco de dados: {e}')
            return None

    #def create_table(self):
        try:
            sql = '''
                    CREATE TABLE IF NOT EXISTS transacoes(
                        id_transacao INTEGER PRIMARY KEY,
                        valor FLOAT,
                        nome_transacao VARCHAR(300),
                        tipo_transacao VARCHAR(100),
                        data VARCHAR(12)
                    )'''
            self.cursor.execute(sql)
            self.connection.commit()
            print('Tabela criada com sucesso')
        except sqlite3.Error as e:
            print(f'Erro ao criar a tabela: {e}')

    def insert_transacao(self, cliente, banho, tosa, transporte, data):
        try:
            sql = '''
                    INSERT INTO pethotel ( Cliente, Banho, Tosa, Transporte, Data)
                    VALUES (?, ?, ?, ?, ?)
                  '''
            self.cursor.execute(sql, (cliente, banho, tosa, transporte, data))
            self.connection.commit()
            print('Transação inserida com sucesso')
        except sqlite3.Error as e:
            print(f'Erro ao inserir transação: {e}')

    def update_transacao(self, cliente, banho, tosa, transporte, data ):
        try:
            sql = '''
                UPDATE pethotel
                SET Cliente = ?, Banho = ?, Tosa = ?, Transporte = ?, Data = ?
                WHERE id_cliente = ?
            '''
            self.cursor.execute(sql, (cliente, banho, tosa, transporte, data))
            self.connection.commit()
            print('Transação atualizada com sucesso')
        except sqlite3.Error as e:
            print(f'Erro ao atualizar transação: {e}')   
            
    def delete_transacao(self, id_cliente):
        try:
            sql = '''
                       DELETE FROM pethotel
                    WHERE id_cliente = ?
                  '''
            self.cursor.execute(sql, (id_cliente,))
            self.connection.commit()
            print('Transação deletada com sucesso')
        except sqlite3.Error as e:
            print(f'Erro ao deletar transação: {e}')


   
    def delete_all(self):
        
            self.cursor.execute("DELETE FROM pethotel")  # Ajuste o nome da tabela, se necessário
            self.connection.commit()

           
    def read_all(self):
        try:
            sql = '''SELECT * FROM pethotel'''
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f'Erro ao ler todas as transações: {e}')
            return []

    def read_one(self, id_cliente):
        try:
            sql = '''SELECT * FROM pethotel WHERE id_cliente = ?'''
            self.cursor.execute(sql, (id_cliente,))
            row = self.cursor.fetchone()
            return row
        except sqlite3.Error as e:
            print(f'Erro ao ler transação: {e}')
            return None

    def read_data_por_ano(self, ano):
        try:
            query = "SELECT * FROM pethotel WHERE strftime('%Y', data) = ?"
            self.cursor.execute(query, (str(ano),))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Erro ao ler transações por ano: {e}')
            return []

    def read_data_por_mes(self, ano, mes):
        try:
            query = "SELECT * FROM pethotel WHERE strftime('%Y', data) = ? AND strftime('%m', data) = ?"
            self.cursor.execute(query, (str(ano), str(mes).zfill(2)))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Erro ao ler transações por mês: {e}')
            return []

    def read_data_por_dia(self, data_pesquisa):
        try:
            query = "SELECT * FROM pethotel WHERE data = ?"
            self.cursor.execute(query, (data_pesquisa,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Erro ao ler transações por dia: {e}')
            return []

    def close(self):
        if self.connection:
            self.connection.close()
            print('Conexão fechada com sucesso')
        else:
            print('Nenhuma conexão ativa para fechar')

    

if __name__ == '__main__':
    conexao = Conexao()
    
    
    # Inserir transações de entrada e saída
    
    
    # Calcular e imprimir os totais
   
    
    # Criar tabelas para exibir os resultados
    
    
   
    
    # Save DataFrames as PDF
    
    conexao.insert_transacao("Cliente Exemplo", 1, 1, 0, "2024-11-13")
     # Defina o id_cliente com um valor apropriado
    conexao.update_transacao("Cliente Atualizado", 0, 1, 1, "2024-11-14")
    conexao.close()