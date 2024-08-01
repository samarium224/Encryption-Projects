from huffman import HuffmanCoding
import sys

path = r"E:\Friends\Encryption\sample.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress('E:\Friends\Encryption\sample.bin')
print("Decompressed text: " + decom_path)