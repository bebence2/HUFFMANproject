

#Thats one node on the tree, it contains their left (the most rare extisting item), 
#and their right (the next most rare item) child, the char of the node and their frequency


class NodeTree:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

#if its a leaf, it rturns that their children are None existent
    def is_leaf(self):
        return self.left is None and self.right is None


#Buid the frequency table, with all the characters and their frequency
def build_frequency_table(text_lines):
    freq = {}
    for line in text_lines:
        for char in line:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


#Builds the huffman tree, by sorting characters based on their frequencies
def build_huffman_tree(freq_table):
    nodes = []
    for char, freq in freq_table.items():
        nodes.append(NodeTree(char, freq))

    while len(nodes) > 1:
        # Find two nodes with the lowest frequencies
        nodes.sort(key=lambda node: node.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Create new internal node
        merged = NodeTree(None, left.freq + right.freq, left, right)
        nodes.append(merged)

    return nodes[0] if nodes else None

#Generating huffman codes based on the node's location on the tree
def generate_huffman_codes(node, code="", code_map=None):
    if code_map is None:
        code_map = {}

    if node.is_leaf():
        code_map[node.char] = code
        return code_map

    if node.left:
        generate_huffman_codes(node.left, code + "0", code_map)
    if node.right:
        generate_huffman_codes(node.right, code + "1", code_map)

    return code_map

#Encoding the input text using their huffman codes
def encode_text(text_lines, code_map):
    encoded = ""
    for line in text_lines:
        for char in line:
            encoded += code_map[char]
    return encoded


#Creating encoded output file, arraning lines
def write_encoded_file(path, code_map, encoded_text):
    with open(path, 'w+') as f:
        # Line 1: characters
        for char in code_map:
            if char == '\n':
                f.write("Enter")
            elif char == ' ':
                f.write("Space")
            else:
                f.write(char)
            f.write(";")
        f.write("\n")

        # Line 2: codes
        for char in code_map:
            f.write(code_map[char])
            f.write(";")
        f.write("\n")

        # Line 3: encoded binary text
        f.write(encoded_text)


# Main encoding function
def encode(input_path, output_path):
    with open(input_path) as f:
        text_lines = f.readlines()

    freq_table = build_frequency_table(text_lines)
    huffman_root = build_huffman_tree(freq_table)
    code_map = generate_huffman_codes(huffman_root)
    encoded_text = encode_text(text_lines, code_map)
    write_encoded_file(output_path, code_map, encoded_text)

    print("Output file saved at:", output_path)