from Decoder import DecodeASecret
from Secret_Sharing import Secret


def main(secret):
    sectet = Secret(secret)
    decoder = DecodeASecret(sectet.lst_of_vectors, sectet.lst_of_teachers)
    return decoder.output(decoder.decode())



