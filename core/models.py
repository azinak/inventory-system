from django.db import models

from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    arabic_name = models.CharField(max_length=100, verbose_name='الإسم بالعربي')
    phone1 = models.CharField(max_length=20, null=True, blank=True)
    phone2 = models.CharField(max_length=20, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True, verbose_name='ملاحظات')
    description = models.TextField(null=True, blank=True)
    camion = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=80, blank=True, null=True)
    nif = models.CharField(max_length=80, blank=True, null=True)
    nis = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.arabic_name



class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    arabic_name = models.CharField(max_length=100, verbose_name='الإسم بالعربي')
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    box = models.IntegerField(blank=True, null=True)
    container = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=10, decimal_places=2)
    distribution_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    barcode = models.CharField(max_length=100, unique=True, null=True, blank=True)
    min_stock_level = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Case(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    INVOICE_TYPES = [
        ('SALE', 'بيع'),
        ('PURCHASE', 'شراء'),
        ('RETURN', 'مرتجع'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_date = models.DateField(default=timezone.now)
    payment_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    invoice_type = models.CharField(max_length=20, choices=INVOICE_TYPES)
    invoice_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = str(uuid.uuid4().hex[:8].upper())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"فاتورة {self.invoice_number} - {self.client.arabic_name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

class Transaction(models.Model):
    transfer_date = models.DateField()
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transfer_address = models.CharField(max_length=150, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    label = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"تحويل {self.id} - {self.client.arabic_name}"

class TransactionInvoice(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2) 

