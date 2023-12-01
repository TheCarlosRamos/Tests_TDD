import unittest
from unittest.mock import MagicMock, patch
from sistema_fatura import SistemaFatura, Distributor, Fatura, ConsumerUnit

class TestSistemaFatura(unittest.TestCase):
    def test_emitir_fatura_com_mes_ano_existente_deve_retornar_erro(self):
        # Configurar o cenário de teste
        sistema = SistemaFatura()
        distributor = Distributor.objects.create(name="Test Distributor", cnpj="12345678901234", university=sistema.university)
        uc = ConsumerUnit.objects.create(name="Test UC", university=sistema.university)
        mes = 5
        ano = 2023

        # Mock do método que verifica se já existe uma fatura
        with patch('sistema_fatura.Fatura.objects.filter', MagicMock(return_value=MagicMock(exists=MagicMock(return_value=True)))):
            with self.assertRaises(ValueError):
                sistema.emitir_fatura(distributor, uc, mes, ano)

    def test_emitir_fatura_com_mes_ano_inexistente_deve_ser_bem_sucedido(self):
        # Configurar o cenário de teste
        sistema = SistemaFatura()
        distributor = Distributor.objects.create(name="Test Distributor", cnpj="12345678901234", university=sistema.university)
        uc = ConsumerUnit.objects.create(name="Test UC", university=sistema.university)
        mes = 5
        ano = 2023

        # Mock do método que verifica se já existe uma fatura
        with patch('sistema_fatura.Fatura.objects.filter', MagicMock(return_value=MagicMock(exists=MagicMock(return_value=False)))):
            # Executar a ação 
            try:
                sistema.emitir_fatura(distributor, uc, mes, ano)
            except ValueError:
                self.fail("Emitir fatura falhou inesperadamente")

if __name__ == '__main__':
    unittest.main()
