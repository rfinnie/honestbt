# honestbt, The Honest Block Tester

```honestbt``` is a program which writes AES-CTR-encrypted data (using a random or specified key) to a block device, then reads back, decrypts and verifies.  It is designed to write seemingly random, non-patterned data but does not need a full reference copy to verify.

It has the following applications:

 * Testing flash drives for counterfeits which may report a larger drive size than what is actually available (e.g. reports itself as a 64GiB drive, but really only has 4GiB and the last 2GiB loops upon itself internally).
 * General-purpose data-destructive drive testing.
 * Single-pass ```shred``` replacement.
 * Simple drive performance test.

**This program works by completely overwriting a block device with essentially garbage, take care to avoid data loss!**

## Current status

"90% functionally done, throw it on GitHub."