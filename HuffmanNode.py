import heapq
from collections import  Counter

# Define a Huffman Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Compare nodes based on frequency for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Build the Huffman Tree
def build_huffman_tree(text):
    # Count the frequency of each character in the text
    freq_map = Counter(text)

    # Create a priority queue (min-heap)
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    # Build the tree by combining two smallest nodes until one node remains
    while len(heap) > 1:
        node1 = heapq.heappop(heap)  # Smallest node
        node2 = heapq.heappop(heap)  # Second smallest node

        # Combine the two nodes
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        # Add the merged node back to the heap
        heapq.heappush(heap, merged)

    # The root of the tree
    return heap[0]


# Generate Huffman Codes
def generate_huffman_codes(root):
    codes = {}

    def generate_codes_recursive(node, current_code):
        if not node:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes_recursive(node.left, current_code + "0")
        generate_codes_recursive(node.right, current_code + "1")

    generate_codes_recursive(root, "")
    return codes


# Compress the input text
def compress_text(text, codes):
    compressed = "".join(codes[char] for char in text)
    return compressed


# Decompress the binary string (for testing purposes)
def decompress_text(compressed, root):
    decompressed = []
    node = root
    for bit in compressed:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decompressed.append(node.char)
            node = root
    return "".join(decompressed)


# Main function for Team 1: Compression
def team1_compression(raw_text):
    print("Original Text:", raw_text)

    # Step 1: Build the Huffman Tree
    huffman_tree = build_huffman_tree(raw_text)

    # Step 2: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(huffman_tree)
    print("Huffman Codes:", huffman_codes)

    # Step 3: Compress the Text
    compressed_text = compress_text(raw_text, huffman_codes)
    print("Compressed Text (Binary):", compressed_text)

    return compressed_text, huffman_tree


# Example Usage
if __name__ == "__main__":
    raw_message = "Every great achievement begins with a simple idea"
    compressed_binary, huffman_tree = team1_compression(raw_message)
