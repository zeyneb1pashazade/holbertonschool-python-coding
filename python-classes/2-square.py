#!/usr/bin/python3
"""
Modül 2-square: Bir kare sınıfı tanımlar.

Bu modül, bir karenin boyutunu (size) kontrol eden ve alanını (area)
hesaplayan özelliklere sahip Square sınıfını içerir.
"""


class Square:
    """
    Square sınıfı, bir karenin boyutunu ve alanını yönetir.

    Özel öznitelik: __size (int): Karenin kenar uzunluğu.
    """

    def __init__(self, size=0):
        """
        Square sınıfının yeni bir örneğini başlatır.

        Args:
            size (int, optional): Karenin boyutu. Varsayılanı 0'dır.

        Raises:
            TypeError: size bir tam sayı (integer) değilse.
            ValueError: size 0'dan küçükse.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Karenin güncel alanını hesaplar ve döndürür.

        Returns:
            int: Karenin alanı (__size * __size).
        """
        return self.__size * self.__size
