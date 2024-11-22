from datetime import datetime

# Product sınıfı
class Product:
    def __init__(self, name=None, price=0, quantity=1):
        # Varsayılan değerler
        self._name = name if name is not None else "Unknown"
        self._price = price if price >= 0 else 0
        self._quantity = quantity if quantity >= 1 else 1
        
        # Veri doğrulama
        if len(self._name) < 3 or len(self._name) > 8:
            raise ValueError("Ürün ismi 3 ile 8 karakter arasında olmalı.")
        if self._price < 0:
            raise ValueError("Fiyat 0'dan küçük olamaz.")
        if self._quantity < 1:
            raise ValueError("Adet 1'den küçük olamaz.")

        # Ekrana ürün adı ve tarih bilgisi yazdırılır
        print(f"Ürün Adı: {self._name}, Tarih: {datetime.now()}")

    # Getter ve Setter metodları
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 8:
            self._name = value
        else:
            raise ValueError("Ürün ismi 3 ile 8 karakter arasında olmalı.")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Fiyat 0'dan küçük olamaz.")
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value >= 1:
            self._quantity = value
        else:
            raise ValueError("Adet 1'den küçük olamaz.")
    
    def get_total_price(self):
        """Toplam fiyatı hesaplar"""
        return self._price * self._quantity
    
    def __str__(self):
        """Ürünü yazdırırken base sınıfın metodunu geçersiz kılar"""
        return f"Ürün: {self._name}, Fiyat: {self._price}, Adet: {self._quantity}, Toplam: {self.get_total_price()}"

# ProductHelper sınıfı
class ProductHelper:
    @staticmethod
    def create_item_from_text(file_path):
        """Metin dosyasını okuyarak ürünleri oluşturur"""
        product_list = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        name, price, quantity = parts
                        try:
                            product = Product(name.strip(), float(price.strip()), int(quantity.strip()))
                            product_list.append(product)
                        except ValueError as e:
                            print(f"Hata: {e} - Satır: {line.strip()}")
                    else:
                        print(f"Geçersiz satır formatı: {line.strip()}")
        except FileNotFoundError:
            print(f"{file_path} bulunamadı.")
        
        return product_list
    
    @staticmethod
    def get_total_balance(products):
        """Ürünlerin toplam bakiyesini hesaplar ve %20 KDV ekler"""
        total_balance = 0
        for product in products:
            total_balance += product.get_total_price()
        
        # %20 KDV ekleyelim
        total_balance_with_tax = total_balance * 1.20
        return total_balance_with_tax

# Ana fonksiyon (test kodu)
if __name__ == "__main__":
    # Dosya yolu ve dosyanın içeriği
    file_path = "Products.txt"
    
    # Metin dosyasını kullanarak ürünleri oluştur
    product_list = ProductHelper.create_item_from_text(file_path)
    
    # Ürünlerin toplam bakiyesini hesapla ve yazdır
    if product_list:
        total_balance = ProductHelper.get_total_balance(product_list)
        print(f"Toplam Bakiye (KDV dahil): {total_balance} TL")
    else:
        print("Hiç ürün bulunamadı.")