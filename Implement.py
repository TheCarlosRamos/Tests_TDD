from datetime import date
from django.core.exceptions import ObjectDoesNotExist

class Fatura(models.Model):
    distributor = models.ForeignKey(
        Distributor,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    
    consumer_unit = models.ForeignKey(
        ConsumerUnit,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    mes = models.IntegerField(
        null=False,
        blank=False,
    )

    ano = models.IntegerField(
        null=False,
        blank=False,
    )

class Distributor(models.Model):

    def emitir_fatura(self, uc, mes, ano):
        # Verificar se já existe uma fatura para a mesma UC, mês e ano
        if Fatura.objects.filter(distributor=self, consumer_unit=uc, mes=mes, ano=ano).exists():
            raise ValueError("Já existe uma fatura para esta UC, mês e ano.")

        nova_fatura = Fatura(distributor=self, consumer_unit=uc, mes=mes, ano=ano)
        nova_fatura.save()

        return nova_fatura
