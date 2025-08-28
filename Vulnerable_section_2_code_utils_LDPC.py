# ----- VN Start -----

 import numpy as np
 import random
 import math
 def ldpc_encode(data_bit_str, P):
     """
     Encode a 64-bit data string using the systematic LDPC encoder.
    
     Parity bits p = (P * d) mod 2. The full codeword is [data || parity].
     """
     if len(data_bit_str) != 64:
 def ldpc_decode_bp(received_codeword, H, p_channel=0.05, max_iter=100):
     """
     Decode a 128-bit LDPC codeword using belief propagation (sum-product algorithm).
    
     Args:
         received_codeword (str): 128-bit string (data and parity bits).
         H (np.array): Parity-check matrix of size (m x n) with n = 128.
         p_channel (float): Assumed error probability for the channel.
         max_iter (int): Maximum number of decoding iterations.
    
     Returns:
         str: Decoded 128-bit codeword as a string.
     """
         # Check if all parity-check equations are satisfied.
         syndrome = np.mod(H.dot(decoded), 2)
         if np.all(syndrome == 0):
            # Successful decoding.
             print(f"Converged in {iteration + 1} iterations")
             break
         
             for j in check_indices:
                 M_vc[j, i] = L_total[i] - M_cv[j, i]
     
    # Return the decoded codeword as a string.
     return "".join(str(bit) for bit in decoded)
 
 if __name__ == '__main__':
     # Generate LDPC matrices for a (128,64) code.
     P, H = generate_ldpc_matrices(k=64, m=64, row_weight=3)
     
     # Original 64-bit data.
    original_data = "1010101111001101111011110000111100001010101010101100110010101010"
     print("Original 64-bit Data:")
     print(original_data)
     
     # Encode the data.
    codeword = ldpc_encode(original_data, P)
     print("\nEncoded Codeword (128 bits):")
     print(codeword)
     
    # Introduce 2 random bit errors.
    corrupted_codeword = introduce_random_errors(codeword, num_errors=5)
    print("\nCorrupted Codeword (128 bits) with 2 bit errors:")
     print(corrupted_codeword)
    
     print("Positions of errors:", [i for i, (a, b) in enumerate(zip(codeword, corrupted_codeword)) if a != b])

     # Decode using the belief propagation decoder.
     recovered_codeword = ldpc_decode_bp(corrupted_codeword, H, p_channel=0.05, max_iter=100)
     print("\nRecovered Codeword (128 bits) with BP decoding:")
     else:
         print("\nWarning: Recovered data does not match the original data.")
         print("Positions of errors:", [i for i, (a, b) in enumerate(zip(original_data, recovered_data)) if a != b])

# ----- VN End -----
\ No newline at end of file