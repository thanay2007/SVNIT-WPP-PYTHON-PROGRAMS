def decode_message(s, index=0, path="", results=None):
    if results is None:
        results = []
    if index == len(s):
        results.append(path)
        return results
    
    if s[index] != '0':
        decode_message(s, index + 1, path + chr(int(s[index]) + 64), results)
    
    if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
        decode_message(s, index + 2, path + chr(int(s[index:index+2]) + 64), results)
    
    return results

encoded_message = "11106"
decoded_messages = decode_message(encoded_message)
print("Possible Decoded Messages:", decoded_messages)
