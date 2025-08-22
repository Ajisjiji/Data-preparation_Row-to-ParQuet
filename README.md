# Data-preparation_Row-to-ParQuet
Parquet encryption and decryption is performed in the Spark workers. Therefore, sensitive data and the encryption keys are not visible to the storage.
Standard Parquet features, such as encoding, compression, columnar projection and predicate push-down, continue to work as usual on files with Parquet modular encryption format.
