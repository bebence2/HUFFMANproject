def decode(inputpath, outputpath):
    #Decodes a file endoed using a custom huffman-like method
    #The input file uses the following structure 
    #Line 1: Characters separated by ';' (e.g., a;b;c;Enter)
    #Line 2: Corresponding Huffman codes separated by ';'
    #Line 3: Encoded string
    #input_path (str): Path to the encoded input file.
    #output_path (str): Path where the decoded output will be saved.

    try:
        # Read and validate input file
        with open(inputpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) < 3:
            raise ValueError("Input file must contain at least 3 lines (symbols, codes, encoded data).")

        # Extract symbol-code pairs and encoded data
        symbols = lines[0].strip().split(';')
        codes = lines[1].strip().split(';')
        encoded_text = lines[2].strip()

        if len(symbols) != len(codes):
            raise ValueError("Symbol and code lists must be the same length.")

        # Mapping from code to symbol
        code_map = dict(zip(codes, symbols))

        decoded_output = ""
        buffer = encoded_text

        # Decode the encoded text by matching prefixes, loops untill buffer get empty
        while buffer:
            matched = False
            for code, symbol in code_map.items():
                if buffer.startswith(code):
                    if symbol == "Enter":
                        decoded_output += "\n"
                    elif symbol == "Space":
                        decoded_output += " "
                    else:
                        decoded_output += symbol
                    buffer = buffer[len(code):] #Cuts the code from the beggining of the buffer
                    matched = True
                    break  # Restart loop after a match
            if not matched:
                raise ValueError("Unable to match code in encoded text. Possibly corrupted input.")

        # Write output to file
        with open(outputpath, 'w', encoding='utf-8') as f:
            f.write(decoded_output)

        # Print success messages
        print(decoded_output)
        print("Output written to:", outputpath)

    except FileNotFoundError:
        print(f"Error: File not found -> {inputpath}")
    except Exception as e:
        print(f"Decoding failed: {str(e)}")