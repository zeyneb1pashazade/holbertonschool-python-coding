#!/usr/bin/python3
"""
Modül 4-square: Bir kare sınıfı tanımlar ve boyutu için özel alıcı/ayarlayıcı
(getter/setter) metotları ile birlikte kareyi yazdıran bir metot içerir.
"""


class Square:
    """
    Square sınıfı, özel bir __size özniteliğine sahiptir, bu özniteliği
    yönetmek için `@property` kullanır ve kareyi `#` karakteriyle yazdırabilir.
    """

    def __init__(self, size=0):
        """
        Square sınıfının yeni bir örneğini başlatır.

        Args:
            size (int, optional): Karenin boyutu. Varsayılanı 0'dır.
        """
        # Setter metodunu çağırarak doğrulama yapıyoruz.
        self.size = size

    @property
    def size(self):
        """
        Karenin boyutunu (__size) alır (getter metodu).

        Returns:
            int: Karenin güncel boyutu.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Karenin boyutunu (__size) ayarlar (setter metodu).

        Args:
            value (int): Karenin ayarlanacak yeni boyutu.

        Raises:
            TypeError: value bir tam sayı (integer) değilse.
            ValueError: value 0'dan küçükse.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Karenin güncel alanını hesaplar ve döndürür.

        Returns:
            int: Karenin alanı (__size * __size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Karenin boyutuna göre, `#` karakterini kullanarak kareyi standart
        çıktıya (stdout) yazdırır.

        Eğer boyut (size) 0 ise, sadece boş bir satır yazdırılır.
        """
        if self.__size == 0:
            print("")
        else:
            # Boyut kadar satır (yükseklik) ve her satırda boyut kadar '#'
            # (genişlik) yazdırırız.
            for i in range(self.__size):
                print("#" * self.__size)
