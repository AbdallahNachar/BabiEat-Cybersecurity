## Digital Signatures

Digital signatures provide cryptographic proof of document authenticity, integrity, and non-repudiation. They serve as the electronic equivalent of handwritten signatures but offer far superior security guarantees through mathematical verification.

### How Digital Signatures Work
Digital signatures use asymmetric cryptography in reverse. The signer uses their private key to create a unique digital signature for a document, while recipients use the signer's public key to verify the signature's authenticity. This process ensures that only the private key holder could have created the signature.

### The Signing Process
1. **Hash Generation**: The document is processed through a cryptographic hash function (like SHA-256) to create a unique fixed-size digest
2. **Signature Creation**: The hash is encrypted using the signer's private key, creating the digital signature
3. **Attachment**: The signature is attached to or bundled with the original document
4. **Distribution**: The signed document is sent to recipients along with the signer's public key or certificate

### Verification Process
Recipients verify digital signatures by:
1. **Hash Calculation**: Computing the hash of the received document using the same algorithm
2. **Signature Decryption**: Using the signer's public key to decrypt the digital signature, revealing the original hash
3. **Comparison**: Comparing the calculated hash with the decrypted hash
4. **Validation**: If the hashes match, the signature is valid and the document is authentic and unmodified

### Key Properties and Benefits

**Authentication**: Digital signatures prove the identity of the signer, confirming that the document came from the claimed source. This relies on the assumption that only the legitimate signer possesses the private key.

**Integrity**: Any alteration to the signed document will result in a different hash, causing signature verification to fail. This provides tamper-evidence superior to traditional signatures.

**Non-repudiation**: Signers cannot deny having signed a document, as the signature can only be created with their private key. This provides legal enforceability in digital transactions.

**Efficiency**: Unlike handwritten signatures, digital signatures can be verified automatically by software systems, enabling high-volume processing of signed documents.

### Common Standards and Algorithms
- **RSA-PSS**: Robust signature scheme based on RSA with probabilistic signature padding
- **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Provides equivalent security to RSA with smaller key sizes
- **DSA (Digital Signature Algorithm)**: NIST standard for digital signatures
- **EdDSA**: Modern signature scheme offering high performance and security

### Digital Certificates and PKI
Digital signatures typically operate within Public Key Infrastructure (PKI) systems. Digital certificates, issued by Certificate Authorities (CAs), bind public keys to identities and provide trust chains. This infrastructure enables signature verification even when signers and verifiers don't know each other directly.

### Legal and Regulatory Framework
Many jurisdictions recognize digital signatures as legally equivalent to handwritten signatures. Standards like the EU's eIDAS regulation and the US ESIGN Act provide legal frameworks for digital signature acceptance. However, some documents may still require traditional signatures due to regulatory requirements.

### Applications and Use Cases
Digital signatures are essential in:
- **Software Distribution**: Ensuring downloaded software hasn't been tampered with
- **Financial Transactions**: Authorizing electronic payments and contracts
- **Email Security**: S/MIME and PGP use digital signatures for email authentication
- **Document Management**: Legal contracts, medical records, and official documents
- **Code Signing**: Verifying the authenticity of applications and drivers
- **Blockchain**: Transaction validation in cryptocurrency systems

### Limitations and Considerations
Digital signature security depends entirely on private key protection. Compromised private keys invalidate all signatures created with them. Key management, including secure storage, backup, and revocation procedures, becomes critical. Additionally, signature verification requires access to current and valid public keys or certificates.

