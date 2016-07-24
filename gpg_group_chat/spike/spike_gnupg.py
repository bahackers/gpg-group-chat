from gnupg import GPG

gpg_test_fingerprint = "0E315D7E40CE9FDC28F9E7C6CFE237CCFF068D3E"
passphrase = "mate1234"

gpg = GPG(binary='/usr/bin/gpg2',
          homedir='~/.gnupg',
          keyring='pubring.gpg',
          secring='secring.gpg')

stored_keys = gpg.list_keys()

message = "This is a test message to be encripted."

options_enc = {
    'passphrase': passphrase,
    'armor': True,
    'default_key': gpg_test_fingerprint
    }
encrypted_msg = gpg.encrypt(message, gpg_test_fingerprint, **options_enc)

print(encrypted_msg)

options_dec = {
    'passphrase': passphrase
    }
decrypted_msg = gpg.decrypt(str(encrypted_msg), **options_dec)

assert message == str(decrypted_msg)

print("This is the original message:", decrypted_msg)

''' "Valid" will return a boolean saying whether the decrypted message's
signature is valid.'''
assert decrypted_msg.valid
